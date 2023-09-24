from argparse import Namespace
import os
import sys
import pprint
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
sys.path.append(".")
sys.path.append("..")
from datasets.augmentations import AgeTransformer
from utils.common import tensor2im
from models.psp import pSp

# Video Conversion
import cv2

# Argument Input
import sys
if len(sys.argv) != 5:
    print(f'current len of agruments: {len(sys.argv)}')
    print("Usage: python script.py Input_path Output_Dir Current_Age Require_Age")
    sys.exit(1)
arg1 = sys.argv[1] # Input Path
arg2 = sys.argv[2] # Output Dir
arg3 = int(sys.argv[3]) # Current Age
arg4 = int(sys.argv[4]) # Required Age
# arg1 = 'input/001.jpg'
# arg2 = 'output'
# arg3 = '25'
# arg4 = '80'


# Model Config Files
EXPERIMENT_TYPE = 'ffhq_aging'
EXPERIMENT_DATA_ARGS = {
    "ffhq_aging": {
        "model_path": "pretrained_models/sam_ffhq_aging.pt",
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
    print('Download pretained model and save it in "pretained_models" dir or if already downloaded then save the model path correctly')

ckpt = torch.load(model_path, map_location='cpu')
opts = ckpt['opts']
pprint.pprint(opts)

opts['checkpoint_path'] = model_path
opts = Namespace(**opts)
net = pSp(opts)
net.eval()
net.cuda()
print('Model successfully loaded!')

# Input Image
image_path = arg1
original_image = Image.open(image_path).convert("RGB")
original_image.resize((256, 256))

def run_alignment(image_path):
    import dlib
    from scripts.align_all_parallel import align_face
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    aligned_image = align_face(filepath=image_path, predictor=predictor)
    print("Aligned image has shape: {}".format(aligned_image.size))
    return aligned_image

aligned_image = run_alignment(image_path)
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
video_name = f"{os.getcwd()}/output_video/{arg1.split('.')[0].split('/')[1]}.mp4"
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

# results = Image.fromarray(results)
# results   # this is a very large image (11*1024 x 1024) so it may take some time to display!

# # save image at full resolution
# results.save(f"{arg2}/age_transformed_image.jpg")


## AGR3

# target_age = arg3
# age_transformer = AgeTransformer(target_age=target_age)

# with torch.no_grad():
#     input_image_age = [age_transformer(input_image.cpu()).to('cuda')]
#     input_image_age = torch.stack(input_image_age)
#     result_tensor = run_on_batch(input_image_age, net)[0]
#     result_image = tensor2im(result_tensor)

# results = np.array(aligned_image.resize((1024, 1024)))
# results = np.concatenate([results, result_image], axis=1)
# results = Image.fromarray(results)

# # Save image at full resolution
# results.save(f"{arg2}/age_transformed_image.jpg")
# print('Saved...')