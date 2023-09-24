# EffyAI Backend

Introduction
EffyAI is a machine learning-powered application designed for video and audio analysis. 
This backend component is built using the Flask framework in Python and serves as the core of the EffyAI system.
om.

Follow these Steps

``````
python3 -m venv effyenv
source effyenv/bin/activate
``````
``````
pip install -r requirements.txt
``````
``````
Download pretrained model (sam_ffhq_aging.pt) and save it to 'src/pretrained_models' directory
(a) Thourgh Command: gdown 1XyumF6_fdAxFmxpFcmPf-q84LU_22EMC
(b) Through Link: https://drive.google.com/file/d/1XyumF6_fdAxFmxpFcmPf-q84LU_22EMC/view
``````
``````
Terminal: python3 src/run.py Input_path(str) Output_Dir(str) Current_Age(int) Require_Age(int)
``````