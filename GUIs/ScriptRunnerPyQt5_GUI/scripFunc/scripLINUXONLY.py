import configparser
import os
import subprocess as sub
from sys import platform

import distro  # for figuring out what linux distro

OS = distro.linux_distribution()
ops = OS[0]

config = configparser.ConfigParser()
config.read('config.ini')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


'''
This file is used to store commands that are to only be used on Linux machines
'''


class funcLINUX:
    def malRem(self):
        if platform == 'linux':
            if ops == 'Manjaro Linux':
                command = 'sudo pacman -S clamav -y'
                sub.Popen(command.split())
            else:
                command = 'sudo apt install clamav -y'
                sub.Popen(command.split())
            command = ['sudo freshclam', 'sudo touch CLAMresults.txt',
                       'sudo clamscan -r --remove / | tee CLAMresults.txt']
            for i in range(0, 3):
                sub.Popen(command[i].split())
        else:
            print('This command is currently in development')

    def alyn(self):
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt install lynis -y'
            sub.Popen(command.split())
            command = 'sudo touch auditRESULTS.txt'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
            sub.Popen(command2.split())
        elif ops == 'darwin':
            print('This function does not currently support this OS')
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S lynis --noconfirm'
            sub.Popen(command.split())
            command = 'sudo touch auditRESULTS.txt'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
            sub.Popen(command2.split())
        elif platform == 'win32':
            print('This function does not currently support this OS.')
