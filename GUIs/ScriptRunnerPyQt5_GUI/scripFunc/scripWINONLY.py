import os
import subprocess as sub
from sys import platform
import getpass
from threading import *
import distro  # for figuring out what linux distro
import configparser
import shutil
from PyQt5 import QtGui
from PyUIs.hashgen import Ui_hashGEN
from PyUIs.enblebit import Ui_bitlockerGUI
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
This file is used to store commands that are to only be used on Windows machines
'''


class funcWINONLY:
    def BITLOCKER(self):

        class bitRUN(QDialog, Ui_bitlockerGUI):
            def __init__(self, parent=None):
                super(bitRUN, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/pictures/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):

                def ENCRYPT(x):
                    command = """
$pass = ConvertTo-SecureString '""" + self.encrypPASS.text() + """' -AsPlainText -Force
Enable-BitLocker """ + x + """ -PasswordProtector $pass"""
                    print(command)
                    #sub.Popen(["powershell", "& {" + command + "}"])

                decryptSTATUS = []
                command = 'Get-BitLockerVolume'
                EXEC = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
                stdout, _ = EXEC.communicate()
                output = stdout.decode("utf-8")
                output2 = output.split('\n')
                i = 7
                while True:
                    try:
                        # print(output2[i])
                        output3 = output2[i].split()
                        # print(output3)
                        decryptSTATUS.append(output3[1])
                        decryptSTATUS.append(output3[3])
                        i = i + 1
                    except Exception as e:
                        # print('Controlled exit of loop: ' + str(e))
                        break
                print(decryptSTATUS)
                buttons = [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4,
                           self.radioButton_5, self.radioButton_6, self.radioButton_7]

                self.selectedDRIVE = ''

                def STATUSCHECK(i):
                    # print(i)
                    self.selectedDRIVE = i
                    # print('selected drive: ' + self.selectedDRIVE)
                    index = decryptSTATUS.index(i)
                    status = index + 1
                    if decryptSTATUS[status] == 'FullyDecrypted':
                        self.label_4.setText('FullyDecrypted')
                        self.label_4.setStyleSheet('Color: red')
                    else:
                        self.label_4.setText('Encrypted')
                        self.label_4.setStyleSheet('Color: green')

                driveLETTER = []

                def cancelbutton():
                    self.close()

                self.radioButton.toggled.connect(lambda: STATUSCHECK(driveLETTER[0]))
                self.radioButton_2.toggled.connect(lambda: STATUSCHECK(driveLETTER[1]))
                self.radioButton_3.toggled.connect(lambda: STATUSCHECK(driveLETTER[2]))
                self.radioButton_4.toggled.connect(lambda: STATUSCHECK(driveLETTER[3]))
                self.radioButton_5.toggled.connect(lambda: STATUSCHECK(driveLETTER[4]))
                self.radioButton_6.toggled.connect(lambda: STATUSCHECK(driveLETTER[5]))
                self.enblBIT.clicked.connect(lambda: threader(ENCRYPT(self.selectedDRIVE)))
                self.cancelbutton.clicked.connect(cancelbutton)

                i = 0
                x = 0
                while True:
                    try:
                        buttons[i].setText(decryptSTATUS[x])
                        # print('i: ' + str(i))
                        # print('x: ' + str(x))
                        # print(decryptSTATUS[x])
                        # print(len(decryptSTATUS))
                        driveLETTER.append(decryptSTATUS[x])
                        # print(driveLETTER[i])
                        x = x + 2
                        i = i + 1
                        if x == len(decryptSTATUS):
                            while i != len(buttons):
                                # print('if')
                                buttons[i].setText('<No Drive Found>')
                                buttons[i].setEnabled(False)
                                i = i + 1
                        else:
                            continue

                    except Exception as e:
                        # print('Controlled exit of loop: ' + str(e))
                        break

                ''' 
                command = """
                $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
                manage-bde -protectors -add -pw $drv
                manage-bde -on $drv"""
                '''

        def threader(com):
            try:
                threader = Thread(target=com)
                threader.start()
            except Exception as e:
                print(e)
                print('Could not start thread')

        def callBITRUN():
            widget = bitRUN()
            widget.exec_()

        callBITRUN()