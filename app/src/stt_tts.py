
# importing the module
from googletrans import Translator
import whisper
import glob
import pandas as pd
from tqdm import tqdm
import os
from .base_tts_and_infer import gen_audio
import shutil
import torch

class TranslateFull():
    def stt_whisper(self,audio_path, output_folder):
        model = whisper.load_model("large-v2")
        result = model.transcribe(audio_path)
        torch.cuda.empty_cache() # realease gpu memory
        output = result["text"].lstrip()
        output = output.replace("\n","")
        # print(result)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if os.path.exists(f"{output_folder}/transcript.txt"):
            os.remove(f"{output_folder}/transcript.txt")

        with open(f"{output_folder}/transcript.txt", "w") as f:
            f.write(output)

    def translate(self,transcript_path, output_folder, language):
        with open(transcript_path, "r") as f:
            transcript = f.read()

        translator = Translator()

        translated_out = translator.translate(transcript, dest=language)
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if os.path.exists(f"{output_folder}/translated.txt"):
            os.remove(f"{output_folder}/translated.txt")

        with open(f"{output_folder}/translated.txt", "w") as f:
            f.write(translated_out.text)

    def tts_narket(self,translated_path, output_folder):
        with open(translated_path, "r") as f:
            transcript = f.read()
        
        ##will remove later
        # transcript = transcript[:250]
        #

        base_audio_path = gen_audio(transcript)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if os.path.exists(f"{output_folder}/audio.wav"):
            os.remove(f"{output_folder}/audio.wav")

        shutil.move(base_audio_path, f"{output_folder}/audio.wav")
        return f"{output_folder}/audio.wav"