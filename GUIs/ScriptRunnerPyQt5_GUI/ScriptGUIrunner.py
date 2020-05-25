import os
import sys
import time

from PyQt5 import QtGui
from PyUIs.main import Ui_MainWindow
from PyUIs.firstconf import *
from PyUIs.comdescript import Ui_comDescript
from PyUIs.progabout import Ui_About
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from scripFunc.scripUNIMULTI import *
from scripFunc.scripWINONLY import *
from scripFunc.scripLINUXONLY import *
from threading import *
from pathlib import Path
import configparser
from sys import platform


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Button logic (calls functions in module and connects to other parts of GUI. Does not actually do anything to system)


class fconfStart(QDialog, Ui_firstConf):

    def __init__(self, parent=None):
        super(fconfStart, self).__init__(parent)
        print('Script Runner First Time Configurations')
        self.setFixedSize(721, 441)
        self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
        self.setupUi(self)
        self.fcFuncts()

    def fcFuncts(self):
        print('Assigning First Time Configurations Functions')

        # sets default values
        self.ssh = 'no'
        self.ftp = 'no'
        self.proftpd = 'no'
        self.vsftpd = 'no'
        self.web = 'no'
        self.apaweb = 'no'
        self.nginweb = 'no'
        self.https = 'no'
        self.smb = 'no'
        self.sql = 'no'
        self.rsnc = 'no'
        self.rdp = 'no'

        config_name = 'config.ini'
        if getattr(sys, 'frozen', False):
            application_Path = os.path.dirname(sys.executable)
        elif __file__:
            application_Path = os.path.dirname(__file__)
        config_path = os.path.join(application_Path, config_name)
        variableCheck = Path(config_path)
        if variableCheck.is_file():
            self.quit_buttonConf.setText('Cancel')
        else:
            self.quit_buttonConf.setText('Quit')

        def sshYES(selected):
            if selected:
                print('ssh yes')
                self.ssh = 'yes'
                print(self.ssh)

        def sshNO(selected):
            if selected:
                print('ssh no')
                self.ssh = 'no'

        def ftpYES(selected):
            if selected:
                print('yes ftp')
                self.proftpdy.setEnabled(True)
                self.proftpdn.setEnabled(True)
                self.vsftpdy.setEnabled(True)
                self.vsftpdn.setEnabled(True)
                self.ftp = 'yes'

        def ftpNO(selected):
            if selected:
                print('no ftp')
                self.proftpdy.setEnabled(False)
                self.proftpdn.setEnabled(False)
                self.vsftpdy.setEnabled(False)
                self.vsftpdn.setEnabled(False)
                self.proftpdn.setChecked(True)
                self.vsftpdn.setChecked(True)
                self.ftp = 'no'
                self.proftpd = 'no'
                self.vsftpd = 'no'

        def ftpPROno(selected):
            if selected:
                print('Proftpd no')
                self.vsftpdy.setEnabled(True)
                self.vsftpdn.setEnabled(True)
                self.proftpd = 'no'

        def ftpPROyes(selected):
            if selected:
                print('Proftpd Yes')
                self.vsftpdy.setEnabled(False)
                self.vsftpdn.setEnabled(False)
                self.vsftpdn.setChecked(True)
                self.proftpd = 'yes'
                self.vsftpd = 'no'

        def vsftpdYES(selected):
            if selected:
                print('Vsftpd No')
                self.proftpdy.setEnabled(False)
                self.proftpdn.setEnabled(False)
                self.proftpdn.setChecked(True)
                self.vsftpd = 'yes'
                self.proftpd = 'no'

        def vsftpdNO(selected):
            if selected:
                print('Vsfptd Yes')
                self.proftpdy.setEnabled(True)
                self.proftpdn.setEnabled(True)
                self.vsftpd = 'no'

        def webserverNO(selected):
            if selected:
                print('No Webserver')
                self.apachey.setEnabled(False)
                self.apachen.setEnabled(False)
                self.apachen.setChecked(True)
                self.nginxy.setEnabled(False)
                self.nginxn.setEnabled(False)
                self.nginxn.setChecked(True)
                self.httpsy.setEnabled(False)
                self.httpsn.setEnabled(False)
                self.httpsn.setChecked(True)
                self.web = 'no'
                self.apaweb = 'no'
                self.nginweb = 'no'
                self.https = 'no'

        def webserverYES(selected):
            if selected:
                print('Yes Webserver')
                self.apachey.setEnabled(True)
                self.apachen.setEnabled(True)
                self.nginxy.setEnabled(True)
                self.nginxn.setEnabled(True)
                self.httpsy.setEnabled(True)
                self.httpsn.setEnabled(True)
                self.web = 'yes'

        def apacheYES(selected):
            if selected:
                print('Yes apache')
                self.nginxy.setEnabled(False)
                self.nginxn.setEnabled(False)
                self.nginxn.setChecked(True)
                self.apaweb = 'yes'
                self.nginweb = 'no'

        def apacheNo(selected):
            if selected:
                print('No Apache')
                self.nginxy.setEnabled(True)
                self.nginxn.setEnabled(True)
                self.apaweb = 'no'

        def nginxYES(selected):
            if selected:
                print('Yes Nginx')
                self.apachey.setEnabled(False)
                self.apachen.setEnabled(False)
                self.apachen.setChecked(True)
                self.nginweb = 'yes'
                self.apaweb = 'no'

        def nginxNO(selected):
            if selected:
                print('No Nginx')
                self.apachey.setEnabled(True)
                self.apachen.setEnabled(True)
                self.nginweb = 'no'

        def httpsYES(selected):
            if selected:
                print('HTTPS Yes')
                self.https = 'yes'

        def httpsNO(selected):
            if selected:
                print('https no')
                self.https = 'no'

        def smbYES(selected):
            if selected:
                print('SMB yes')
                self.smb = 'yes'

        def smbNO(selected):
            if selected:
                print('SMB no')
                self.smb = 'no'

        def sqlYES(selected):
            if selected:
                print('SQL Yes')
                self.sql = 'yes'

        def sqlNO(selected):
            if selected:
                print('SQL No')
                self.sql = 'no'

        def rsncYES(selected):
            if selected:
                print('rsnc Yes')
                self.rsnc = 'yes'

        def rsncNO(selected):
            if selected:
                print('rsnc No')
                self.rsnc = 'no'

        def rdpYES(selected):
            if selected:
                print('RDP Yes')
                self.rdp = 'yes'

        def rdpNO(selected):
            if selected:
                print('RDP No')
                self.rdp = 'no'

        def quitButton():
            print('Closing program')
            if variableCheck.is_file():
                self.close()
            else:
                sys.exit(0)

        def confirmBTTN():
            if self.ssh != '' and self.ftp != '' and self.proftpd != '' and self.vsftpd != '' and self.web != '' and self.apaweb != '' and self.nginweb != '' and self.https != '' and self.smb != '' and self.sql != '' and self.rsnc != '' and self.rdp != '':
                print('saving configurations\n')
                print(
                    "ssh=" + self.ssh + ", ftp=" + self.ftp + ", proftpd=" + self.proftpd + ", vsftpd=" + self.vsftpd + ", web=" + self.web + ", apaweb=" + self.apaweb + ", nginweb=" + self.nginweb + ", https=" + self.https + ", smb=" + self.smb + ", sql=" + self.sql + ", rsnc=" + self.rsnc + ", RDP=" + self.rdp)

                filename = "config.ini"

                config = configparser.ConfigParser()
                config['Services'] = {'ssh': self.ssh,
                                      'ftp': self.ftp,
                                      'proftpd': self.proftpd,
                                      'vsftpd': self.vsftpd,
                                      'web': self.web,
                                      'apaweb': self.apaweb,
                                      'nginweb': self.nginweb,
                                      'https': self.https,
                                      'smb': self.smb,
                                      'sql': self.sql,
                                      'rsnc': self.rsnc,
                                      'rdp': self.rdp}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

                def closing():
                    print('closing')
                    self.close()


                RESTART = QMessageBox()
                RESTART.setWindowTitle("Hey! Listen!")
                RESTART.setText("Configurations have been sucessfully saved.")
                RESTART.setIcon(QMessageBox.Information)
                RESTART.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                RESTART.setStandardButtons(QMessageBox.Close)
                #RESTART.buttonClicked.connect(lambda: closing())
                x = RESTART.exec_()
                self.close()
            else:
                HEY = QMessageBox()
                HEY.setWindowTitle('Hey! Listen!')
                HEY.setText("Hey! You have not finished filling in all of the choices!")
                HEY.setIcon(QMessageBox.Critical)
                HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = HEY.exec_()

        self.sshy.toggled.connect(sshYES)
        self.sshn.toggled.connect(sshNO)
        self.proftpdy.toggled.connect(ftpPROyes)
        self.proftpdn.toggled.connect(ftpPROno)
        self.vsftpdy.toggled.connect(vsftpdYES)
        self.vsftpdn.toggled.connect(vsftpdNO)
        self.ftpy.toggled.connect(ftpYES)
        self.ftpn.toggled.connect(ftpNO)
        self.webn.toggled.connect(webserverNO)
        self.weby.toggled.connect(webserverYES)
        self.apachey.toggled.connect(apacheYES)
        self.apachen.toggled.connect(apacheNo)
        self.nginxy.toggled.connect(nginxYES)
        self.nginxn.toggled.connect(nginxNO)
        self.httpsy.toggled.connect(httpsYES)
        self.httpsn.toggled.connect(httpsNO)
        self.smby.toggled.connect(smbYES)
        self.smbn.toggled.connect(smbNO)
        self.sqly.toggled.connect(sqlYES)
        self.sqln.toggled.connect(sqlNO)
        self.rsyncy.toggled.connect(rsncYES)
        self.rsyncn.toggled.connect(rsncNO)
        self.rdpy.toggled.connect(rdpYES)
        self.rdpn.toggled.connect(rdpNO)
        self.confirmbtn.clicked.connect(confirmBTTN)
        self.quit_buttonConf.clicked.connect(quitButton)


class Mainstart(QMainWindow, Ui_MainWindow):

    def threader(self, com):
        try:
            threader = Thread(target=com)
            threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    def __init__(self, parent=None):
        super(Mainstart, self).__init__(parent)
        print('Script Runner has started')

        config_name = 'config.ini'
        if getattr(sys, 'frozen', False):
            application_Path = os.path.dirname(sys.executable)
        elif __file__:
            application_Path = os.path.dirname(__file__)
        config_path = os.path.join(application_Path, config_name)
        print(config_path)
        variableCheck = Path(config_path)

        if variableCheck.is_file():
            config = configparser.ConfigParser()
            config.read(variableCheck)
            # x = config.get('Services', 'ssh')
            # print(x)
            print('Configuration file has been loaded...')

            QMainWindow.__init__(self)
            self.setupUi(self)
            self.setFixedSize(848, 603)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.mmfuncassign(variableCheck)
        else:
            print('Ello, you have some configurations to do!')

            def firstCONF():
                widget = fconfStart()
                widget.exec_()

            self.threader(firstCONF())

        ###################

    def mmfuncassign(self, configurations):
        print('Assigning functions')
        config = configparser.ConfigParser()
        config.read(configurations)

        self.header_title.setWordWrap(True)
        self.descriptions.setWordWrap(True)
        scripfunc = ScriptRunnerFunc()
        funcWIN = funcWINONLY()
        funcLIN = funcLINUX()

        def quitButton():
            print('Closing program')
            sys.exit(0)

        def display(i):
            if i == 0:
                self.header_title.setText('Universal Commands')
                self.descriptions.setText(
                    'Description: These commands will work on most Operating Systems\nE.g. Windows, MacOS X, and Linux (Debian, Ubuntu, certain Arch distros)')
                self.stackedWidget.setCurrentIndex(i)
            elif i == 1:
                if platform == 'win32':
                    self.header_title.setText('Windows 10 Commands')
                    self.descriptions.setText(
                        'Description: These commands will work on the following Windows systems: 10, 8.x, and 7')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()
            elif i == 2:
                if platform == 'linux' or platform == 'Linux':
                    self.header_title.setText('Linux Commands')
                    self.descriptions.setText(
                        'Description: These commands will work on the following Linux systems: Debian based systems, Ubuntu, and Manjaro')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()
            elif i == 3:
                if platform == 'darwin':
                    self.header_title.setText('MacOS X Commands')
                    self.descriptions.setText('Description: These commands will ONLY work on MacOS X')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()

        display(0)

        def light_darkMODE(i):
            print('Mode change')
            if i == 0:
                print('Dark Mode in development')
            elif i == 1:
                print('Light Mode in development')

        def showHOWTO():
            HOWTO = QMessageBox()
            HOWTO.setWindowTitle('Hey! This is a How To!')
            HOWTO.setText("""
+----------------------------------------+
|    H o w  T o  U s e  T h e  P r o g r a m    |
+----------------------------------------+

1.) Run as root
2.) Choose command that you would like to use
3.) Click it
4.) Sit back and relax while the command runs   :)
""")
            HOWTO.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HOWTO.setStyleSheet('background-color: #414E6E; color: #CCD2E6')
            x = HOWTO.exec_()  # change to QDialog

        def runCOMDESCRIPT():
            class showComDescript(QDialog, Ui_comDescript):
                def __init__(self, parent=None):
                    super(showComDescript, self).__init__(parent)
                    self.setupUi(self)
                    self.setFixedSize(531, 360)
                    self.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))

            def callCOMdescript():
                widget = showComDescript()
                widget.exec_()

            callCOMdescript()

        def runABOUTPROG():
            class showAboutProg(QDialog, Ui_About):
                def __init__(self, parent=None):
                    super(showAboutProg, self).__init__(parent)
                    self.setupUi(self)
                    self.setFixedSize(330, 182)
                    self.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))

            def callaboutprog():
                widget = showAboutProg()
                widget.exec_()

            callaboutprog()

        def indev():
            INDEV = QMessageBox()
            INDEV.setWindowTitle('Hey! Listen!')
            INDEV.setText('Hey! This command is not yet complete and in development!')
            INDEV.setIcon(QMessageBox.Critical)
            INDEV.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            x = INDEV.exec_()

        def wrongos():
            WRONGOS = QMessageBox()
            WRONGOS.setWindowTitle('Hey! Listen!')
            WRONGOS.setText('Hey! These commands do not support this Operating System!')
            WRONGOS.setIcon(QMessageBox.Critical)
            WRONGOS.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            x = WRONGOS.exec_()

        def chngconf():
            widget = fconfStart()
            widget.exec_()

        self.uniCom.clicked.connect(lambda: display(0))
        self.winCom.clicked.connect(lambda: display(1))
        self.linCom.clicked.connect(lambda: display(2))
        self.macCom.clicked.connect(lambda: display(3))
        self.actionLight_Mode.triggered.connect(lambda: light_darkMODE(1))
        self.actionDark_Mode.triggered.connect(lambda: light_darkMODE(0))

        # Menubar Buttons
        self.actionHow_To_Use_Program.triggered.connect(lambda: self.threader(showHOWTO()))
        self.actionAbout_Creator.triggered.connect(lambda: self.threader(runABOUTPROG()))
        self.actionCommand_Descriptions.triggered.connect(lambda: self.threader(runCOMDESCRIPT()))
        self.actionChange_Configurations.triggered.connect(lambda: self.threader(chngconf()))

        # Universal Buttons
        self.Updates_buttonUNI.clicked.connect(lambda: self.threader(scripfunc.updateos()))
        self.rmvprosoftbuttonUNI.clicked.connect(lambda: self.threader(indev()))  #
        self.srchmedbuttonUNI.clicked.connect(lambda: self.threader(scripfunc.srchmedia))
        self.chkhashfile_buttonUNI.clicked.connect(lambda: self.threader(scripfunc.hashCheck()))

        # Windows Main Menu Commands

        self.fwlbutton_2.clicked.connect(lambda: self.threader(scripfunc.fwl))
        self.basicConfbutton_2.clicked.connect(lambda: self.threader(lambda: scripfunc.basConf(config.get('Services', 'rdp'))))  #
        self.rmvprosoftbutton_2.clicked.connect(lambda: self.threader(scripfunc.rmProSoft()))
        self.enblBitLockerbutton.clicked.connect(lambda: self.threader(funcWIN.BITLOCKER()))
        self.servicesConfButton_4.clicked.connect(lambda: self.threader(scripfunc.servSet(config.get('Services', 'ssh'), config.get('Services', 'smb'), config.get('Services', 'web'), config.get('Services', 'apaweb'), config.get('Services', 'nginweb'))))
        # Windows User Group Commands
        self.WINUSRGRUBUTTON = [self.adgrutosys_3, self.adusrtogru_3, self.adusrtosys_3, self.chngusrpas_3,
                                self.lsgruusrin_3, self.lslocagru_3, self.lslocausr_3, self.lsmemgru_3,
                                self.rmvgrufrosys_3, self.rmvusrfrogru_3, self.rmvusrfrosys_3]
        for i in range(0, 11):
            self.WINUSRGRUBUTTON[i].clicked.connect(lambda: self.threader(indev()))  #

        # Linux Main Menu Commands
        self.fwlbutton_3.clicked.connect(lambda: self.threader(scripfunc.fwl))
        self.auditbutton_3.clicked.connect(lambda: self.threader(funcLIN.alyn))
        self.malrembutton_3.clicked.connect(lambda: self.threader(funcLIN.malRem()))  #
        self.rmvprosoftbutton_3.clicked.connect(lambda: self.threader(indev()))  #
        self.basicConfbutton_3.clicked.connect(lambda: self.threader(indev()))  #
        self.servicesConfButton_2.clicked.connect(lambda: self.threader(indev()))  #
        # Linux User Group Commands
        self.LINUXUSRGRUBUTTONS = [self.adgrutosys_4, self.adusrtogru_4, self.adusrtosys_4, self.chngusrpas_4,
                                   self.lsgruusrin_4, self.lslocagru_4, self.lslocausr_4, self.lsmemgru_4,
                                   self.rmvgrufrosys_4, self.rmvusrfrogru_4, self.rmvusrfrosys_4]
        for i in range(0, 11):
            self.LINUXUSRGRUBUTTONS[i].clicked.connect(lambda: self.threader(indev()))  #

        # MacOS Buttons
        self.MACBUTTONS = [self.rmvprosoftbutton_4, self.malrembutton_4, self.basicConfbutton_4,
                           self.servicesConfButton_3, self.adgrutosys_5, self.adusrtogru_5, self.adusrtosys_5,
                           self.chngusrpas_5, self.lsgruusrin_5, self.lslocagru_5, self.lslocausr_5, self.lsmemgru_5,
                           self.rmvgrufrosys_5, self.rmvusrfrogru_5, self.rmvusrfrosys_5]
        for i in range(0, 15):
            self.MACBUTTONS[i].clicked.connect(lambda: self.threader(indev()))

        self.quit_button_3.clicked.connect(quitButton)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Mainstart()
    main.show()
    sys.exit(app.exec_())
