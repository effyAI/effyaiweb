from flask import Flask, request
from flask_restful import Resource, Api
import json
from sys import platform
import os
from so_vits_svc_fork.inference.main import infer

from train_clone_voice import Audio_split, TestMain
from base_tts_and_infer import gen_audio
import  time
import torch
import shutil

app = Flask(__name__)
api = Api(app)

BASE_CLONE_FOLDER = 'VoiceToClone'
if not os.path.exists(BASE_CLONE_FOLDER):
    os.makedirs(BASE_CLONE_FOLDER)

remove_file_list = ['configs', 'dataset', 'dataset_raw', 'filelists', 'logs', 'res']

def get_optimal_device(index: int = 0) -> torch.device:
    if torch.cuda.is_available():
        return torch.device(f"cuda:{index % torch.cuda.device_count()}")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        try:
            import torch_xla.core.xla_model as xm  # noqa

            if xm.xrt_world_size() > 0:
                return torch.device("xla")
            # return xm.xla_device()
        except ImportError:
            pass
    return torch.device("cpu")

class CloneAudio(Resource):
    def post(self):
        # print(request.files['source_wav_file'].filename)
        for rmf in remove_file_list:
            if os.path.exists(rmf):
                print('[+] Cleaning - {}'.format(rmf))
                shutil.rmtree(os.getcwd()+'/'+rmf)


        save_path = "{}/Testaudio.wav".format(BASE_CLONE_FOLDER)
        request.files['source_wav_file'].save(save_path)

        ## spliting and training in on voice
        spl_au = Audio_split()

        resp = spl_au.splitter(audio=save_path, split_sec=8)
        if resp['status'] == 0:
            return (resp['reason'], 400) 
        if resp['status'] == 1:
            print("Traning Will start Shortly")

        svc = TestMain()
        svc.preprocess()
        EPOCH = 1000
        svc.train(epochs=EPOCH)

        g_path = os.getcwd()+'/logs/44k/G_{}.pth'.format(EPOCH)
        c_path = os.getcwd()+'/logs/44k/config.json'
        return ({"Sucess": "Trained Sucess Fully",
                 "g_path": g_path,
                 "c_path": c_path}, 200)

    def get(self):
        print(request.data)

class InferAudio(Resource):
    def post(self):
        req_data = json.loads(request.data.decode('utf-8'))

        text = req_data['text']
        g_path = req_data['g_path']
        c_path = req_data['c_path']

        base_aud_path = gen_audio(text=text)

        conv_path = 'res'
        if not os.path.exists(conv_path):
            os.makedirs(conv_path)

        res_file = os.getcwd()+'/'+conv_path+'/'+'test_{}.wav'.format(time.strftime("%d_%m_%Y_%H_%M_%S"))
        # subprocess.call(['svc', 'infer', '-m', g_path ,'-c' ,c_path, base_aud_path, '-o',res_file])
        infer(
            # paths
            input_path=base_aud_path,
            output_path=res_file,
            model_path=g_path,
            config_path=c_path,
            recursive=False,
            # svc config
            speaker=str,
            cluster_model_path=None,
            transpose=0,
            auto_predict_f0=True,
            cluster_infer_ratio=0,
            noise_scale=0.4,
            f0_method="dio",
            # slice config
            db_thresh = -20,
            pad_seconds = 0.5,
            chunk_seconds = 0.5,
            absolute_thresh=False,
            max_chunk_seconds=40,
            device=get_optimal_device(),
        )

        return ({"file_path": res_file}, 200)

class ProgressStats(Resource):
    def get(self):
        prog_file = os.getcwd()+'/'+'train_progress.json' 
        with open(prog_file) as f:
            a = json.load(f)
            a['Progress']+=1
            return a

api.add_resource(InferAudio, '/infer/')
api.add_resource(CloneAudio, '/clone/')
api.add_resource(ProgressStats, '/progress/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)