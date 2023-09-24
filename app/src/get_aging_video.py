from argparse import Namespace
import os
import sys
import pprint
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
import requests
from io import BytesIO
sys.path.append(".")
sys.path.append("..")
# sys.path.append('/home/ubuntu/effyaiweb/src')
from .datasets.augmentations import AgeTransformer
from .utils.common import tensor2im
from .models.psp import pSp
from .database import upload_image_to_s3

# Video Conversion
import cv2

def age_input(input1, input3, input4):
    # if len(sys.argv) != 5:
    #     print(f'current len of agruments: {len(sys.argv)}')
    #     print("Usage: python script.py Input_path Output_Dir Current_Age Require_Age")
    #     sys.exit(1)
    # arg1 = sys.argv[1] # Input Path
    # arg2 = sys.argv[2] # Output Dir
    # arg3 = int(sys.argv[3]) # Current Age
    # arg4 = int(sys.argv[4]) # Required Age

    arg1 = input1
    # arg2 = input2
    arg3 = input3
    arg4 = input4

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

    if not os.path.exists(model_path):
        print('Download pretained model and save it in "app/src/pretained_models" dir or if already downloaded then save the model path correctly')
        return 'null'

    ckpt = torch.load(model_path, map_location='cpu')
    opts = ckpt['opts']
    pprint.pprint(opts)

    opts['checkpoint_path'] = model_path
    opts = Namespace(**opts)
    net = pSp(opts)
    net.eval()
    net.cuda()
    print('Model successfully loaded!')

    # Download Image from URL
    input_url = arg1 # Input Image
    response = requests.get(input_url)
    if response.status_code == 200:
        # Open the image using PIL (Python Imaging Library)
        img = Image.open(BytesIO(response.content)).convert("RGB") 
        # Save the image locally
        img.save('/home/ubuntu/effyaiweb/app/src/input/downloaded_image.jpg')
        print("Image downloaded and saved as 'downloaded_image.jpg'")
    else:
        print("Failed to download the image. Status code:", response.status_code)

    original_image = Image.open('effyaiweb/app/src/input/downloaded_image.jpg').convert("RGB") # Input URL
    # image_path = arg1 # Input Path
    # original_image = Image.open(image_path).convert("RGB") # Input Path
    original_image.resize((256, 256))

    def run_alignment(image_path):
        import dlib
        from .scripts.align_all_parallel import align_face
        predictor = dlib.shape_predictor("effyaiweb/app/src/shape_predictor_68_face_landmarks.dat")
        aligned_image = align_face(filepath=image_path, predictor=predictor)
        print("Aligned image has shape: {}".format(aligned_image.size))
        return aligned_image

    aligned_image = run_alignment('effyaiweb/app/src/input/downloaded_image.jpg') # Input URL
    # aligned_image = run_alignment(image_path) # Input Path
    aligned_image.resize((256, 256))
    img_transforms = EXPERIMENT_ARGS['transform']
    input_image = img_transforms(aligned_image)

    # Image Generation
    def run_on_batch(inputs, net):
        result_batch = net(inputs.to("cuda").float(), randomize_noise=False, resize=False)
        return result_batch


    # we'll run the image on multiple target ages 
    target_ages = [i for i in range(arg3, arg4 + 1)]
    age_transformers = [AgeTransformer(target_age=age) for age in target_ages]

    # for each age transformed age, we'll concatenate the results to display them side-by-side
    results = np.array(aligned_image.resize((1024, 1024)))
    count = 0
    result_images = []

    # Video Options
    # image_folder = '/home/ubuntu/stylegan/sam_ready/SAM/output'
    # image_list = os.listdir(image_folder)
    video_name = f"{os.getcwd()}/effyaiweb/app/src/output_video/{arg1.split('.')[0].split('/')[-1]}.mp4"
    fps = 6  # You can adjust the frame rate as needed.
    frame_size = (1024, 1024)  # Set the width and height of the frames.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed.
    out = cv2.VideoWriter(video_name, fourcc, fps, frame_size)

    for age_transformer in age_transformers:
        print(f"Running on target age: {age_transformer.target_age}")
        with torch.no_grad():
            input_image_age = [age_transformer(input_image.cpu()).to('cuda')]
            input_image_age = torch.stack(input_image_age)
            result_tensor = run_on_batch(input_image_age, net)[0]
            result_image = tensor2im(result_tensor)
            results = np.concatenate([results, result_image], axis=1)

            result_images.append(np.array(result_image)) # List of Image Array

            result_image = Image.fromarray(np.array(result_image))
            # result_image.save(f"{arg2}/{count}.jpg") # save image at full resolution

            # image = cv2.imdecode(np.array(result_image), flags=cv2.IMREAD_COLOR)
            # result_image_rgb = cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB)
            out.write(cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB))
            count += 1

    out.release()
    cv2.destroyAllWindows()

    s3_vid_name = f"{arg1.split('.')[0].split('/')[-1]}.mp4"

    # upload to s3
    res_url = upload_image_to_s3('AKIAVZBVXJWJLAWNRCWZ', 'SzjAgZQBhe7oPaQfqNgkWAe34aAHnBrd9CD1Kbjx', 'us-east-1', 'effy-bandhan', s3_vid_name, video_name)

    os.unlink(video_name)

    return res_url