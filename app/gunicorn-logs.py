import logging
# Log file location
logfile = "/home/ubuntu/development/effyaiweb/app/gunicorn-logs.py"
# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
loglevel = logging.INFO
# Log format (optional)
logformat = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"[2023-09-28 14:20:08 +0000] [34792] [INFO] Starting gunicorn 21.2.0
[2023-09-28 14:20:08 +0000] [34792] [INFO] Listening at: http://0.0.0.0:8000 (34792)
[2023-09-28 14:20:08 +0000] [34792] [INFO] Using worker: sync
[2023-09-28 14:20:08 +0000] [34793] [INFO] Booting worker with pid: 34793
[2023-09-28 14:21:17 +0000] [34792] [INFO] Handling signal: winch
[2023-09-28 14:22:39 +0000] [34792] [INFO] Handling signal: hup
[2023-09-28 14:22:39 +0000] [34792] [INFO] Hang up: Master
[2023-09-28 14:22:39 +0000] [35329] [INFO] Booting worker with pid: 35329
[2023-09-28 14:22:39 +0000] [34792] [ERROR] Worker (pid:34793) was sent SIGHUP!
[2023-09-28 14:22:42 +0000] [35329] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:42 +0000] [35329] [INFO] Worker exiting (pid: 35329)
[2023-09-28 14:22:42 +0000] [34792] [ERROR] Worker (pid:35329) exited with code 120
[2023-09-28 14:22:42 +0000] [34792] [ERROR] Worker (pid:35329) exited with code 120.
[2023-09-28 14:22:42 +0000] [35388] [INFO] Booting worker with pid: 35388
[2023-09-28 14:22:45 +0000] [35388] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:45 +0000] [35388] [INFO] Worker exiting (pid: 35388)
[2023-09-28 14:22:46 +0000] [34792] [ERROR] Worker (pid:35388) exited with code 120
[2023-09-28 14:22:46 +0000] [34792] [ERROR] Worker (pid:35388) exited with code 120.
[2023-09-28 14:22:46 +0000] [35448] [INFO] Booting worker with pid: 35448
[2023-09-28 14:22:49 +0000] [35448] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:49 +0000] [35448] [INFO] Worker exiting (pid: 35448)
[2023-09-28 14:22:49 +0000] [34792] [ERROR] Worker (pid:35448) exited with code 120
[2023-09-28 14:22:49 +0000] [34792] [ERROR] Worker (pid:35448) exited with code 120.
[2023-09-28 14:22:49 +0000] [35507] [INFO] Booting worker with pid: 35507
[2023-09-28 14:22:52 +0000] [35507] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:52 +0000] [35507] [INFO] Worker exiting (pid: 35507)
[2023-09-28 14:22:53 +0000] [34792] [ERROR] Worker (pid:35507) exited with code 120
[2023-09-28 14:22:53 +0000] [34792] [ERROR] Worker (pid:35507) exited with code 120.
[2023-09-28 14:22:53 +0000] [35566] [INFO] Booting worker with pid: 35566
[2023-09-28 14:22:56 +0000] [35566] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:56 +0000] [35566] [INFO] Worker exiting (pid: 35566)
[2023-09-28 14:22:56 +0000] [34792] [ERROR] Worker (pid:35566) exited with code 120
[2023-09-28 14:22:56 +0000] [34792] [ERROR] Worker (pid:35566) exited with code 120.
[2023-09-28 14:22:56 +0000] [35625] [INFO] Booting worker with pid: 35625
[2023-09-28 14:22:59 +0000] [35625] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:22:59 +0000] [35625] [INFO] Worker exiting (pid: 35625)
[2023-09-28 14:23:00 +0000] [34792] [ERROR] Worker (pid:35625) exited with code 120
[2023-09-28 14:23:00 +0000] [34792] [ERROR] Worker (pid:35625) exited with code 120.
[2023-09-28 14:23:00 +0000] [35684] [INFO] Booting worker with pid: 35684
[2023-09-28 14:23:03 +0000] [35684] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:03 +0000] [35684] [INFO] Worker exiting (pid: 35684)
[2023-09-28 14:23:03 +0000] [34792] [ERROR] Worker (pid:35684) exited with code 120
[2023-09-28 14:23:03 +0000] [34792] [ERROR] Worker (pid:35684) exited with code 120.
[2023-09-28 14:23:03 +0000] [35745] [INFO] Booting worker with pid: 35745
[2023-09-28 14:23:06 +0000] [35745] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:06 +0000] [35745] [INFO] Worker exiting (pid: 35745)
[2023-09-28 14:23:07 +0000] [34792] [ERROR] Worker (pid:35745) exited with code 120
[2023-09-28 14:23:07 +0000] [34792] [ERROR] Worker (pid:35745) exited with code 120.
[2023-09-28 14:23:07 +0000] [35934] [INFO] Booting worker with pid: 35934
[2023-09-28 14:23:10 +0000] [35934] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:10 +0000] [35934] [INFO] Worker exiting (pid: 35934)
[2023-09-28 14:23:11 +0000] [34792] [ERROR] Worker (pid:35934) exited with code 120
[2023-09-28 14:23:11 +0000] [34792] [ERROR] Worker (pid:35934) exited with code 120.
[2023-09-28 14:23:11 +0000] [36027] [INFO] Booting worker with pid: 36027
[2023-09-28 14:23:14 +0000] [36027] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:14 +0000] [36027] [INFO] Worker exiting (pid: 36027)
[2023-09-28 14:23:14 +0000] [34792] [ERROR] Worker (pid:36027) exited with code 120
[2023-09-28 14:23:14 +0000] [34792] [ERROR] Worker (pid:36027) exited with code 120.
[2023-09-28 14:23:14 +0000] [36087] [INFO] Booting worker with pid: 36087
[2023-09-28 14:23:17 +0000] [36087] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:17 +0000] [36087] [INFO] Worker exiting (pid: 36087)
[2023-09-28 14:23:18 +0000] [34792] [ERROR] Worker (pid:36087) exited with code 120
[2023-09-28 14:23:18 +0000] [34792] [ERROR] Worker (pid:36087) exited with code 120.
[2023-09-28 14:23:18 +0000] [36148] [INFO] Booting worker with pid: 36148
[2023-09-28 14:23:20 +0000] [36148] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:20 +0000] [36148] [INFO] Worker exiting (pid: 36148)
[2023-09-28 14:23:21 +0000] [34792] [ERROR] Worker (pid:36148) exited with code 120
[2023-09-28 14:23:21 +0000] [34792] [ERROR] Worker (pid:36148) exited with code 120.
[2023-09-28 14:23:21 +0000] [36333] [INFO] Booting worker with pid: 36333
[2023-09-28 14:23:24 +0000] [36333] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:24 +0000] [36333] [INFO] Worker exiting (pid: 36333)
[2023-09-28 14:23:25 +0000] [34792] [ERROR] Worker (pid:36333) exited with code 120
[2023-09-28 14:23:25 +0000] [34792] [ERROR] Worker (pid:36333) exited with code 120.
[2023-09-28 14:23:25 +0000] [36423] [INFO] Booting worker with pid: 36423
[2023-09-28 14:23:28 +0000] [36423] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:28 +0000] [36423] [INFO] Worker exiting (pid: 36423)
[2023-09-28 14:23:28 +0000] [34792] [ERROR] Worker (pid:36423) exited with code 120
[2023-09-28 14:23:28 +0000] [34792] [ERROR] Worker (pid:36423) exited with code 120.
[2023-09-28 14:23:28 +0000] [36482] [INFO] Booting worker with pid: 36482
[2023-09-28 14:23:31 +0000] [36482] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:31 +0000] [36482] [INFO] Worker exiting (pid: 36482)
[2023-09-28 14:23:32 +0000] [34792] [ERROR] Worker (pid:36482) exited with code 120
[2023-09-28 14:23:32 +0000] [34792] [ERROR] Worker (pid:36482) exited with code 120.
[2023-09-28 14:23:32 +0000] [36558] [INFO] Booting worker with pid: 36558
[2023-09-28 14:23:35 +0000] [36558] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:35 +0000] [36558] [INFO] Worker exiting (pid: 36558)
[2023-09-28 14:23:35 +0000] [34792] [ERROR] Worker (pid:36558) exited with code 120
[2023-09-28 14:23:35 +0000] [34792] [ERROR] Worker (pid:36558) exited with code 120.
[2023-09-28 14:23:35 +0000] [36636] [INFO] Booting worker with pid: 36636
[2023-09-28 14:23:38 +0000] [36636] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:38 +0000] [36636] [INFO] Worker exiting (pid: 36636)
[2023-09-28 14:23:39 +0000] [34792] [ERROR] Worker (pid:36636) exited with code 120
[2023-09-28 14:23:39 +0000] [34792] [ERROR] Worker (pid:36636) exited with code 120.
[2023-09-28 14:23:39 +0000] [36753] [INFO] Booting worker with pid: 36753
[2023-09-28 14:23:42 +0000] [36753] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:42 +0000] [36753] [INFO] Worker exiting (pid: 36753)
[2023-09-28 14:23:42 +0000] [34792] [ERROR] Worker (pid:36753) exited with code 120
[2023-09-28 14:23:42 +0000] [34792] [ERROR] Worker (pid:36753) exited with code 120.
[2023-09-28 14:23:42 +0000] [36816] [INFO] Booting worker with pid: 36816
[2023-09-28 14:23:45 +0000] [36816] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:45 +0000] [36816] [INFO] Worker exiting (pid: 36816)
[2023-09-28 14:23:46 +0000] [34792] [ERROR] Worker (pid:36816) exited with code 120
[2023-09-28 14:23:46 +0000] [34792] [ERROR] Worker (pid:36816) exited with code 120.
[2023-09-28 14:23:46 +0000] [36899] [INFO] Booting worker with pid: 36899
[2023-09-28 14:23:49 +0000] [36899] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:49 +0000] [36899] [INFO] Worker exiting (pid: 36899)
[2023-09-28 14:23:49 +0000] [34792] [ERROR] Worker (pid:36899) exited with code 120
[2023-09-28 14:23:49 +0000] [34792] [ERROR] Worker (pid:36899) exited with code 120.
[2023-09-28 14:23:49 +0000] [36995] [INFO] Booting worker with pid: 36995
[2023-09-28 14:23:52 +0000] [36995] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:52 +0000] [36995] [INFO] Worker exiting (pid: 36995)
[2023-09-28 14:23:53 +0000] [34792] [ERROR] Worker (pid:36995) exited with code 120
[2023-09-28 14:23:53 +0000] [34792] [ERROR] Worker (pid:36995) exited with code 120.
[2023-09-28 14:23:53 +0000] [37071] [INFO] Booting worker with pid: 37071
[2023-09-28 14:23:56 +0000] [37071] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:56 +0000] [37071] [INFO] Worker exiting (pid: 37071)
[2023-09-28 14:23:56 +0000] [34792] [ERROR] Worker (pid:37071) exited with code 120
[2023-09-28 14:23:56 +0000] [34792] [ERROR] Worker (pid:37071) exited with code 120.
[2023-09-28 14:23:56 +0000] [37133] [INFO] Booting worker with pid: 37133
[2023-09-28 14:23:59 +0000] [37133] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:23:59 +0000] [37133] [INFO] Worker exiting (pid: 37133)
[2023-09-28 14:24:00 +0000] [34792] [ERROR] Worker (pid:37133) exited with code 120
[2023-09-28 14:24:00 +0000] [34792] [ERROR] Worker (pid:37133) exited with code 120.
[2023-09-28 14:24:00 +0000] [37208] [INFO] Booting worker with pid: 37208
[2023-09-28 14:24:03 +0000] [37208] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:03 +0000] [37208] [INFO] Worker exiting (pid: 37208)
[2023-09-28 14:24:03 +0000] [34792] [ERROR] Worker (pid:37208) exited with code 120
[2023-09-28 14:24:03 +0000] [34792] [ERROR] Worker (pid:37208) exited with code 120.
[2023-09-28 14:24:03 +0000] [37270] [INFO] Booting worker with pid: 37270
[2023-09-28 14:24:06 +0000] [37270] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:06 +0000] [37270] [INFO] Worker exiting (pid: 37270)
[2023-09-28 14:24:07 +0000] [34792] [ERROR] Worker (pid:37270) exited with code 120
[2023-09-28 14:24:07 +0000] [34792] [ERROR] Worker (pid:37270) exited with code 120.
[2023-09-28 14:24:07 +0000] [37348] [INFO] Booting worker with pid: 37348
[2023-09-28 14:24:10 +0000] [37348] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:10 +0000] [37348] [INFO] Worker exiting (pid: 37348)
[2023-09-28 14:24:10 +0000] [34792] [ERROR] Worker (pid:37348) exited with code 120
[2023-09-28 14:24:10 +0000] [34792] [ERROR] Worker (pid:37348) exited with code 120.
[2023-09-28 14:24:10 +0000] [37410] [INFO] Booting worker with pid: 37410
[2023-09-28 14:24:13 +0000] [37410] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:13 +0000] [37410] [INFO] Worker exiting (pid: 37410)
[2023-09-28 14:24:14 +0000] [34792] [ERROR] Worker (pid:37410) exited with code 120
[2023-09-28 14:24:14 +0000] [34792] [ERROR] Worker (pid:37410) exited with code 120.
[2023-09-28 14:24:14 +0000] [37469] [INFO] Booting worker with pid: 37469
[2023-09-28 14:24:17 +0000] [37469] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:17 +0000] [37469] [INFO] Worker exiting (pid: 37469)
[2023-09-28 14:24:17 +0000] [34792] [ERROR] Worker (pid:37469) exited with code 120
[2023-09-28 14:24:17 +0000] [34792] [ERROR] Worker (pid:37469) exited with code 120.
[2023-09-28 14:24:17 +0000] [37531] [INFO] Booting worker with pid: 37531
[2023-09-28 14:24:20 +0000] [37531] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:20 +0000] [37531] [INFO] Worker exiting (pid: 37531)
[2023-09-28 14:24:21 +0000] [34792] [ERROR] Worker (pid:37531) exited with code 120
[2023-09-28 14:24:21 +0000] [34792] [ERROR] Worker (pid:37531) exited with code 120.
[2023-09-28 14:24:21 +0000] [37606] [INFO] Booting worker with pid: 37606
[2023-09-28 14:24:24 +0000] [37606] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:24 +0000] [37606] [INFO] Worker exiting (pid: 37606)
[2023-09-28 14:24:25 +0000] [34792] [ERROR] Worker (pid:37606) exited with code 120
[2023-09-28 14:24:25 +0000] [34792] [ERROR] Worker (pid:37606) exited with code 120.
[2023-09-28 14:24:25 +0000] [37689] [INFO] Booting worker with pid: 37689
[2023-09-28 14:24:28 +0000] [37689] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:28 +0000] [37689] [INFO] Worker exiting (pid: 37689)
[2023-09-28 14:24:28 +0000] [34792] [ERROR] Worker (pid:37689) exited with code 120
[2023-09-28 14:24:28 +0000] [34792] [ERROR] Worker (pid:37689) exited with code 120.
[2023-09-28 14:24:28 +0000] [37760] [INFO] Booting worker with pid: 37760
[2023-09-28 14:24:31 +0000] [37760] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:31 +0000] [37760] [INFO] Worker exiting (pid: 37760)
[2023-09-28 14:24:32 +0000] [34792] [ERROR] Worker (pid:37760) exited with code 120
[2023-09-28 14:24:32 +0000] [34792] [ERROR] Worker (pid:37760) exited with code 120.
[2023-09-28 14:24:32 +0000] [37822] [INFO] Booting worker with pid: 37822
[2023-09-28 14:24:35 +0000] [37822] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:35 +0000] [37822] [INFO] Worker exiting (pid: 37822)
[2023-09-28 14:24:35 +0000] [34792] [ERROR] Worker (pid:37822) exited with code 120
[2023-09-28 14:24:35 +0000] [34792] [ERROR] Worker (pid:37822) exited with code 120.
[2023-09-28 14:24:35 +0000] [37881] [INFO] Booting worker with pid: 37881
[2023-09-28 14:24:38 +0000] [37881] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:38 +0000] [37881] [INFO] Worker exiting (pid: 37881)
[2023-09-28 14:24:39 +0000] [34792] [ERROR] Worker (pid:37881) exited with code 120
[2023-09-28 14:24:39 +0000] [34792] [ERROR] Worker (pid:37881) exited with code 120.
[2023-09-28 14:24:39 +0000] [37943] [INFO] Booting worker with pid: 37943
[2023-09-28 14:24:42 +0000] [37943] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:42 +0000] [37943] [INFO] Worker exiting (pid: 37943)
[2023-09-28 14:24:42 +0000] [34792] [ERROR] Worker (pid:37943) exited with code 120
[2023-09-28 14:24:42 +0000] [34792] [ERROR] Worker (pid:37943) exited with code 120.
[2023-09-28 14:24:42 +0000] [38013] [INFO] Booting worker with pid: 38013
[2023-09-28 14:24:45 +0000] [38013] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:45 +0000] [38013] [INFO] Worker exiting (pid: 38013)
[2023-09-28 14:24:46 +0000] [34792] [ERROR] Worker (pid:38013) exited with code 120
[2023-09-28 14:24:46 +0000] [34792] [ERROR] Worker (pid:38013) exited with code 120.
[2023-09-28 14:24:46 +0000] [38078] [INFO] Booting worker with pid: 38078
[2023-09-28 14:24:49 +0000] [38078] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:49 +0000] [38078] [INFO] Worker exiting (pid: 38078)
[2023-09-28 14:24:49 +0000] [34792] [ERROR] Worker (pid:38078) exited with code 120
[2023-09-28 14:24:49 +0000] [34792] [ERROR] Worker (pid:38078) exited with code 120.
[2023-09-28 14:24:49 +0000] [38162] [INFO] Booting worker with pid: 38162
[2023-09-28 14:24:52 +0000] [38162] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:52 +0000] [38162] [INFO] Worker exiting (pid: 38162)
[2023-09-28 14:24:53 +0000] [34792] [ERROR] Worker (pid:38162) exited with code 120
[2023-09-28 14:24:53 +0000] [34792] [ERROR] Worker (pid:38162) exited with code 120.
[2023-09-28 14:24:53 +0000] [38224] [INFO] Booting worker with pid: 38224
[2023-09-28 14:24:56 +0000] [38224] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:56 +0000] [38224] [INFO] Worker exiting (pid: 38224)
[2023-09-28 14:24:56 +0000] [34792] [ERROR] Worker (pid:38224) exited with code 120
[2023-09-28 14:24:56 +0000] [34792] [ERROR] Worker (pid:38224) exited with code 120.
[2023-09-28 14:24:56 +0000] [38307] [INFO] Booting worker with pid: 38307
[2023-09-28 14:24:59 +0000] [38307] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:24:59 +0000] [38307] [INFO] Worker exiting (pid: 38307)
[2023-09-28 14:25:00 +0000] [34792] [ERROR] Worker (pid:38307) exited with code 120
[2023-09-28 14:25:00 +0000] [34792] [ERROR] Worker (pid:38307) exited with code 120.
[2023-09-28 14:25:00 +0000] [38381] [INFO] Booting worker with pid: 38381
[2023-09-28 14:25:03 +0000] [38381] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:03 +0000] [38381] [INFO] Worker exiting (pid: 38381)
[2023-09-28 14:25:03 +0000] [34792] [ERROR] Worker (pid:38381) exited with code 120
[2023-09-28 14:25:03 +0000] [34792] [ERROR] Worker (pid:38381) exited with code 120.
[2023-09-28 14:25:03 +0000] [38443] [INFO] Booting worker with pid: 38443
[2023-09-28 14:25:05 +0000] [38477] [INFO] Starting gunicorn 21.2.0
[2023-09-28 14:25:05 +0000] [38477] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2023-09-28 14:25:05 +0000] [38477] [ERROR] Retrying in 1 second.
[2023-09-28 14:25:06 +0000] [38443] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:06 +0000] [38443] [INFO] Worker exiting (pid: 38443)
[2023-09-28 14:25:06 +0000] [38477] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2023-09-28 14:25:06 +0000] [38477] [ERROR] Retrying in 1 second.
[2023-09-28 14:25:07 +0000] [34792] [ERROR] Worker (pid:38443) exited with code 120
[2023-09-28 14:25:07 +0000] [34792] [ERROR] Worker (pid:38443) exited with code 120.
[2023-09-28 14:25:07 +0000] [38514] [INFO] Booting worker with pid: 38514
[2023-09-28 14:25:07 +0000] [38477] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2023-09-28 14:25:07 +0000] [38477] [ERROR] Retrying in 1 second.
[2023-09-28 14:25:08 +0000] [38477] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2023-09-28 14:25:08 +0000] [38477] [ERROR] Retrying in 1 second.
[2023-09-28 14:25:09 +0000] [38477] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2023-09-28 14:25:09 +0000] [38477] [ERROR] Retrying in 1 second.
[2023-09-28 14:25:10 +0000] [38514] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:10 +0000] [38514] [INFO] Worker exiting (pid: 38514)
[2023-09-28 14:25:10 +0000] [34792] [ERROR] Worker (pid:38514) exited with code 120
[2023-09-28 14:25:10 +0000] [34792] [ERROR] Worker (pid:38514) exited with code 120.
[2023-09-28 14:25:10 +0000] [38581] [INFO] Booting worker with pid: 38581
[2023-09-28 14:25:10 +0000] [38477] [ERROR] Can't connect to ('0.0.0.0', 8000)
[2023-09-28 14:25:13 +0000] [38581] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:13 +0000] [38581] [INFO] Worker exiting (pid: 38581)
[2023-09-28 14:25:14 +0000] [34792] [ERROR] Worker (pid:38581) exited with code 120
[2023-09-28 14:25:14 +0000] [34792] [ERROR] Worker (pid:38581) exited with code 120.
[2023-09-28 14:25:14 +0000] [38670] [INFO] Booting worker with pid: 38670
[2023-09-28 14:25:17 +0000] [38670] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:17 +0000] [38670] [INFO] Worker exiting (pid: 38670)
[2023-09-28 14:25:17 +0000] [34792] [ERROR] Worker (pid:38670) exited with code 120
[2023-09-28 14:25:17 +0000] [34792] [ERROR] Worker (pid:38670) exited with code 120.
[2023-09-28 14:25:17 +0000] [38741] [INFO] Booting worker with pid: 38741
[2023-09-28 14:25:20 +0000] [38741] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:20 +0000] [38741] [INFO] Worker exiting (pid: 38741)
[2023-09-28 14:25:21 +0000] [34792] [ERROR] Worker (pid:38741) exited with code 120
[2023-09-28 14:25:21 +0000] [34792] [ERROR] Worker (pid:38741) exited with code 120.
[2023-09-28 14:25:21 +0000] [38803] [INFO] Booting worker with pid: 38803
[2023-09-28 14:25:24 +0000] [38803] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:24 +0000] [38803] [INFO] Worker exiting (pid: 38803)
[2023-09-28 14:25:24 +0000] [34792] [ERROR] Worker (pid:38803) exited with code 120
[2023-09-28 14:25:24 +0000] [34792] [ERROR] Worker (pid:38803) exited with code 120.
[2023-09-28 14:25:24 +0000] [38865] [INFO] Booting worker with pid: 38865
[2023-09-28 14:25:27 +0000] [38865] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:27 +0000] [38865] [INFO] Worker exiting (pid: 38865)
[2023-09-28 14:25:28 +0000] [34792] [ERROR] Worker (pid:38865) exited with code 120
[2023-09-28 14:25:28 +0000] [34792] [ERROR] Worker (pid:38865) exited with code 120.
[2023-09-28 14:25:28 +0000] [38933] [INFO] Booting worker with pid: 38933
[2023-09-28 14:25:31 +0000] [38933] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:31 +0000] [38933] [INFO] Worker exiting (pid: 38933)
[2023-09-28 14:25:31 +0000] [34792] [ERROR] Worker (pid:38933) exited with code 120
[2023-09-28 14:25:31 +0000] [34792] [ERROR] Worker (pid:38933) exited with code 120.
[2023-09-28 14:25:31 +0000] [39011] [INFO] Booting worker with pid: 39011
[2023-09-28 14:25:34 +0000] [39011] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:34 +0000] [39011] [INFO] Worker exiting (pid: 39011)
[2023-09-28 14:25:35 +0000] [34792] [ERROR] Worker (pid:39011) exited with code 120
[2023-09-28 14:25:35 +0000] [34792] [ERROR] Worker (pid:39011) exited with code 120.
[2023-09-28 14:25:35 +0000] [39082] [INFO] Booting worker with pid: 39082
[2023-09-28 14:25:38 +0000] [39082] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:38 +0000] [39082] [INFO] Worker exiting (pid: 39082)
[2023-09-28 14:25:38 +0000] [34792] [ERROR] Worker (pid:39082) exited with code 120
[2023-09-28 14:25:38 +0000] [34792] [ERROR] Worker (pid:39082) exited with code 120.
[2023-09-28 14:25:38 +0000] [39144] [INFO] Booting worker with pid: 39144
[2023-09-28 14:25:41 +0000] [39144] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:41 +0000] [39144] [INFO] Worker exiting (pid: 39144)
[2023-09-28 14:25:42 +0000] [34792] [ERROR] Worker (pid:39144) exited with code 120
[2023-09-28 14:25:42 +0000] [34792] [ERROR] Worker (pid:39144) exited with code 120.
[2023-09-28 14:25:42 +0000] [39230] [INFO] Booting worker with pid: 39230
[2023-09-28 14:25:45 +0000] [39230] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:45 +0000] [39230] [INFO] Worker exiting (pid: 39230)
[2023-09-28 14:25:45 +0000] [34792] [ERROR] Worker (pid:39230) exited with code 120
[2023-09-28 14:25:45 +0000] [34792] [ERROR] Worker (pid:39230) exited with code 120.
[2023-09-28 14:25:45 +0000] [39301] [INFO] Booting worker with pid: 39301
[2023-09-28 14:25:48 +0000] [39301] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:48 +0000] [39301] [INFO] Worker exiting (pid: 39301)
[2023-09-28 14:25:49 +0000] [34792] [ERROR] Worker (pid:39301) exited with code 120
[2023-09-28 14:25:49 +0000] [34792] [ERROR] Worker (pid:39301) exited with code 120.
[2023-09-28 14:25:49 +0000] [39376] [INFO] Booting worker with pid: 39376
[2023-09-28 14:25:52 +0000] [39376] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:52 +0000] [39376] [INFO] Worker exiting (pid: 39376)
[2023-09-28 14:25:52 +0000] [34792] [ERROR] Worker (pid:39376) exited with code 120
[2023-09-28 14:25:52 +0000] [34792] [ERROR] Worker (pid:39376) exited with code 120.
[2023-09-28 14:25:52 +0000] [39435] [INFO] Booting worker with pid: 39435
[2023-09-28 14:25:55 +0000] [39435] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:55 +0000] [39435] [INFO] Worker exiting (pid: 39435)
[2023-09-28 14:25:56 +0000] [34792] [ERROR] Worker (pid:39435) exited with code 120
[2023-09-28 14:25:56 +0000] [34792] [ERROR] Worker (pid:39435) exited with code 120.
[2023-09-28 14:25:56 +0000] [39497] [INFO] Booting worker with pid: 39497
[2023-09-28 14:25:59 +0000] [39497] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:25:59 +0000] [39497] [INFO] Worker exiting (pid: 39497)
[2023-09-28 14:25:59 +0000] [34792] [ERROR] Worker (pid:39497) exited with code 120
[2023-09-28 14:25:59 +0000] [34792] [ERROR] Worker (pid:39497) exited with code 120.
[2023-09-28 14:25:59 +0000] [39559] [INFO] Booting worker with pid: 39559
[2023-09-28 14:26:02 +0000] [39559] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:26:02 +0000] [39559] [INFO] Worker exiting (pid: 39559)
[2023-09-28 14:26:03 +0000] [34792] [ERROR] Worker (pid:39559) exited with code 120
[2023-09-28 14:26:03 +0000] [34792] [ERROR] Worker (pid:39559) exited with code 120.
[2023-09-28 14:26:03 +0000] [39618] [INFO] Booting worker with pid: 39618
[2023-09-28 14:26:06 +0000] [39618] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:26:06 +0000] [39618] [INFO] Worker exiting (pid: 39618)
[2023-09-28 14:26:06 +0000] [34792] [ERROR] Worker (pid:39618) exited with code 120
[2023-09-28 14:26:06 +0000] [34792] [ERROR] Worker (pid:39618) exited with code 120.
[2023-09-28 14:26:06 +0000] [39693] [INFO] Booting worker with pid: 39693
[2023-09-28 14:26:09 +0000] [39693] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:26:09 +0000] [39693] [INFO] Worker exiting (pid: 39693)
[2023-09-28 14:26:10 +0000] [34792] [ERROR] Worker (pid:39693) exited with code 120
[2023-09-28 14:26:10 +0000] [34792] [ERROR] Worker (pid:39693) exited with code 120.
[2023-09-28 14:26:10 +0000] [39758] [INFO] Booting worker with pid: 39758
[2023-09-28 14:26:12 +0000] [34792] [INFO] Handling signal: term
[2023-09-28 14:26:13 +0000] [39758] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
  File "/home/ubuntu/development/effyaiweb/venv/lib/python3.10/site-packages/gunicorn/util.py", line 371, in import_app
    mod = importlib.import_module(module)
  File "/usr/local/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/ubuntu/development/effyaiweb/app/app.py", line 3, in <module>
    from src.get_aging_video import age_input
  File "/home/ubuntu/development/effyaiweb/app/src/get_aging_video.py", line 9, in <module>
    from .scripts.align_all_parallel import align_face
  File "/home/ubuntu/development/effyaiweb/app/src/scripts/align_all_parallel.py", line 22, in <module>
    print(os.getcwd())
OSError: [Errno 5] Input/output error
[2023-09-28 14:26:13 +0000] [39758] [INFO] Worker exiting (pid: 39758)
[2023-09-28 14:26:13 +0000] [34792] [ERROR] Worker (pid:39758) exited with code 120
[2023-09-28 14:26:13 +0000] [34792] [ERROR] Worker (pid:39758) exited with code 120.
[2023-09-28 14:26:13 +0000] [34792] [INFO] Shutting down: Master
