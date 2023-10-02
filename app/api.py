from flask import Flask, request
from flask_restful import Resource, Api
import json
from sys import platform
import os
from so_vits_svc_fork.inference.main import infer

from src.train_clone_voice import Audio_split, TestMain
from src.base_tts_and_infer import gen_audio
import  time
import torch
import shutil
from pathlib import Path
from threading import Thread
from src.utils import AwsBackNFro, get_optimal_device, vid_to_aud
from src.stt_tts import TranslateFull

app = Flask(__name__)
api = Api(app)


#configs
BASE_DATA_FOLDER = os.path.join(Path(os.getcwd()).parent.absolute(),'data')
remove_file_list = ['configs', 'dataset', 'dataset_raw', 'filelists', 'logs', 'res']
DEVICE = get_optimal_device()

class DubNow(Resource):
    def post(self):

        if 'video' not in request.files:
            return ({"Error": "Please Provide Video File"}, 400)
        if 'user_id' not in request.form:
            return ({"Error": "Please Provide User ID"}, 400)
        if 'project_id' not in request.form:
            return ({"Error": "Please Provide Project ID"}, 400)
        if 'language' not in request.form:
            return ({"Error": "Please Provide Language"}, 400)

        video_file = request.files['video']
        video_file_name = video_file.filename
        user_id = request.form['user_id']
        project_id = request.form['project_id']
        language = request.form['language']

        # Base project folder

        BASE_PROJECT_FOLDER = os.path.join(BASE_DATA_FOLDER,user_id,project_id)
        if os.path.exists(BASE_PROJECT_FOLDER):
            shutil.rmtree(BASE_PROJECT_FOLDER)
        if not os.path.exists(BASE_PROJECT_FOLDER):
            os.makedirs(BASE_PROJECT_FOLDER)
        
        #save video file
        save_vid_folder = "input_video"
        save_vid_path = os.path.join(BASE_PROJECT_FOLDER, save_vid_folder)
        if not os.path.exists(save_vid_path):
            os.makedirs(save_vid_path)
        
        save_vid_path = os.path.join(save_vid_path, video_file_name)
        request.files['video'].save(os.path.join(save_vid_path))

        # converted video to audio
        save_audio_folder = "input_audio"
        save_audio_path = os.path.join(BASE_PROJECT_FOLDER, save_audio_folder)
        if not os.path.exists(save_audio_path):
            os.makedirs(save_audio_path)
        vid_to_aud(save_vid_path, save_audio_path)
        save_audio_path_file = os.path.join(save_audio_path, 'audio.wav')

        spl_au = Audio_split()

        BASE_VOICE_CLONE_FOLDER = os.path.join(BASE_PROJECT_FOLDER, 'voice_cloning')
        resp = spl_au.splitter(audio_path=save_audio_path_file, out_path=BASE_VOICE_CLONE_FOLDER, split_sec=8)
        if resp['status'] == 0:
            return (resp['reason'], 400) 
        if resp['status'] == 1:
            print("Traning Will start Shortly")

        svc = TestMain()
        # svc.preprocess(base_path=BASE_PROJECT_FOLDER)
        EPOCH = 1000

        #starting thread for training
        Thread(target=svc.preprocess_n_train, args=(BASE_VOICE_CLONE_FOLDER,EPOCH,500)).start()



        tranF = TranslateFull()

        # tranF.stt_whisper
        stt_folder = os.path.join(BASE_PROJECT_FOLDER, 'stt')
        if not os.path.exists(stt_folder):
            os.makedirs(stt_folder)
        tranF.stt_whisper(save_audio_path_file,stt_folder)

        # tranF.translate
        stt_txt_folder = os.path.join(stt_folder,'transcript.txt')
        translate_folder = os.path.join(BASE_PROJECT_FOLDER, 'translate')
        if not os.path.exists(translate_folder):
            os.makedirs(translate_folder)
        tranF.translate(stt_txt_folder,translate_folder, language)

        # tranF.tts_narket
        translate_txt_folder = os.path.join(translate_folder,'translated.txt')
        tts_folder = os.path.join(BASE_PROJECT_FOLDER, 'tts')
        if not os.path.exists(tts_folder):
            os.makedirs(tts_folder)
        base_main_audio_path = tranF.tts_narket(translate_txt_folder,tts_folder)

        print("base_main_audio_path",base_main_audio_path)
        
        # if not os.path.exists(os.path.join(BASE_PROJECT_FOLDER,'audio_infer.json')):
        #     with open(os.path.join(BASE_PROJECT_FOLDER,'audio_infer.json'), 'w') as f:
        #         json.dump({"audio_path":base_main_audio_path}, f)

        # svc.infer(base_audio_path=base_main_audio_path, BASE_PROJECT_FOLDER=BASE_PROJECT_FOLDER)

        return ({"status": 1,
                 "user_id": user_id,
                 "project_id": project_id}, 200)

class InfefDub(Resource):
    def post(self):
        if 'user_id' not in request.form:
            return ({"Error": "Please Provide User ID"}, 400)
        if 'project_id' not in request.form:
            return ({"Error": "Please Provide Project ID"}, 400)

        user_id = request.form['user_id']
        project_id = request.form['project_id']

        BASE_PROJECT_FOLDER = os.path.join(BASE_DATA_FOLDER,user_id,project_id)
        BASE_PROJECT_FOLDER_CLONE = os.path.join(BASE_DATA_FOLDER,user_id,project_id, 'voice_cloning')

        with open(os.path.join(BASE_PROJECT_FOLDER_CLONE, 'train_progress.json')) as f:
            a = json.load(f)
            if a['Progress'] < 99:
                return ({"model_training":1},200)

        source_wav = os.path.join(BASE_PROJECT_FOLDER,'tts','audio.wav')

        svc = TestMain()
        output = svc.infer(base_audio_path=source_wav, BASE_PROJECT_FOLDER=BASE_PROJECT_FOLDER_CLONE)
        return (output, 200)

class TrainProgress(Resource):
    def get(self):
        # if 'user_id' not in request.data:
        #     return ({"Error": "Please Provide User ID"}, 400)
        # if 'project_id' not in request.data:
        #     return ({"Error": "Please Provide Project ID"}, 400)
        
        req_data = json.loads(request.data.decode('utf-8'))
        user_id = str(req_data['user_id'])
        project_id = str(req_data['project_id'])

        BASE_PROJECT_FOLDER = os.path.join(BASE_DATA_FOLDER,user_id,project_id, 'voice_cloning')

        try:
            prog_file = os.path.join(BASE_PROJECT_FOLDER, 'train_progress.json') 
            with open(prog_file) as f:
                a = json.load(f)
                if a['Progress'] == 99:
                    a['Progress']+=1
                return a
        except:
            return {"Progress":0}

api.add_resource(DubNow, '/dubnow')
api.add_resource(InfefDub, '/infer_dub')
api.add_resource(TrainProgress, '/train_progress')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8099)

        