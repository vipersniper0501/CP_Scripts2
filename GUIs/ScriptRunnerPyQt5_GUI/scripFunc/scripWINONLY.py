import os
import subprocess as sub
from sys import platform
import getpass
import itertools
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
                self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):

                # Executes encryption command
                def ENCRYPT(drive):
                    l1 = self.encrypPASS.text()
                    # print(l1)
                    # print(len(l1))
                    l2 = self.encrypPASS_2.text()
                    # print(l2)
                    # print(len(l2))
                    # Try loop enforces password policy.
                    try:
                        symbols = '`~!@#$%^&*()_+-=[]{};:,./<>?'
                        characterBOOL = ''
                        for i, x in itertools.product(range(0, len(l1)), range(0, len(l2))):
                            character = l1[i]
                            character2 = l2[x]
                            if character.islower() and character2.islower():
                                characterBOOL = True
                            elif not character.islower() and not character2.islower():
                                characterBOOL = False
                            if characterBOOL:
                                break

                        characterUPBOOL = ''
                        for i, x in itertools.product(range(0, len(l1)), range(0, len(l2))):
                            character = l1[i]
                            character2 = l2[x]
                            if character.isupper() and character2.isupper():
                                characterUPBOOL = True
                            elif not character.isupper() and not character2.isupper():
                                characterUPBOOL = False
                            if characterUPBOOL:
                                break

                        symbolsBOOL = ''
                        for y in range(0, len(symbols)):
                            if (symbols[y] not in l1) and (symbols[y] not in l2):
                                symbolsBOOL = False
                            elif (symbols[y] in l1) and (symbols[y] in l2):
                                symbolsBOOL = True
                            if symbolsBOOL:
                                break

                        numberBOOL = ''
                        for i, x in itertools.product(range(0, len(l1)), range(0, len(l2))):
                            character = l1[i]
                            character2 = l2[x]
                            if character.isdigit() and character2.isdigit():
                                numberBOOL = True
                            elif not character.isdigit() and not character2.isdigit():
                                numberBOOL = False
                            if numberBOOL:
                                break

                        print(str(characterBOOL) + ' Lower Case')
                        print(str(characterUPBOOL) + ' Upper case')
                        print(str(symbolsBOOL) + ' symbols')
                        print(str(numberBOOL) + ' number')
                    except IndexError:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your passwords do not match!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()

                    if len(l1) == 0 or len(l2) == 0:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! You don't have a password!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif len(l1) <= 8 or len(l2) <= 8:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 8 characters!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif l1 != l2:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your passwords do not match!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif not characterBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 lower case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif not characterUPBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Upper Case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif not symbolsBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Symbol! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    elif not numberBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 number! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        x = HEY.exec_()
                    else:
                        command = """
$pass = ConvertTo-SecureString '""" + self.encrypPASS.text() + """' -AsPlainText -Force
Enable-BitLocker """ + drive + """ -PasswordProtector $pass"""
                        '''
                        Only works if 'Allow BitLocker without compatible TPM' is enabled in the Group Policy
                        Also does not encrypt right away. If you type 'Get-BitlockerVolume' in powershell, it will tell
                        you how much has been encrypted so far.
                        '''
                        print(command)

                        # sub.Popen(["powershell", "& {" + command + "}"])

                        def restartyn(i):
                            print(i)

                        COMPLETE = QMessageBox()
                        COMPLETE.setIcon(QMessageBox.Question)
                        COMPLETE.setWindowTitle('Hey! Listen!')
                        COMPLETE.setText('Restart for encryption to begin on the drive.')
                        x = COMPLETE.exec_()

                # Gets list of drives and encryption status'
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
                # print(decryptSTATUS)
                buttons = [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4,
                           self.radioButton_5, self.radioButton_6, self.radioButton_7]

                self.selectedDRIVE = ''

                # Displays the encryption status of a drive
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

                # Assigns buttons to commands
                self.radioButton.toggled.connect(lambda: STATUSCHECK(driveLETTER[0]))
                self.radioButton_2.toggled.connect(lambda: STATUSCHECK(driveLETTER[1]))
                self.radioButton_3.toggled.connect(lambda: STATUSCHECK(driveLETTER[2]))
                self.radioButton_4.toggled.connect(lambda: STATUSCHECK(driveLETTER[3]))
                self.radioButton_5.toggled.connect(lambda: STATUSCHECK(driveLETTER[4]))
                self.radioButton_6.toggled.connect(lambda: STATUSCHECK(driveLETTER[5]))
                self.enblBIT.clicked.connect(lambda: threader(ENCRYPT(self.selectedDRIVE)))
                self.cancelbutton.clicked.connect(cancelbutton)

                # Sets default status check to the C: Drive
                STATUSCHECK("C:")

                # adds the drive letters to the available radio buttons
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

                # Sets the C: Drive as the default choice
                i = 0
                while i < len(buttons):
                    if buttons[i].text() == "C:":
                        buttons[i].setChecked(True)
                    i = i + 1

                ''' 
                command = """
                $drv = Read-Host -Prompt 'What drive would you like to enable bit locker on? [Ex: c:   e:  ]   '
                manage-bde -protectors -add -pw $drv
                manage-bde -on $drv"""
                '''

        # Allows for program to continue running while the function executes.
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