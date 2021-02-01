#  import os
import configparser
import subprocess as sub
from sys import platform, path
#  path.append(os.getcwd())

#  import Custom_threading as ct
from threading import Thread
from typing import Any
import distro  # for figuring out what linux distro

OS = distro.linux_distribution()[0]

config = configparser.ConfigParser()
config.read('config.ini')

"""def resource_path(relative_path):
    
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)"""


def NewThread(com, Returning: bool, thread_ID, *arguments) -> Any:
    """
    Will create a new thread for a function/command.

    :param com: Command to be Executed
    :param Returning: True/False Will the command return anything?
    :param thread_ID: Name of thread
    :param arguments: Arguments to be sent to Command

    """
    
    class NewThreadWorker(Thread):
        def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *,
                     daemon=None):
            Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
            self.daemon = True
            self._return = None
        
        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        
        def joinThread(self):
            Thread.join(self)
            return self._return
    
    ntw = NewThreadWorker(target=com, name=thread_ID, args=(*arguments,))
    if Returning:
        ntw.start()
        return ntw.joinThread()
    else:
        ntw.start()


def malRem():
    def malrem():
        if platform == 'linux':
            if OS == 'Manjaro Linux':
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
    ct.NewThread(malrem, False, "Malware Removal")


def alyn():
    # Check to see if lynis is installed first, 
    # if yes : skip install, if no : install
    if OS in ('Ubuntu', 'debian'):
        command = 'sudo apt install lynis -y'
        sub.Popen(command.split())
        command = 'touch auditRESULTS.txt'
        sub.Popen(command.split())
        command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
        sub.Popen(command2.split())
    elif OS == 'darwin':
        print('This function does not currently support this OS')
    elif OS == 'Manjaro Linux':
        command = 'sudo pacman -S lynis --noconfirm'
        sub.Popen(command.split())
        command = 'sudo touch auditRESULTS.txt'
        sub.Popen(command.split())
        command2 = 'sudo lynis audit system | tee auditRESULTS.txt'
        sub.Popen(command2.split())




