# EffyAI Backend

Introduction
EffyAI is a machine learning-powered application designed for video and audio analysis. 
This backend component is built using the Flask framework in Python and serves as the core of the EffyAI system.
om.

## Follow these Steps

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

## Supervisor Setup Code
```
sudo apt-get install ninja-build
sudo apt-get update
sudo apt-get install supervisor
sudo nano /etc/supervisor/conf.d/effyaiweb.conf
```
```
[program:myapp]
command=/path/to/your/virtualenv/bin/gunicorn -w 3 -b 0.0.0.0:8000 your_app_module:app
directory=/path/to/your/app
user=your_username
autostart=true
autorestart=true
redirect_stderr=true
stderr_logfile=/var/log/hello_world/hello_world.err.log
stdout_logfile=/var/log/hello_world/hello_world.out.log
```
To Start/Update
```
sudo supervisorctl reread
sudo supervisorctl update
sudo service supervisor restart
sudo supervisorctl status
```
To Stop
```
sudo supervisorctl stop
```
or
```
sudo supervisorctl stop myproject_gunicorn
```