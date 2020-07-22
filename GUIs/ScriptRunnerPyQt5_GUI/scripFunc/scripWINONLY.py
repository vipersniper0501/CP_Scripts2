import configparser
import itertools
import os
import shutil
import subprocess as sub
from threading import *
from distutils.dir_util import copy_tree

import distro  # for figuring out what linux distro
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

from PyUIs.changepass import Ui_chngpass
from PyUIs.enblebit import Ui_bitlockerGUI
from PyUIs.addusrUI import Ui_addUSR
from PyUIs.rmvUSRoGRU import Ui_rmvusrogru

OS = distro.linux_distribution()
ops = OS[0]

config = configparser.ConfigParser()
config.read('config.ini')


# This function is not really needed, but nice to have if needed.
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS # pylint: disable=no-member
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)


# This file is used to store commands that are to only be used on Windows machines


# TODO: When done, possible convert the try and if statements used for enforcing the complexity requirement into it's
#  own function to reduce the number of lines in the file.


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

                        sub.Popen(["powershell", "& {" + command + "}"])

                        def restart():
                            print('Restart is now happening')
                            command = 'Restart-Computer'
                            sub.Popen(["powershell", "& {" + command + "}"])

                        COMPLETE = QMessageBox()
                        COMPLETE.setIcon(QMessageBox.Question)
                        COMPLETE.setWindowTitle('Hey! Listen!')
                        COMPLETE.setText('You must restart the computer for encryption to begin on the drive. '
                                         '\nWould you like to restart now?')
                        COMPLETE.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                        x = COMPLETE.exec_()

                        if x == QMessageBox.Yes:
                            print('Restarting...')
                            restart()
                        elif x == QMessageBox.No:
                            print('Closing...')
                            self.close()

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
                    except Exception:
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
                try:
                    STATUSCHECK("C:")
                except Exception:
                    STATUSCHECK("c:")

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

    def browserCONF(self):
        print('Configuring browser...')
        # def cptree(src, dst, symlinks=False, ignore=None):
        #    for item in os.listdir(src):
        #        s = os.path.join(src, item)
        #        d = os.path.join(dst, item)
        #    if os.path.isdir(s):
        #        shutil.copytree(s, d, symlinks, ignore)
        #    else:
        #        shutil.copy2(s, d)
        try:
            EXEC = sub.Popen(["powershell", "& {$env:UserName}"], stdout = sub.PIPE)
            stdout, _ = EXEC.communicate()
            output = stdout.decode("utf-8")
            output = output.split('\r\n')
            # shutil.rmtree(r'%appdata%\Mozilla\Extensions')
            rmv_folder = 'C:\\Users\\' + str(output[0]) + '\\AppData\\Roaming\\Mozilla\\Firefox'
            shutil.rmtree(rmv_folder)
            # shutil.rmtree(r'%appdata%\Mozilla\SystemExtensionsDev')
        except Exception as e:
            print('Error caught: ' + str(e))
        # copy_tree('../configurations/Win_Mozilla/Extensions', 'C:/')
        # copy_tree('../configurations/Win_Mozilla/Firefox', 'C:/')
        # copy_tree('../configurations/Win_Mozilla/SystemExtensionsDev', 'C:/')
        shutil.copytree('../configurations/Win_Mozilla/Extensions',
                        r'%appdata%\Mozilla\Extensions')
        shutil.copytree('../configurations/Win_Mozilla/Firefox',
                        r'%appdata%\Mozilla\Firefox')
        shutil.copytree('../configurations/Win_Mozilla/SystemExtensionsDev',
                        r'%appdata%\Mozilla\SystemExtensionsDev')
        print('Firefox has been configured')


def threader(com):
    try:
        threader = Thread(target = com)
        threader.start()
    except Exception as e:
        print(e)
        print('Could not start thread')


class funcWINusrgru:
    def addusr(self):
        class addusrtosys(QDialog, Ui_addUSR):
            def __init__(self, parent = None):
                super(addusrtosys, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):
                self.adminyn = 'n'

                def adminy(selected):
                    if selected:
                        print('This user will be an admin')
                        self.adminyn = 'y'

                def adminn(selected):
                    if selected:
                        print('This user will NOT be an admin')
                        self.adminyn = 'n'

                self.admin_y.toggled.connect(adminy)
                self.admin_n.toggled.connect(adminn)

                def CONFIRM():
                    username = self.username_input.text()
                    passwd = self.Password1_input.text()
                    passwd_confirm = self.Password2_input.text()

                    l1 = passwd
                    l2 = passwd_confirm
                    # Try loop enforces password policy.
                    try:
                        symbols = "`~!@#$%^&*()_+-=[]{};:,./<>?"
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
                        HEY.exec_()

                    def completedPOP():
                        COMPLETE = QMessageBox()
                        COMPLETE.setIcon(QMessageBox.Question)
                        COMPLETE.setWindowTitle('Hey! Listen!')
                        COMPLETE.setText('User ' + username + ' has been successfully added to system.')
                        COMPLETE.setStandardButtons(QMessageBox.Close)
                        COMPLETE.exec_()
                        self.close()

                    if len(username) == 0:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! You don't have a username!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif len(l1) == 0 or len(l2) == 0:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! You don't have a password!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif len(l1) <= 8 or len(l2) <= 8:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 8 characters!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif l1 != l2:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your passwords do not match!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not characterBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 lower case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not characterUPBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Upper Case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not symbolsBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Symbol! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not numberBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 number! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    else:
                        if self.adminyn == 'y':
                            print('This user will be an admin')
                            print(os.getcwd())
                            command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwd) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Add-LocalGroupMember -Group "Administrators" -Member $nusnm"""
                            print(command)
                            sub.Popen(["powershell", "& {" + command + "}"])
                            print('User ' + username + " has been successfully added!")
                            completedPOP()
                        elif self.adminyn == 'n':
                            print('This user will not be an admin')
                            command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwd) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss"""
                            print(command)
                            sub.Popen(["powershell", "& {" + command + "}"])
                            print('User ' + username + " has been successfully added!")
                            completedPOP()

                def cancelbutton():
                    self.close()

                self.Confirm_button.clicked.connect(lambda: threader(CONFIRM()))
                self.Cancel_button.clicked.connect(cancelbutton)

                def threader(com):
                    try:
                        threader = Thread(target=com)
                        threader.start()
                    except Exception as e:
                        print(e)
                        print('Could not start thread')

        def calladdusrtosys():
            widget = addusrtosys()
            widget.exec_()

        calladdusrtosys()

    def remusr(self):
        class rmvusrfrosys(QDialog, Ui_rmvusrogru):
            def __init__(self, parent = None):
                super(rmvusrfrosys, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):
                self.setWindowTitle('Remove User From System')
                self.label.setText('Current Users:')
                self.label2.setText('Username: ')

                def findnames():
                    # Local users are added to a list of names
                    EXEC = sub.Popen(["powershell", "& {net localgroup users}"], stdout = sub.PIPE)
                    stdout, _ = EXEC.communicate()
                    output = stdout.decode("utf-8")
                    output = output.split("\n")
                    # print(output)
                    n = []
                    for i in range(6, len(output) - 3):
                        # print(output[i])
                        # if '\r' in output[i]:
                        #     print('found in ' + str(i))
                        #     print(output[i])
                        n.append(output[i])
                    a = []
                    for i in range(0, len(n)):
                        x = n[i]
                        y = x.split('\r')
                        # print(y)
                        a.append(y)
                    # print(a)
                    names = []
                    for i in range(0, len(a)):
                        # print(a[i])
                        x = a[i]
                        y = x[0]
                        # print(y)
                        names.append(y)
                    # print(names)

                    # Local Administrators are added to list of names
                    EXEC = sub.Popen(["powershell", "& {net localgroup administrators}"],
                                     stdout = sub.PIPE)
                    stdout, _ = EXEC.communicate()
                    output = stdout.decode("utf-8")
                    output = output.split("\n")
                    # print(output)
                    n2 = []
                    for i in range(6, len(output) - 3):
                        # print(output[i])
                        # if '\r' in output[i]:
                        #     print('found in ' + str(i))
                        #     print(output[i])
                        n2.append(output[i])
                    a2 = []
                    for i in range(0, len(n2)):
                        x = n2[i]
                        y = x.split('\r')
                        # print(y)
                        a2.append(y)
                    # print(a)
                    for i in range(0, len(a2)):
                        # print(a[i])
                        x = a2[i]
                        y = x[0]
                        EXEC = sub.Popen(["powershell", "& {$env:UserName}"], stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        output = output.split('\r\n')
                        if output[0] == y:
                            y = output[0] + '   (Current User)'
                        # print(y)
                        names.append(y)
                    # print(names)
                    return names

                listoNames = findnames()

                for i in range(0, len(listoNames)):
                    QListWidgetItem(listoNames[i], self.listOFnames)

                username = self.Username_Input.text()

                def completedPOP(username):
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        'User ' + username + ' has been successfully removed from the system.')
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.close()

                def removal(username):
                    sub.Popen(["powershell", "& {net user " + username + " /DELETE}"])
                    completedPOP(username)

                def confirmation(com):
                    CONFIRM = QMessageBox()
                    CONFIRM.setWindowTitle('Hey! Listen!')
                    CONFIRM.setText("Hey! Are you sure you want to do this?")
                    CONFIRM.setIcon(QMessageBox.Critical)
                    CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                    CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    x = CONFIRM.exec_()
                    if x == QMessageBox.Yes:
                        print('Removing user ' + com)
                        removal(com)
                    elif x == QMessageBox.No:
                        print('Cancelling...')

                self.Confirm_button.clicked(lambda: confirmation(username))

        def callrmvusrfrosys():
            widget = rmvusrfrosys()
            widget.exec_()

        callrmvusrfrosys()

    def addgrutosys(self):
        pass

    def remgrufrosys(self):
        pass

    def addusrtogru(self):
        pass

    def remusrfrogru(self):
        pass

    def lslocausrs(self):
        pass

    def lslocagrus(self):
        pass

    def lsmemofgru(self):
        pass

    def lsgrusanusrin(self):
        pass

    def chngpasswdofall(self):

        # TODO: This command as of July 7th, 2020 is broken. More on the issue can be found here: https://github.com/vipersniper0501/CP_Scripts2/issues/48

        class changepasswordofall(QDialog, Ui_chngpass):
            def __init__(self, parent=None):
                super(changepasswordofall, self).__init__(parent)
                self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
                self.setupUi(self)
                self.EXECUTE()

            def EXECUTE(self):
                def findnames():
                    names = []
                    try:
                        print('Detecting Users On System...')
                        # Local users are added to a list of names
                        EXEC = sub.Popen(["powershell", "& {net localgroup users}"],
                                         stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        output = output.split("\n")
                        # print(output)
                        n = []
                        for i in range(6, len(output) - 3):
                            # print(output[i])
                            # if '\r' in output[i]:
                            #     print('found in ' + str(i))
                            #     print(output[i])
                            n.append(output[i])
                        a = []
                        for i in range(0, len(n)):
                            x = n[i]
                            y = x.split('\r')
                            # print(y)
                            a.append(y)
                        # print(a)
                        # names = []
                        for i in range(0, len(a)):
                            # print(a[i])
                            x = a[i]
                            y = x[0]
                            # print(y)
                            names.append(y)
                        # print(names)
                        # Local Administrators are added to list of names
                        EXEC = sub.Popen(["powershell", "& {net localgroup administrators}"],
                                         stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        output = output.split("\n")
                        # print(output)
                        n2 = []
                        for i in range(6, len(output) - 3):
                            # print(output[i])
                            # if '\r' in output[i]:
                            #     print('found in ' + str(i))
                            #     print(output[i])
                            n2.append(output[i])
                        a2 = []
                        for i in range(0, len(n2)):
                            x = n2[i]
                            y = x.split('\r')
                            # print(y)
                            a2.append(y)
                        # print(a)
                        for i in range(0, len(a2)):
                            # print(a[i])
                            x = a2[i]
                            y = x[0]
                            # print(y)
                            names.append(y)
                        # print(names)

                        # Removal of current user from list of names (This is so the current user does not get it's password
                        # changed.
                        EXEC = sub.Popen(["powershell", "& {$env:UserName}"], stdout = sub.PIPE)
                        stdout, _ = EXEC.communicate()
                        output = stdout.decode("utf-8")
                        output = output.split('\r\n')
                        # print(output)
                        for i in range(0, len(names)):
                            # print(i)
                            print(names[i])
                            if output[0] == names[i]:
                                # print('user found')
                                # print(i)
                                names.pop(i)
                                # print(names)
                            if i == len(names):
                                break
                        print('--------------------------------------------------')
                        print('The following list are all current users and admins on this system')
                        print(names)
                        return names
                    except Exception as e:
                        print('Index error has occured. exception was caught: ' + str(e))
                        print(names)
                        return names

                x = findnames()

                def completedPOP():
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText('Passwords for all users have been successfully changed.')
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.close()

                def RUN(names):
                    l1 = self.passwd.text()
                    # print(l1)
                    # print(len(l1))
                    l2 = self.pass_verify.text()
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
                        HEY.exec_()

                    if len(l1) == 0 or len(l2) == 0:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! You don't have a password!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif len(l1) <= 8 or len(l2) <= 8:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 8 characters!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif l1 != l2:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your passwords do not match!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not characterBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 lower case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not characterUPBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Upper Case letter!")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not symbolsBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 Symbol! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    elif not numberBOOL:
                        HEY = QMessageBox()
                        HEY.setWindowTitle('Hey! Listen!')
                        HEY.setText("Hey! Your password must have at least 1 number! [Ex: !@#$%^%&]")
                        HEY.setIcon(QMessageBox.Critical)
                        HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                        HEY.exec_()
                    else:
                        for i in range(0, len(names)):
                            command = """$Password = ConvertTo-SecureString """ + "'{}'".format(
                                self.passwd.text()) + """ -AsPlainText -Force
$Username = Get-LocalUser -Name """ + "'{}'".format(names[i]) + """
$Username | Set-LocalUser -Password $Password"""
                            # print(command + "\n")
                            sub.Popen(["powershell", "& {" + command + "}"], stdout = sub.PIPE)
                            print('User ' + names[i] + "'s password has been successfully changed.")
                        completedPOP()

                self.chngpass_button.clicked.connect(lambda: threader(RUN(x)))

                # def threader(com):
                #     try:
                #         threader = Thread(target=com)
                #         threader.start()
                #     except Exception as e:
                #         print(e)
                #         print('Could not start thread')

        def callChangepaswordofall():
            widget = changepasswordofall()
            widget.exec_()

        callChangepaswordofall()
