#!/usr/bin/env python3
import logging
import logging.handlers
import subprocess
import sys
import importlib.util
import datetime

logfile = '/tmp/pcchecker.log'
logger = logging.getLogger("crumbs")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
fileHandler = logging.FileHandler(logfile)
streamHandler = logging.StreamHandler()
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.debug('Program Running...')

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
# print(installed_packages) //DEBUG

# if 'notify2' in installed_packages:
if (importlib.util.find_spec('notify2')) is None:
    print('notify2 is not installed')
    install_and_import('notify2')

def show_notify():
    try:
        import os        
        import notify2

        if not 'DISPLAY' in os.environ:
            os.environ['DISPLAY'] = ':0'        

        notify2.init('PC Checker')
        title = 'PC Checker'
        body = '메세지 테스트 입니다.\r\nPC 점검결과 이상이 없습니다.\r\n\r\nhttps://hamonikr.org'        
        iconfile = '/home/hamonikr/workspaces/hamonikr-pcchecker/debian/usr/share/icons/hicolor/256x256/apps/pcchecker.png'
        notify = notify2.Notification(title, body, iconfile)
        notify.show()

    except Exception:
        return

show_notify()