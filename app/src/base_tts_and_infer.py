import subprocess
import os
from tqdm import tqdm
# from so_vits_svc_fork.inference.main import 

import requests
import zipfile
import tempfile
import os
import json
import time

class AudioAPI:
    def __init__(self, api_key, api_url='https://api.narakeet.com', polling_interval=5):
        self.api_key = api_key
        self.api_url = api_url
        self.polling_interval = polling_interval

    def request_audio_task(self, format, text, voice):
        url = f'{self.api_url}/text-to-speech/{format}?voice={voice}'
        options = {
            'headers': {
                'Content-Type': 'text/plain',
                'x-api-key': self.api_key,
            },
            'data': text.encode('utf8')
        }
        response = requests.post(url, **options)
        response.raise_for_status()
        return response.json()

    def request_vtt_task(self, vtt_file, voice, voice_speed = 1, format = 'mp3'):
        url = f'{self.api_url}/text-to-speech/{format}?voice={voice}&voice-speed={voice_speed}'
        with open(vtt_file, 'r', encoding='utf-8') as f:
            text = f.read()
            options = {
                'headers': {
                    'Content-Type': 'text/vtt',
                    'x-api-key': self.api_key,
                },
                'data': text.encode('utf8')
            }
            response = requests.post(url, **options)
            response.raise_for_status()
        return response.json()


    def poll_until_finished(self, task_url, progress_callback=None):
        while True:
            response = requests.get(task_url)
            response.raise_for_status()
            data = response.json()
            if data.get('finished', False):
                break

            if progress_callback:
                progress_callback(data)

            time.sleep(self.polling_interval)

        return data

    def download_to_file(self, url, file):
        with open(file, 'wb') as f:
            f.write(requests.get(url).content)



def gen_audio(text):
    api_key = '9TR3ykPcWb7zo6vUMpXqv3Q4SQIt4ZLa7nVWLCLI'
    format = "wav"
    voice = "nitesh"
    script = text

    def show_progress(progress_data):
        # change this to do something smarter with percent and message
        print(progress_data)

    api = AudioAPI(api_key)

    # start a build task using the text sample and voice
    # and wait for it to finish
    task = api.request_audio_task(format, script, voice)
    task_result = api.poll_until_finished(task['statusUrl'], show_progress)

    # grab the result file
    if task_result['succeeded']:
        filename = f'output.{format}'
        api.download_to_file(task_result['result'], filename)
        print(f'downloaded to {filename}')
        print(os.getcwd()+'/'+filename)
        return os.getcwd()+'/'+filename
    else:
        raise Exception(task_result['message'])


if __name__ == '__main__':
##
    base_path = './polycab/mul3'
    base_audio = os.listdir(base_path)
    base_audio = [x for x in base_audio if x.endswith('.wav')]


    # base_audio = gen_audio("Dear Ashu Jee") #narkeet call

    conv_path = 'polycab/res5'
    if not os.path.exists(conv_path):
        os.makedirs(conv_path)

    for i in tqdm(base_audio):

        subprocess.call(['svc', 'infer', '-m', 'polycab/G_1000.pth' ,'-c' ,'polycab/config.json', base_path + '/' + i, '-o',conv_path + '/' + i])
        # break
