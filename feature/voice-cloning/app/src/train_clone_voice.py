import json
import os
from pathlib import Path
import shutil
import sys

class Audio_split():
    def splitter(self, audio, split_sec = 8) -> str:
        '''Will return split audio path'''
        import librosa
        import soundfile as sf
        import os

        out_path = 'dataset_raw/sp1'
        file_path = audio
        min_split_sec = split_sec # range min_split_sec - till word complete


        if not os.path.exists(out_path):
            os.makedirs(out_path)

        y, sr = librosa.load(file_path, mono=True, sr=22050)
        duration = librosa.get_duration(y=y, sr=sr)
        # y = librosa.to_mono(y)
        print(y.shape, sr, duration, len(y)/sr, len(y)/duration)

        if duration/60 < 1.5:
            print("Short Sample")
            return {'status':0,
                    'reason':'Short Sample'}


        y_split = librosa.effects.split(y, top_db=30,)

        def time_spliter(y_split, y,out_path, sr=22050):
            i = 0
            p1 = 0

            while p1<len(y_split):
                start = y_split[p1][0]
                p1+=1
                if p1 >= len(y_split):
                    break
                while (y_split[p1][1] - start) <= sr*min_split_sec:
        #             print((y_split[p1][1] - start) / sr , (y_split[p1][1] - start) / sr  <= 8, 8)
                    if p1>=len(y_split):
                        break
                    p1+=1
                    
                    # print(p1,"here")
                # print(p1,len(y_split))
                print((y_split[p1][1] - start) / sr , (y_split[p1][1] - start) / sr, "Writing:-","{}.wav".format(i))
                sf.write('{}/{}.wav'.format(out_path,i), y[start:y_split[p1][1]], 22050, 'PCM_24')
                p1+=1
                i+=1
            
        try:
            time_spliter(y_split, y, out_path, sr=22050)
        except IndexError as e:
            pass
        return {'status':1,
                'f_path': ' out_path'}

class TestMain():
    def __init__(self) -> None:
        # import so_vits_svc_fork.cluster.train_cluster  # noqa
        import so_vits_svc_fork.inference.main 
        import so_vits_svc_fork.preprocessing.preprocess_flist_config 
        import so_vits_svc_fork.preprocessing.preprocess_hubert_f0 
        import so_vits_svc_fork.preprocessing.preprocess_resample 
        import so_vits_svc_fork.preprocessing.preprocess_split 
        import so_vits_svc_fork.train

    def preprocess(self):
        from so_vits_svc_fork.preprocessing.preprocess_resample import (
            preprocess_resample,
        )
        preprocess_resample(
            "dataset_raw", "dataset/44k", 44100, n_jobs=-1 # tunable
        )

        from so_vits_svc_fork.preprocessing.preprocess_flist_config import (
            preprocess_config,
        )

        preprocess_config(
            "dataset/44k",
            "filelists/train.txt",
            "filelists/val.txt",
            "filelists/test.txt",
            "configs/44k/config.json",
            "so-vits-svc-4.0v1",
        )


        from so_vits_svc_fork.preprocessing.preprocess_hubert_f0 import (
            preprocess_hubert_f0,
        )

        preprocess_hubert_f0("dataset/44k", "configs/44k/config.json")

        if not os.path.exists('logs/44k'):
            os.makedirs('logs/44k')

        shutil.copy('configs/44k/config.json', 'logs/44k/config.json')

    def train(self, epochs=1000, eval_interval=500):

        from so_vits_svc_fork.train import train

        config_path = Path("logs/44k/config.json")
        config_json = json.loads(config_path.read_text("utf-8"))
        config_json["train"]["epochs"] = epochs
        config_json["train"]["eval_interval"] = eval_interval

        config_path.write_text(json.dumps(config_json), "utf-8")

        prog = {"Progress":0}
        prog_file = os.getcwd()+'/'+'train_progress.json' 
        with open(prog_file,'w') as f:
            json.dump(prog, fp=f)
        # print("---------------------------------",prog_file)
        train(config_path, "logs/44k", prog_file)
    
    
    def infer(self):
        from so_vits_svc_fork.inference.main import infer  # noqa

        # infer("dataset_raw/34j/1.wav", "configs/config.json", "logs/44k")

if __name__ == '__main__':
    spl_au = Audio_split()

    resp = spl_au.splitter(audio='./ajit_pawar_base.wav', split_sec=8)
    if resp['status'] == 0:
        print(resp['reason'])
        sys.exit(0)
    if resp['status'] == 1:
        print("Traning Will shart Shortly")

    svc = TestMain()
    svc.preprocess()
    svc.train()
