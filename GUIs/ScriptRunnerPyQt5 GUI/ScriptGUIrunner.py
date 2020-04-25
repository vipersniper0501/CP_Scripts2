import os
import sys
import time
from main import Ui_MainWindow
from aboutcreator import *
from firstconf import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from scripFunc.scripEXEC import *
from threading import *
from pathlib import Path
import configparser



###################
#Ideas:
# Universal Commands Section/Windows 10 Section/Linux Section/MacOS X Section
# Command that finds Hash Value of file
# 
###################


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Button logic (calls functions in module and connects to other parts of GUI. Does not actually do anything to system)


class fconfStart(QMainWindow, Ui_firstConf):

    def __init__(self):
        print('Script Runner First Time Configurations')
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(726, 448)
        self.setWindowIcon(QtGui.QIcon('cup2.png'))
        self.fcFuncts()

    def fcFuncts(self):
        print('Assigning First Time Configurations Functions')

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
                self.vsfptpd = 'no'

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
            sys.exit()

        def confirmBTTN():
            if self.ssh != '' and self.ftp != '' and self.proftpd != '' and self.vsftpd != '' and self.web != '' and self.apaweb != '' and self.nginweb != '' and self.https != '' and self.smb != '' and self.sql != '' and self.rsnc != '' and self.rdp != '':
                print('saving configurations\n')
                print("ssh=" + self.ssh + ", ftp=" + self.ftp + ", proftpd=" + self.proftpd + ", vsftpd=" + self.vsftpd + ", web=" + self.web + ", apaweb=" + self.apaweb + ", nginweb=" + self.nginweb + ", https=" + self.https + ", smb=" + self.smb + ", sql=" + self.sql + ", rsnc=" + self.rsnc + ", RDP=" + self.rdp)

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

                RESTART = QMessageBox()
                RESTART.setWindowTitle("Hey! Listen!")
                RESTART.setText("Reopen the program to continue.")
                RESTART.setIcon(QMessageBox.Information)
                RESTART.setWindowIcon(QtGui.QIcon('HEY.png'))
                RESTART.setStandardButtons(QMessageBox.Close)
                RESTART.buttonClicked.connect(lambda: sys.exit(0))
                x = RESTART.exec_()
            else:
                HEY = QMessageBox()
                HEY.setWindowTitle('Hey! Listen!')
                HEY.setText("Hey! You have not finished filling in all of the choices!")
                HEY.setIcon(QMessageBox.Critical)
                HEY.setWindowIcon(QtGui.QIcon('HEY.png'))
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

    def __init__(self):
        print('Script Runner has started')

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(604, 427)
        self.setWindowIcon(QtGui.QIcon('cup2.png'))
        self.mmfuncassign()

    #####################################
    def mmfuncassign(self):
        print('Assigning functions')






        scripfunc = ScriptRunnerFunc()

        # self.menubarButtons = [self.actionAbout_Creator]
        # self.menubarActions = [self.aboutCre]

        # buttons = {self.Updates_button:scripfunc.updateos}

        # self.buttonNames = [self.Updates_button, self.servsetbutton, self.fwlbutton, self.malrembutton, self.rmvprosoftbutton, self.basicConfbutton, self.auditbutton, self.srchmedbutton]
        # targets = [scripfunc.updateos, scripfunc.servSet, scripfunc.fwl, scripfunc.malRem, scripfunc.rmProCont, scripfunc.basConf, scripfunc.alyn, scripfunc.srchmedia]

        # menubar
        # for i in range(0, len(self.menubarButtons)):
        #    self.menubarButtons[i].triggered.connect(self.menubarActions[i])

        # for i in range(0, len(self.buttonNames)):
        #    self.buttonNames[i].setCheckable(True)
        #    self.buttonNames[i].clicked.connect(lambda i=i: threader(i))
        #    self.buttonNames[i].pressed.connect(lambda i=i: buttonPress(i))
        # self.quit_button.clicked.connect(self.quitButon)

        def quitButton():
            print('Closing program')
            sys.exit()

        # Main Menu Buttons
        self.quit_button.clicked.connect(quitButton)
        self.Updates_button.clicked.connect(lambda: threader(scripfunc.updateos))
        self.servsetbutton.clicked.connect(lambda: threader(scripfunc.servSet))
        self.fwlbutton.clicked.connect(lambda: threader(scripfunc.fwl))
        self.malrembutton.clicked.connect(lambda: threader(scripfunc.malRem))
        self.rmvprosoftbutton.clicked.connect(lambda: threader(scripfunc.rmProCont))
        self.basicConfbutton.clicked.connect(lambda: threader(scripfunc.basConf))
        self.auditbutton.clicked.connect(lambda: threader(scripfunc.alyn))
        self.srchmedbutton.clicked.connect(lambda: threader(scripfunc.srchmedia))


        #User/Group Menu Buttons
        self.quit_button_3.clicked.connect(quitButton)

        def threader(com):
            try:
                threader = Thread(target=com)
                threader.start()
            except Exception as e:
                print(e)
                print('Could not start thread')


        # def buttonPress(button):
        # print('button pressed')
        # print(self.buttonNames[button])
        #    if self.buttonNames[button].isChecked():
        #        self.buttonNames[button].setStyleSheet("""


# border: 2px solid;
# border-color: grey;
# border-style: inset;
# border-width: 2.5px;
# background-color: lightblue;
# border-radius: 10px;
# color: black;
#                """)

#            else:
#               self.buttonNames[button].setStyleSheet("""
# border: 2px solid;
# border-color: grey;
# border-style: outset;
# border-width: 2.5px;
# background-color: lightblue;
# border-radius: 10px;
# color: black;
#                """)


######################







if __name__ == "__main__":

    cwd = os.getcwd()
    variableCheck = Path(cwd + '/config.ini')
    print(variableCheck)
    print(cwd)
    variableCheck.is_file()
    if variableCheck.is_file():

        config = configparser.ConfigParser()
        config.read('config.ini')
        x = config.get('Services', 'ssh')
        print(x)

        print('Configuration file has been loaded...')

        app = QApplication(sys.argv)
        main = Mainstart()
        main.show()
        sys.exit(app.exec_())
    else:
        print('Ello, you have some configurations to do!')
        app = QApplication(sys.argv)
        main = fconfStart()
        main.show()
        sys.exit(app.exec_())


