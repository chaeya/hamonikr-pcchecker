#!/usr/bin/env python3
import os
import subprocess

def notify(title="Info", message="Hello World!"):
    if os.getenv('SUDO_USER') is None:
        subprocess.run(['notify-send', '-i', 'gtk-dialog-warning', title, message],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True)                
    else:
        userID = subprocess.run(['id', '-u', os.environ['SUDO_USER']],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                check=True).stdout.decode("utf-8").replace('\n', '')

        subprocess.run(['sudo', '-u', os.environ['SUDO_USER'], 'DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/{}/bus'.format(userID), 
                        'notify-send', '-i', 'gtk-dialog-warning', title, message],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True)        


notify('Info', '테스트용 알림 메세지')
print('Hello...')
