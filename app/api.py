from flask import Flask, request
from flask_restful import Resource, Api

import os
import shutil
from pathlib import Path

from src.utils import get_optimal_device, vocal_extractor

app = Flask(__name__)
api = Api(app)


#configs
BASE_DATA_FOLDER = os.path.join(Path(os.getcwd()).parent.absolute(),'data')
remove_file_list = ['configs', 'dataset', 'dataset_raw', 'filelists', 'logs', 'res']
DEVICE = get_optimal_device()

class ExtractAudios(Resource):
    def post(self):

        if 'audio' not in request.files:
            return ({"Error": "Please Provide Video File"}, 400)
        if 'user_id' not in request.form:
            return ({"Error": "Please Provide User ID"}, 400)
        if 'project_id' not in request.form:
            return ({"Error": "Please Provide Project ID"}, 400)

        audio_file = request.files['audio']
        audio_file_name = audio_file.filename
        user_id = request.form['user_id']
        project_id = request.form['project_id']

        # Base project folder

        BASE_PROJECT_FOLDER = os.path.join(BASE_DATA_FOLDER,project_id,user_id)
        # if os.path.exists(BASE_PROJECT_FOLDER):
        #     shutil.rmtree(BASE_PROJECT_FOLDER)
        if not os.path.exists(BASE_PROJECT_FOLDER):
            os.makedirs(BASE_PROJECT_FOLDER)
        
        #save video file
        save_aud_folder = "input_audio"
        save_aud_path = os.path.join(BASE_PROJECT_FOLDER, save_aud_folder)
        if not os.path.exists(save_aud_path):
            os.makedirs(save_aud_path)
        
        save_aud_path = os.path.join(save_aud_path, audio_file_name)
        request.files['audio'].save(os.path.join(save_aud_path))
        # print(save_aud_path)

        #extract vocals
        out_path = os.path.join(BASE_PROJECT_FOLDER, 'ectracted_vocals')
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        out_vocal_aud_path = vocal_extractor(mus_path=save_aud_path, out_path=out_path)

        out_audio_files = {}
        for subdir, dirs, files in os.walk(out_vocal_aud_path):
            for file in files:
                full_path = os.path.join(subdir, file)
                out_audio_files[file] = full_path
            
        # print(out_audio_files)

        return ({"status": 1,
                 "user_id": user_id,
                 "project_id": project_id,
                 "out_music":out_audio_files}, 200)

api.add_resource(ExtractAudios, '/extract_vocals')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8099)

        