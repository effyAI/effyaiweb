import uuid
import subprocess
import ffmpeg
import cv2
from .database import upload_image_to_s3
from .models.psp import pSp
from .utils.common import tensor2im
from .datasets.augmentations import AgeTransformer
from .scripts.align_all_parallel import align_face
from argparse import Namespace
import os
import sys
import pprint
import numpy as np
import time
from PIL import Image
import torch
import torchvision.transforms as transforms
import requests
from io import BytesIO
sys.path.append(".")
sys.path.append("..")
# sys.path.append('/home/ubuntu/effyaiweb/src')

# Video Conversion


def age_input(input1, input2, input3, input4, input5):
    # if len(sys.argv) != 5:
    #     print(f'current len of agruments: {len(sys.argv)}')
    #     print("Usage: python script.py Input_path Output_Dir Current_Age Require_Age")
    #     sys.exit(1)
    # arg1 = sys.argv[1] # Input Path
    # arg2 = sys.argv[2] # Output Dir
    # arg3 = int(sys.argv[3]) # Current Age
    # arg4 = int(sys.argv[4]) # Required Age

    start_time = time.time()

    arg1 = input1
    net = input2
    arg3 = input3
    arg4 = input4
    uuid1 = input5

    print(os.getcwd())

    # Model Config Files
    EXPERIMENT_TYPE = 'ffhq_aging'
    EXPERIMENT_DATA_ARGS = {
        "ffhq_aging": {
            "model_path": "effyaiweb/app/src/pretrained_models/sam_ffhq_aging.pt",
            "image_path": "notebooks/images/866.jpg",
            "transform": transforms.Compose([
                transforms.Resize((256, 256)),
                transforms.ToTensor(),
                transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
        }
    }
    EXPERIMENT_ARGS = EXPERIMENT_DATA_ARGS[EXPERIMENT_TYPE]
    model_path = EXPERIMENT_ARGS['model_path']

    # if not os.path.exists(model_path):
    #     print('Download pretained model and save it in "app/src/pretained_models" dir or if already downloaded then save the model path correctly')
    #     return 'null'
    # ckpt = torch.load(model_path, map_location='cpu')
    # opts = ckpt['opts']
    # pprint.pprint(opts)
    # opts['checkpoint_path'] = model_path
    # opts = Namespace(**opts)
    # net = pSp(opts)

    net.eval()
    net.cuda()
    print('Model successfully loaded!')

    # Download Image from URL
    input_url = arg1  # Input Image
    downloaded_img_path = f'/home/ubuntu/development/effyaiweb/app/src/input/{uuid1}.jpg'
    try:
        response = requests.get(input_url)
    except:
        print('Invalid URL Response')
        return {'error': 404}
    if response.status_code == 200:
        # Open the image using PIL (Python Imaging Library)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        print(f"Image Shape: {img.size[0]}x{img.size[1]} pixels")
        # Save the image locally
        img.save(downloaded_img_path)
        print(f"Image downloaded and saved as '{uuid}.jpg'")
        print('Image Size: ', os.path.getsize(downloaded_img_path))
    else:
        print("Failed to download the image. Status code:", response.status_code)
        return {'error': 404}

    original_image = Image.open(
        downloaded_img_path).convert("RGB")  # Input URL
    # image_path = arg1 # Input Path
    # original_image = Image.open(image_path).convert("RGB") # Input Path
    original_image.resize((256, 256))

    print('image resized...')

    def run_alignment(image_path):
        print('starting face detection')
        import dlib
        predictor = dlib.shape_predictor(
            "/home/ubuntu/development/effyaiweb/app/src/shape_predictor_68_face_landmarks.dat")
        mediapipe = True # True: MediaPipe and False: dlib
        if mediapipe:
            aligned_image = align_face(filepath=image_path, predictor=predictor, dlib=False)
        else:
            aligned_image = align_face(filepath=image_path, predictor=predictor, dlib=True)

        if isinstance(aligned_image, str) and aligned_image == 'No Face Found':
            os.unlink(downloaded_img_path)
            print('No Face Found')
            return 'No Face Found'
        print("Aligned image has shape: {}".format(aligned_image.size))
        return aligned_image

    aligned_image = run_alignment(downloaded_img_path)  # Input URL
    if isinstance(aligned_image, str) and aligned_image == 'No Face Found':
        return {'error': 405}
    # aligned_image = run_alignment(image_path) # Input Path
    aligned_image.resize((256, 256))
    img_transforms = EXPERIMENT_ARGS['transform']
    input_image = img_transforms(aligned_image)

    # Image Generation
    def run_on_batch(inputs, net):
        result_batch = net(inputs.to("cuda").float(),
                           randomize_noise=False, resize=False)
        return result_batch

    # we'll run the image on multiple target ages
    target_ages = [i for i in range(arg3, arg4 + 1)]
    age_transformers = [AgeTransformer(target_age=age) for age in target_ages]

    # for each age transformed age, we'll concatenate the results to display them side-by-side
    # results = np.array(aligned_image.resize((1024, 1024)))
    # count = 0
    # result_images = []

    
    video_name = f"{os.getcwd()}/src/output_video/generated_output_{uuid1}.mp4"
    fps = 6  # You can adjust the frame rate as needed.
    frame_size = (1024, 1024)  # Set the width and height of the frames.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_name, fourcc, fps, frame_size)

    for age_transformer in age_transformers:
        print(f"Running on target age: {age_transformer.target_age}")
        with torch.no_grad():
            input_image_age = [age_transformer(input_image.cpu()).to('cuda')]
            input_image_age = torch.stack(input_image_age)
            result_tensor = run_on_batch(input_image_age, net)[0]
            result_image = tensor2im(result_tensor)
            # results = np.concatenate([results, result_image], axis=1)

            # result_images.append(np.array(result_image))  # List of Image Array

            # result_image = Image.fromarray(np.array(result_image))
            # result_image.save(f"{arg2}/{count}.jpg") # save image at full resolution

            # image = cv2.imdecode(np.array(result_image), flags=cv2.IMREAD_COLOR)
            # result_image_rgb = cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB)
            out.write(cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB))
            # count += 1

    out.release()
    cv2.destroyAllWindows()

    # s3_vid_name = f"{arg1.split('.')[0].split('/')[-1]}.mp4"

    # mp4 to h264 conversion
    input_file = video_name  # Replace with the path to your input MP4 file
    # Output h264 path
    output_file = f'{os.getcwd()}/src/output_video/output_{uuid1}.mp4'
    command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264',
               output_file]  # Run FFmpeg command using subprocess
    subprocess.call(command)

    # UUID generation
    # uuid1 = uuid.uuid1()
    s3_vid_name = f'{uuid1}.mp4'

    # upload to s3
    res_url = upload_image_to_s3('AKIAVZBVXJWJLAWNRCWZ', 'SzjAgZQBhe7oPaQfqNgkWAe34aAHnBrd9CD1Kbjx',
                                 'ap-southeast-1', 'effy-bandhan', s3_vid_name, output_file)

    os.unlink(downloaded_img_path)
    os.unlink(video_name)
    os.unlink(output_file)

    print(f'Total time taken: {time.time() - start_time}')

    return {'s3_output': res_url}
