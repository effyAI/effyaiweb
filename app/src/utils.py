import boto3
import os
import torch

import os


class AwsBackNFro():
    def __init__(self):
        self.aws_access_key_id = "AKIAVZBVXJWJLAWNRCWZ"
        self.aws_secret_access_key="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"
        self.region_name="us-east-1"

        self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key,
                              region_name=self.region_name)
        
        self.s3_bucket = boto3.resource('s3', aws_access_key_id=self.aws_access_key_id,
                          aws_secret_access_key=self.aws_secret_access_key,
                          region_name=self.region_name)

        self.bucket_name = 'effy-voicecloning'

    def upload(self, file_obj, file_path):
        self.s3.upload_fileobj(file_obj, self.bucket_name, file_path)
        s3_url = f'https://{self.bucket_name}.s3.amazonaws.com/{file_obj.filename}'
        return s3_url

    def download(self, file_path, local_file_path):
        self.s3.download_file(self.bucket_name, file_path, local_file_path)
        return local_file_path

    def upload_dict(self, file_dict):
        for subdir, dirs, files in os.walk(file_dict):
            for file in files:
                full_path = os.path.join(subdir, file)
                with open(full_path, 'rb') as data:
                    self.s3_bucket.Bucket(self.bucket_name).put_object(Key=full_path[len(file_dict)+1:], Body=data)

        print("Folders Uploaded to S3")

def get_optimal_device(index: int = 0) -> torch.device:
    if torch.cuda.is_available():
        return torch.device(f"cuda:{index % torch.cuda.device_count()}")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

def vid_to_aud(video_path, save_audio_path):
    print("[+] Converting Video to Audio")
    os.system(f"ffmpeg -i {video_path} -ab 160k -ac 1 -ar 22050 -vn {save_audio_path}/audio.wav -y")
    print("[+] Video to Audio Conversion Done")

def vocal_extractor(mus_path, out_path, ):
    import demucs.separate

    ptm_name = "mdx_extra" #pre trained model name
    input_audio_name = mus_path.split('/')[-1].split('.')[0]

    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", ptm_name, mus_path, "-o",out_path,"--segment","20"])

    ##return extracted vocals path
    return os.path.join(out_path, ptm_name, input_audio_name)


# if __name__ == "__main__":
#     stt_whisper("audio.wav", "output_folder")