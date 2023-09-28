import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# import os
# from PIL import Image
# import requests
# from io import BytesIO

# !pip install mediapipe
# !wget -O face_landmarker_v2_with_blendshapes.task -q https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task
# !wget -q -O image.png https://storage.googleapis.com/mediapipe-assets/business-person.png
# img = cv2.imread("image.png")
# cv2_imshow(img)

mp_left_eye = [33, 160, 158, 133, 153, 163]
mp_right_eye = [362, 385, 387, 263, 373, 380]
mp_outer_mouth = [185, 40,  37, 0, 267, 270, 291, 321, 314, 17, 84, 91]

# input_url = 'https://img.freepik.com/premium-photo/amazing-scenic-view-sea-bay-mountain-islands-palawan-philippines_328046-19574.jpg'  # Input Image
# try:
#     response = requests.get(input_url)
# except:
#     print('Invalid URL Response')

# if response.status_code == 200:
#     # Open the image using PIL (Python Imaging Library)
#     img = Image.open(BytesIO(response.content)).convert("RGB")
#     print(f"Image Shape: {img.size[0]}x{img.size[1]} pixels")
#     # Save the image locally
#     img.save('downloaded_image.jpg')
#     print("Image downloaded and saved as 'downloaded_image.jpg'")
#     print('Image Size: ', os.path.getsize('downloaded_image.jpg'))
# else:
#     print("Failed to download the image. Status code:", response.status_code)


def get_landmarks(image_path):
    print('starting landmarks generation')
    # STEP 1: Import the necessary modules.

    # STEP 2: Create an FaceLandmarker object.
    base_options = python.BaseOptions(model_asset_path='/home/ubuntu/development/effyaiweb/app/src/scripts/face_landmarker_v2_with_blendshapes.task')
    options = vision.FaceLandmarkerOptions(base_options=base_options,
                                        output_face_blendshapes=True,
                                        output_facial_transformation_matrixes=True,
                                        num_faces=1)
    detector = vision.FaceLandmarker.create_from_options(options)

    # STEP 3: Load the input image.
    image = mp.Image.create_from_file(image_path)
    width = image.width
    height = image.height
    
    # STEP 4: Detect face landmarks from the input image.
    detection_result = detector.detect(image)

    face_landmarks_list = detection_result.face_landmarks

    if face_landmarks_list == []:
        return 'No Face Found'

    left_eye = []
    for i in mp_left_eye:
        left_eye.append([int(width*face_landmarks_list[0][i].x), int(height*face_landmarks_list[0][i].y)])
    right_eye = []
    for i in mp_right_eye:
        right_eye.append([int(width*face_landmarks_list[0][i].x), int(height*face_landmarks_list[0][i].y)])
    outer_mouth = []
    for i in mp_outer_mouth:
        outer_mouth.append([int(width*face_landmarks_list[0][i].x), int(height*face_landmarks_list[0][i].y)])
    # print(left_eye, right_eye, outer_mouth)
    return (left_eye), right_eye, outer_mouth
# print(get_landmarks('downloaded_image.jpg', 418, 626))



# temp = [[175.5268952846527, 262.87042212486267], [180.84337723255157, 270.8324261903763], [193.70763063430786, 290.0980305671692], [199.20656323432922, 298.33327412605286], [190.72671884298325, 285.6337942481041], [179.5322389602661, 268.8688554763794]], 
# [[226.96083784103394, 339.8982882499695], [232.36820876598358, 347.9964083433151], [245.38850319385529, 367.49570095539093], [251.3864780664444, 376.47831404209137], [244.34811341762543, 365.9376052618027], [231.4299694299698, 346.5912939310074]], 
# [6, 40, 37, 0, 267, 270, 291, 321, 314, 17, 84, 91]



# temp1 = [[261 162]
#  [272 156]
#  [284 156]
#  [296 163]
#  [284 165]
#  [271 165]], [[342 161]
#  [353 153]
#  [365 153]
#  [376 158]
#  [366 161]
#  [355 162]], [[279 236]
#  [293 232]
#  [309 230]
#  [322 233]
#  [335 229]
#  [352 230]
#  [370 233]
#  [354 255]
#  [336 266]
#  [323 268]
#  [309 267]
#  [293 257]]