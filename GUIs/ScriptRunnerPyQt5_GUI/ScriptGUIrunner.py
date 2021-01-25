#!/usr/bin/env python3
import configparser
import os
import sys
import logging as log
from pathlib import Path
from platform import uname
from threading import Thread
import threading
from typing import Any

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject

from PyUIs.comdescript import Ui_comDescript
from PyUIs.firstconf import Ui_firstConf
from PyUIs.main import Ui_MainWindow
from PyUIs.progabout import Ui_About
from PyUIs.howToUI import Ui_How_To

from scripFunc.scripLINUXONLY import malRem, alyn
from scripFunc.scripUNIMULTI import Update_OS, Media_Search, Configure_Firewall, Basic_Configurations, rmProSoft, Configure_Services, Hash_Run
from scripFunc.scripWINONLY import BITLOCKER, Configure_Browsers, chngpasswdofall, lsgrusanusrin, lsmemofgru, lslocagrus, lslocausrs, remusrfrogru, addusrtogru, remgrufrosys, addgrutosys, remusr, addusr

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

# log.basicConfig(filename = 'runtime.log', level=log.INFO)


try:
    if sys.argv[1] == '--DEBUG':
        DEBUG = True
except IndexError:
    DEBUG = False

print(DEBUG)


def NewThread(com, Returning: bool, thread_ID, *arguments) -> Any:
    """
    Will create a new thread for a function/command.

    :param com: Command to be Executed
    :param Returning: True/False Will the command return anything?
    :param thread_ID: Name of thread
    :param arguments: Arguments to be sent to Command

    """
    
    class NewThreadWorker(Thread):
        def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, *,
                     daemon = None):
            Thread.__init__(self, group, target, name, args, kwargs, daemon = daemon)
            self.daemon = True
            self._return = None
        
        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        
        def joinThread(self):
            Thread.join(self)
            return self._return
    
    ntw = NewThreadWorker(target = com, name = thread_ID, args = (*arguments,))
    if Returning:
        ntw.start()
        return ntw.joinThread()
    else:
        ntw.start()


def CIDR_Configurations():

    class fconfStart(QDialog, Ui_firstConf):
        def __init__(self, parent = None):
            super(fconfStart, self).__init__(parent)
            print('Script Runner First Time Configurations')
            self.setFixedSize(720, 440)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setupUi(self)
            self.fcFuncts()
        
        def fcFuncts(self):
            print('Assigning First Time Configurations Functions')
            
            # sets default values
            self.rdp = False
            self.rsnc = False
            self.sql = False
            self.smb = False
            self.https = False
            self.nginweb = False
            self.apaweb = False
            self.web = False
            self.vsftpd = False
            self.proftpd = False
            self.ftp = False
            self.ssh = False
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
                    self.ssh = True
            
            def sshNO(selected):
                if selected:
                    print('ssh no')
                    self.ssh = False

            def ftpYES(selected):
                if selected:
                    print('yes ftp')
                    self.proftpdy.setEnabled(True)
                    self.proftpdn.setEnabled(True)
                    self.vsftpdy.setEnabled(True)
                    self.vsftpdn.setEnabled(True)
                    self.ftp = True
            
            def ftpNO(selected):
                if selected:
                    print('no ftp')
                    self.proftpdy.setEnabled(False)
                    self.proftpdn.setEnabled(False)
                    self.vsftpdy.setEnabled(False)
                    self.vsftpdn.setEnabled(False)
                    self.proftpdn.setChecked(True)
                    self.vsftpdn.setChecked(True)
                    self.ftp = False
                    self.proftpd = False
                    self.vsftpd = False
            
            def ftpPROno(selected):
                if selected:
                    print('Proftpd no')
                    self.vsftpdy.setEnabled(True)
                    self.vsftpdn.setEnabled(True)
                    self.proftpd = False
            
            def ftpPROyes(selected):
                if selected:
                    print('Proftpd Yes')
                    self.vsftpdy.setEnabled(False)
                    self.vsftpdn.setEnabled(False)
                    self.vsftpdn.setChecked(True)
                    self.proftpd = True
                    self.vsftpd = False
            
            def vsftpdYES(selected):
                if selected:
                    print('Vsftpd No')
                    self.proftpdy.setEnabled(False)
                    self.proftpdn.setEnabled(False)
                    self.proftpdn.setChecked(True)
                    self.vsftpd = True
                    self.proftpd = False
            
            def vsftpdNO(selected):
                if selected:
                    print('Vsfptd Yes')
                    self.proftpdy.setEnabled(True)
                    self.proftpdn.setEnabled(True)
                    self.vsftpd = False
            
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
                    self.web = False
                    self.apaweb = False
                    self.nginweb = False
                    self.https = False
            
            def webserverYES(selected):
                if selected:
                    print('Yes Webserver')
                    self.apachey.setEnabled(True)
                    self.apachen.setEnabled(True)
                    self.nginxy.setEnabled(True)
                    self.nginxn.setEnabled(True)
                    self.httpsy.setEnabled(True)
                    self.httpsn.setEnabled(True)
                    self.web = True
            
            def apacheYES(selected):
                if selected:
                    print('Yes apache')
                    self.nginxy.setEnabled(False)
                    self.nginxn.setEnabled(False)
                    self.nginxn.setChecked(True)
                    self.apaweb = True
                    self.nginweb = False
            
            def apacheNo(selected):
                if selected:
                    print('No Apache')
                    self.nginxy.setEnabled(True)
                    self.nginxn.setEnabled(True)
                    self.apaweb = False
            
            def nginxYES(selected):
                if selected:
                    print('Yes Nginx')
                    self.apachey.setEnabled(False)
                    self.apachen.setEnabled(False)
                    self.apachen.setChecked(True)
                    self.nginweb = True
                    self.apaweb = False
            
            def nginxNO(selected):
                if selected:
                    print('No Nginx')
                    self.apachey.setEnabled(True)
                    self.apachen.setEnabled(True)
                    self.nginweb = False
            
            def httpsYES(selected):
                if selected:
                    print('HTTPS Yes')
                    self.https = True
            
            def httpsNO(selected):
                if selected:
                    print('https no')
                    self.https = False
            
            def smbYES(selected):
                if selected:
                    print('SMB yes')
                    self.smb = True
            
            def smbNO(selected):
                if selected:
                    print('SMB no')
                    self.smb = False
            
            def sqlYES(selected):
                if selected:
                    print('SQL Yes')
                    self.sql = True
            
            def sqlNO(selected):
                if selected:
                    print('SQL No')
                    self.sql = False
            
            def rsncYES(selected):
                if selected:
                    print('rsnc Yes')
                    self.rsnc = True
            
            def rsncNO(selected):
                if selected:
                    print('rsnc No')
                    self.rsnc = False
            
            def rdpYES(selected):
                if selected:
                    print('RDP Yes')
                    self.rdp = True
            
            def rdpNO(selected):
                if selected:
                    print('RDP No')
                    self.rdp = False
            
            def quitButton():
                
                if variableCheck.is_file():
                    print('Cancelling configurations. Nothing has changed.')
                    self.close()
                    # main_commands = Main_start()
                    # main_commands.dialog_completed()
                else:
                    print('Closing program')
                    sys.exit(0)
            
            def confirmBTTN():
                if (self.ssh != '' and self.ftp != '' and self.proftpd != '' and self.vsftpd != '' and self.web != '' and self.apaweb != '' and self.nginweb != '' and self.https != '' and self.smb != '' and self.sql != '' and self.rsnc != '' and self.rdp != ''):
                    print('saving configurations\n')
                    print("ssh=" + str(self.ssh) + ", ftp=" + str(self.ftp) + ", proftpd=" + str(self.proftpd) + ", vsftpd=" + str(self.vsftpd) + ", web=" + str(self.web) + ", apaweb=" + str(self.apaweb) + ", nginweb=" + str(self.nginweb) + ", https=" + str(self.https) + ", smb=" + str(self.smb) + ", sql=" + str(self.sql) + ", rsnc=" + str(self.rsnc) + ", RDP=" + str(self.rdp))
                    
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
                    RESTART.setText("Configurations have been sucessfully saved.")
                    RESTART.setIcon(QMessageBox.Information)
                    RESTART.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    RESTART.setStandardButtons(QMessageBox.Close)
                    RESTART.exec_()
                    self.close()
                    beginMain = Main_start()
                    beginMain.show()
                else:
                    HEY = QMessageBox()
                    HEY.setWindowTitle('Hey! Listen!')
                    HEY.setText("Hey! You have not finished filling in all of the choices!")
                    HEY.setIcon(QMessageBox.Critical)
                    HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                    HEY.exec_()
            
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

        def begin(self):
            super(fconfStart, self).exec_()

    c = fconfStart()
    NewThread(c.begin, False, "CIDR_Configurations")



class Main_start(QMainWindow, Ui_MainWindow):
    # signalMain = pyqtSignal()
    
    def __init__(self, parent = None):
        super(Main_start, self).__init__(parent)
        print('Script Runner has started')
        self.setFixedSize(860, 675)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
        config_name2 = 'config.ini'
        if getattr(sys, 'frozen', False):
            application_Path2 = os.path.dirname(sys.executable)
        elif __file__:
            application_Path2 = os.path.dirname(__file__)
        config_path2 = os.path.join(application_Path2, config_name2)
        variableCheck2 = Path(config_path2)
        self.dialog_done = False
        self.mmfuncassign(variableCheck2)
    
    def mmfuncassign(self, configurations):
        print('Assigning functions')
        config = configparser.ConfigParser()
        config.read(configurations)
        self.header_title.setWordWrap(True)
        self.descriptions.setWordWrap(True)
        
        def quitButton():
            # log.info('Closing program')
            sys.exit(0)
        
        def display(i):
            """
            Sets the window Title and Descriptions upon OS selection. (The buttons that say 'Linux', 'Windows', and 'MacOS')
            """
            if i == 0:
                self.header_title.setText('Universal Commands')
                self.descriptions.setText(
                    'Description: These commands will work on most Operating Systems\nE.g. Windows, MacOS X, and Linux (Debian, Ubuntu, certain Arch distros)')
                self.stackedWidget.setCurrentIndex(i)
            elif i == 1:
                if uname()[0] == 'Windows' or DEBUG == True:
                    self.header_title.setText('Windows 10 Commands')
                    self.descriptions.setText(
                        'Description: These commands will work on the following Windows systems: 10, 8.x, and 7')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()
            elif i == 2:
                if uname()[0] == 'Linux' or DEBUG == True:
                    self.header_title.setText('Linux Commands')
                    self.descriptions.setText(
                        'Description: These commands will work on the following Linux systems: Debian based systems, Ubuntu, and Manjaro')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()
            elif i == 3:
                if uname()[0] == 'Darwin' or DEBUG == True:
                    self.header_title.setText('MacOS X Commands')
                    self.descriptions.setText(
                        'Description: These commands will ONLY work on MacOS X')
                    self.stackedWidget.setCurrentIndex(i)
                else:
                    wrongos()
        
        def light_darkMODE(i):
            """
            This function is not working currently. Need to find way of actually switching colorschemes.
            """
            print('Mode change')
            if i == 0:
                print('Dark Mode in development')
            elif i == 1:
                print('Light Mode in development')
        
        def showHOWTO():
            class showHowToUi(QDialog, Ui_How_To):
                def __init__(self, parent = None):
                    super(showHowToUi, self).__init__(parent)
                    self.setupUi(self)
                    self.setFixedSize(400, 305)
                    self.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            
            showHowToUi().exec_()
        
        def runCOMDESCRIPT():
            class showComDescript(QDialog, Ui_comDescript):
                def __init__(self, parent = None):
                    super(showComDescript, self).__init__(parent)
                    self.setupUi(self)
                    self.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))

            showComDescript().exec_()
        
        def runABOUTPROG():
            class showAboutProg(QDialog, Ui_About):
                def __init__(self, parent = None):
                    super(showAboutProg, self).__init__(parent)
                    self.setupUi(self)
                    self.setFixedSize(390, 282)
                    self.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            
            showAboutProg().exec_()
        
        def indev():
            INDEV = QMessageBox()
            INDEV.setWindowTitle('Hey! Listen!')
            INDEV.setText('Hey! This command is not yet complete and in development!')
            INDEV.setIcon(QMessageBox.Critical)
            INDEV.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            INDEV.exec_()
        
        def wrongos():
            WRONGOS = QMessageBox()
            WRONGOS.setWindowTitle('Hey! Listen!')
            WRONGOS.setText('Hey! These commands do not support this Operating System!')
            WRONGOS.setIcon(QMessageBox.Critical)
            WRONGOS.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            WRONGOS.exec_()
        
        def confirmation(com):
            CONFIRM = QMessageBox()
            CONFIRM.setWindowTitle('Hey! Listen!')
            CONFIRM.setText("Hey! Are you sure you want to do this?")
            CONFIRM.setIcon(QMessageBox.Critical)
            CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            x = CONFIRM.exec_()
            if x == QMessageBox.Yes:
                print('Starting...')
                com()
            elif x == QMessageBox.No:
                print('Cancelling...')
        
        display(0)
        
        self.uniCom.clicked.connect(lambda: display(0))
        self.winCom.clicked.connect(lambda: display(1))
        self.linCom.clicked.connect(lambda: display(2))
        self.macCom.clicked.connect(lambda: display(3))
        self.actionLight_Mode.triggered.connect(lambda: light_darkMODE(1))
        self.actionDark_Mode.triggered.connect(lambda: light_darkMODE(0))
        
        # Menubar Buttons
        self.actionHow_To_Use_Program.triggered.connect(lambda: showHOWTO())
        self.actionAbout_Creator.triggered.connect(lambda: runABOUTPROG())
        self.actionCommand_Descriptions.triggered.connect(lambda: runCOMDESCRIPT())
        self.actionChange_Configurations.triggered.connect(lambda: CIDR_Configurations())
        
        # # Universal Buttons
        # self.Updates_buttonUNI.clicked.connect(lambda: NewThread(update_os, False))
        # self.rmvprosoftbuttonUNI.clicked.connect(lambda: indev())
        # self.srchmedbuttonUNI.clicked.connect(lambda: NewThread(self.signalAssignment, False, "Search_Media", search_media))
        self.srchmedbuttonUNI.clicked.connect(lambda: Media_Search())
        
        """
        Attempt at making signal connect between hashRUN() classes begin() function. The use of signals should allow the functions to become multithreaded. As of right now this is currently not working. There are no "errors" as in it doesn't crash, but when I run it and try to click on the Hash Check button, nothing happens. This use of signals is used to prevent an error in pyqt5 that says something like "PyQt Timer could not be started..."
        """
        self.chkhashfile_buttonUNI.clicked.connect(lambda: Hash_Run())
        
        # Windows Main Menu Commands
        self.fwlbutton_2.clicked.connect(lambda: Configure_Firewall())
        # self.basicConfbutton_2.clicked.connect(
        #     lambda: NewThread(confirmation, False, basConf(config.get('Services', 'rdp'))))
        # self.rmvprosoftbutton_2.clicked.connect(lambda: NewThread(rmProSoft, False))
        self.enblBitLockerbutton.clicked.connect(lambda: BITLOCKER())
        # self.servicesConfButton_4.clicked.connect(
        #     lambda: NewThread(confirmation, False, Configure_Services(
        #         config.get(
        #             'Services',
        #             'ssh'),
        #         config.get(
        #             'Services',
        #             'smb'),
        #         config.get(
        #             'Services',
        #             'web'),
        #         config.get(
        #             'Services',
        #             'apaweb'),
        #         config.get(
        #             'Services',
        #             'nginweb'),
        #         config.get(
        #             'Services',
        #             'ftp'),
        #         config.get(
        #             'Services',
        #             'proftpd'),
        #         config.get(
        #             'Services',
        #             'vsftpd'))))
        # self.browserConf.clicked.connect(lambda: Configure_Browsers())
        # Windows User Group Commands
        self.WINUSRGRUBUTTON = [self.lsgruusrin_3, self.lsmemgru_3]
        for i in range(0, len(self.WINUSRGRUBUTTON)):
            self.WINUSRGRUBUTTON[i].clicked.connect(lambda: indev())
        
        self.adusrtosys_3.clicked.connect(lambda: addusr())
        self.rmvusrfrosys_3.clicked.connect(lambda: remusr())
        self.adgrutosys_3.clicked.connect(lambda: addgrutosys())
        self.rmvgrufrosys_3.clicked.connect(lambda: remgrufrosys())
        self.adusrtogru_3.clicked.connect(lambda: addusrtogru())
        self.rmvusrfrogru_3.clicked.connect(lambda: remusrfrogru())
        self.lslocausr_3.clicked.connect(lambda: lslocausrs())
        self.lslocagru_3.clicked.connect(lambda: lslocagrus())
        self.chngusrpas_3.clicked.connect(lambda: chngpasswdofall())
        #
        # # Linux Main Menu Commands
        # self.fwlbutton_3.clicked.connect(lambda: fwl())
        self.auditbutton_3.clicked.connect(lambda: alyn())
        # self.malrembutton_3.clicked.connect(lambda: malRem())  #
        # self.rmvprosoftbutton_3.clicked.connect(lambda: indev())  #
        # self.basicConfbutton_3.clicked.connect(lambda: indev())  #
        # self.servicesConfButton_2.clicked.connect(lambda: indev())  #

        # Linux User Group Commands
        self.LINUXUSRGRUBUTTONS = [self.adgrutosys_4, self.adusrtogru_4, self.adusrtosys_4,
                                   self.chngusrpas_4,self.lsgruusrin_4, self.lslocagru_4, self.lslocausr_4,
                                   self.lsmemgru_4,self.rmvgrufrosys_4, self.rmvusrfrogru_4,
                                   self.rmvusrfrosys_4]
        for i in range(0, 11):
            self.LINUXUSRGRUBUTTONS[i].clicked.connect(lambda: indev())  #
        
        # # MacOS Buttons
        self.MACBUTTONS = [self.rmvprosoftbutton_4, self.malrembutton_4, self.basicConfbutton_4,
                           self.servicesConfButton_3, self.adgrutosys_5, self.adusrtogru_5,
                           self.adusrtosys_5,self.chngusrpas_5, self.lsgruusrin_5, self.lslocagru_5,
                           self.lslocausr_5,self.lsmemgru_5,self.rmvgrufrosys_5, self.rmvusrfrogru_5, 
                           self.rmvusrfrosys_5]
        for i in range(0, 15):
            self.MACBUTTONS[i].clicked.connect(lambda: indev())
        
        self.quit_button_3.clicked.connect(quitButton)

    # def signalAssignment(self, com):
        # add way to save thread id to Current_Threads dictionary to be called later to stop the thread.
        # Assigns the function to the main signal
    #     print(threading.current_thread().getName())
    #     self.signalMain.connect(com)
    #     self.run_command()
        

    # def wait_for_command(self):
        # locks up main thread until the command dialog has closed
        # NOTE: This might interfere with commands that run in the background (Ex: Search for prohibited)
    #     while not self.dialog_done:
            # print(threading.get_ident())
    #         pass
    #     self.dialog_done = False
    
    # def dialog_completed(self):
    #     print('Dialog has stopped?')
    #     self.dialog_done = True

    # def run_command(self):
        # emits the main signal essentially calling the function assigned to the signal (This is all done within a new thread, seperate from the main thread)
    #     self.signalMain.emit()
    #     self.wait_for_command()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    config_name = 'config.ini'
    if getattr(sys, 'frozen', False):
        application_Path = os.path.dirname(sys.executable)
    elif __file__:
        application_Path = os.path.dirname(__file__)
    config_path = os.path.join(application_Path, config_name)
    print(config_path)
    variableCheck = Path(config_path)
    
    # Checks to make sure there is a config file. If not, then First time setup runs
    if variableCheck.is_file():
        config = configparser.ConfigParser()
        config.read(variableCheck)
        print('Configuration file has been loaded...')
        
        main = Main_start()
        main.show()
        sys.exit(app.exec_())
    else:
        print('Ello, you have some configurations to do!')
        CIDR_Configurations()
        sys.exit(app.exec_())
