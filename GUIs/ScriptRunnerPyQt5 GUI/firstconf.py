# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstConf.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstConf(object):
    def setupUi(self, firstConf):
        firstConf.setObjectName("firstConf")
        firstConf.resize(723, 448)
        firstConf.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.102273 rgba(0, 105, 173, 255), stop:0.926136 rgba(0, 173, 155, 255))")
        self.quit_buttonConf = QtWidgets.QPushButton(firstConf)
        self.quit_buttonConf.setGeometry(QtCore.QRect(610, 390, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_buttonConf.setFont(font)
        self.quit_buttonConf.setStyleSheet("color: black;")
        self.quit_buttonConf.setObjectName("quit_buttonConf")
        self.confirmbtn = QtWidgets.QPushButton(firstConf)
        self.confirmbtn.setGeometry(QtCore.QRect(510, 390, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmbtn.setFont(font)
        self.confirmbtn.setStyleSheet("color: black;")
        self.confirmbtn.setDefault(True)
        self.confirmbtn.setObjectName("confirmbtn")
        self.fconflbl = QtWidgets.QLabel(firstConf)
        self.fconflbl.setGeometry(QtCore.QRect(20, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        self.fconflbl.setFont(font)
        self.fconflbl.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;color: black;")
        self.fconflbl.setObjectName("fconflbl")
        self.fconfqalbl = QtWidgets.QLabel(firstConf)
        self.fconfqalbl.setGeometry(QtCore.QRect(20, 70, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fconfqalbl.setFont(font)
        self.fconfqalbl.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.fconfqalbl.setAlignment(QtCore.Qt.AlignCenter)
        self.fconfqalbl.setObjectName("fconfqalbl")
        self.frame = QtWidgets.QFrame(firstConf)
        self.frame.setGeometry(QtCore.QRect(50, 120, 191, 41))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sshy = QtWidgets.QRadioButton(self.frame)
        self.sshy.setGeometry(QtCore.QRect(90, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sshy.setFont(font)
        self.sshy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.sshy.setObjectName("sshy")
        self.sshn = QtWidgets.QRadioButton(self.frame)
        self.sshn.setGeometry(QtCore.QRect(140, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sshn.setFont(font)
        self.sshn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.sshn.setObjectName("sshn")
        self.ssh = QtWidgets.QLabel(self.frame)
        self.ssh.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ssh.setFont(font)
        self.ssh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ssh.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.ssh.setAlignment(QtCore.Qt.AlignCenter)
        self.ssh.setObjectName("ssh")
        self.ftpfrm = QtWidgets.QFrame(firstConf)
        self.ftpfrm.setGeometry(QtCore.QRect(50, 180, 211, 101))
        self.ftpfrm.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.ftpfrm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ftpfrm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ftpfrm.setObjectName("ftpfrm")
        self.vsftpdynfrm = QtWidgets.QFrame(self.ftpfrm)
        self.vsftpdynfrm.setGeometry(QtCore.QRect(30, 70, 171, 21))
        self.vsftpdynfrm.setStyleSheet("border: none")
        self.vsftpdynfrm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vsftpdynfrm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vsftpdynfrm.setObjectName("vsftpdynfrm")
        self.vsftpdn = QtWidgets.QRadioButton(self.vsftpdynfrm)
        self.vsftpdn.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vsftpdn.setFont(font)
        self.vsftpdn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.vsftpdn.setObjectName("vsftpdn")
        self.vsftpdy = QtWidgets.QRadioButton(self.vsftpdynfrm)
        self.vsftpdy.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vsftpdy.setFont(font)
        self.vsftpdy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.vsftpdy.setObjectName("vsftpdy")
        self.vsfptd = QtWidgets.QLabel(self.vsftpdynfrm)
        self.vsfptd.setGeometry(QtCore.QRect(0, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vsfptd.setFont(font)
        self.vsfptd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.vsfptd.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.vsfptd.setAlignment(QtCore.Qt.AlignCenter)
        self.vsfptd.setObjectName("vsfptd")
        self.proftpdynfrm = QtWidgets.QFrame(self.ftpfrm)
        self.proftpdynfrm.setGeometry(QtCore.QRect(30, 40, 171, 21))
        self.proftpdynfrm.setStyleSheet("border: none")
        self.proftpdynfrm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.proftpdynfrm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.proftpdynfrm.setObjectName("proftpdynfrm")
        self.proftpdn = QtWidgets.QRadioButton(self.proftpdynfrm)
        self.proftpdn.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.proftpdn.setFont(font)
        self.proftpdn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.proftpdn.setObjectName("proftpdn")
        self.proftpdy = QtWidgets.QRadioButton(self.proftpdynfrm)
        self.proftpdy.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.proftpdy.setFont(font)
        self.proftpdy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.proftpdy.setObjectName("proftpdy")
        self.proftpd = QtWidgets.QLabel(self.proftpdynfrm)
        self.proftpd.setGeometry(QtCore.QRect(0, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.proftpd.setFont(font)
        self.proftpd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.proftpd.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.proftpd.setAlignment(QtCore.Qt.AlignCenter)
        self.proftpd.setObjectName("proftpd")
        self.ftpynfrm = QtWidgets.QFrame(self.ftpfrm)
        self.ftpynfrm.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.ftpynfrm.setStyleSheet("border: none")
        self.ftpynfrm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ftpynfrm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ftpynfrm.setObjectName("ftpynfrm")
        self.ftpn = QtWidgets.QRadioButton(self.ftpynfrm)
        self.ftpn.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ftpn.setFont(font)
        self.ftpn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.ftpn.setObjectName("ftpn")
        self.ftpy = QtWidgets.QRadioButton(self.ftpynfrm)
        self.ftpy.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ftpy.setFont(font)
        self.ftpy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.ftpy.setObjectName("ftpy")
        self.ftp = QtWidgets.QLabel(self.ftpynfrm)
        self.ftp.setGeometry(QtCore.QRect(0, 0, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ftp.setFont(font)
        self.ftp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ftp.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.ftp.setAlignment(QtCore.Qt.AlignCenter)
        self.ftp.setObjectName("ftp")
        self.frame_2 = QtWidgets.QFrame(firstConf)
        self.frame_2.setGeometry(QtCore.QRect(50, 290, 291, 131))
        self.frame_2.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 271, 21))
        self.frame_6.setStyleSheet("border: none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.weby = QtWidgets.QRadioButton(self.frame_6)
        self.weby.setGeometry(QtCore.QRect(180, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weby.setFont(font)
        self.weby.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.weby.setObjectName("weby")
        self.web = QtWidgets.QLabel(self.frame_6)
        self.web.setGeometry(QtCore.QRect(0, 0, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.web.setFont(font)
        self.web.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.web.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.web.setAlignment(QtCore.Qt.AlignCenter)
        self.web.setObjectName("web")
        self.webn = QtWidgets.QRadioButton(self.frame_6)
        self.webn.setGeometry(QtCore.QRect(230, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.webn.setFont(font)
        self.webn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.webn.setObjectName("webn")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(60, 40, 171, 21))
        self.frame_7.setStyleSheet("border: none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.apache = QtWidgets.QLabel(self.frame_7)
        self.apache.setGeometry(QtCore.QRect(0, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apache.setFont(font)
        self.apache.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.apache.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.apache.setAlignment(QtCore.Qt.AlignCenter)
        self.apache.setObjectName("apache")
        self.apachey = QtWidgets.QRadioButton(self.frame_7)
        self.apachey.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apachey.setFont(font)
        self.apachey.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.apachey.setObjectName("apachey")
        self.apachen = QtWidgets.QRadioButton(self.frame_7)
        self.apachen.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apachen.setFont(font)
        self.apachen.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.apachen.setObjectName("apachen")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setGeometry(QtCore.QRect(60, 70, 171, 21))
        self.frame_8.setStyleSheet("border: none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.nginxy = QtWidgets.QRadioButton(self.frame_8)
        self.nginxy.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nginxy.setFont(font)
        self.nginxy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.nginxy.setObjectName("nginxy")
        self.nginxn = QtWidgets.QRadioButton(self.frame_8)
        self.nginxn.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nginxn.setFont(font)
        self.nginxn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.nginxn.setObjectName("nginxn")
        self.nginx = QtWidgets.QLabel(self.frame_8)
        self.nginx.setGeometry(QtCore.QRect(0, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nginx.setFont(font)
        self.nginx.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nginx.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.nginx.setAlignment(QtCore.Qt.AlignCenter)
        self.nginx.setObjectName("nginx")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setGeometry(QtCore.QRect(60, 100, 171, 21))
        self.frame_9.setStyleSheet("border: none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.https = QtWidgets.QLabel(self.frame_9)
        self.https.setGeometry(QtCore.QRect(0, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.https.setFont(font)
        self.https.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.https.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.https.setAlignment(QtCore.Qt.AlignCenter)
        self.https.setObjectName("https")
        self.httpsn = QtWidgets.QRadioButton(self.frame_9)
        self.httpsn.setGeometry(QtCore.QRect(130, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.httpsn.setFont(font)
        self.httpsn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.httpsn.setObjectName("httpsn")
        self.httpsy = QtWidgets.QRadioButton(self.frame_9)
        self.httpsy.setGeometry(QtCore.QRect(80, 0, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.httpsy.setFont(font)
        self.httpsy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.httpsy.setObjectName("httpsy")
        self.frame_3 = QtWidgets.QFrame(firstConf)
        self.frame_3.setGeometry(QtCore.QRect(410, 120, 191, 41))
        self.frame_3.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.smb = QtWidgets.QLabel(self.frame_3)
        self.smb.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.smb.setFont(font)
        self.smb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.smb.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.smb.setAlignment(QtCore.Qt.AlignCenter)
        self.smb.setObjectName("smb")
        self.smbn = QtWidgets.QRadioButton(self.frame_3)
        self.smbn.setGeometry(QtCore.QRect(140, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.smbn.setFont(font)
        self.smbn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.smbn.setObjectName("smbn")
        self.smby = QtWidgets.QRadioButton(self.frame_3)
        self.smby.setGeometry(QtCore.QRect(90, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.smby.setFont(font)
        self.smby.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.smby.setObjectName("smby")
        self.frame_4 = QtWidgets.QFrame(firstConf)
        self.frame_4.setGeometry(QtCore.QRect(410, 170, 191, 41))
        self.frame_4.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.sqln = QtWidgets.QRadioButton(self.frame_4)
        self.sqln.setGeometry(QtCore.QRect(140, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sqln.setFont(font)
        self.sqln.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.sqln.setObjectName("sqln")
        self.sqly = QtWidgets.QRadioButton(self.frame_4)
        self.sqly.setGeometry(QtCore.QRect(90, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sqly.setFont(font)
        self.sqly.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.sqly.setObjectName("sqly")
        self.sql = QtWidgets.QLabel(self.frame_4)
        self.sql.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sql.setFont(font)
        self.sql.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sql.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.sql.setAlignment(QtCore.Qt.AlignCenter)
        self.sql.setObjectName("sql")
        self.frame_5 = QtWidgets.QFrame(firstConf)
        self.frame_5.setGeometry(QtCore.QRect(410, 230, 191, 41))
        self.frame_5.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.rsync = QtWidgets.QLabel(self.frame_5)
        self.rsync.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsync.setFont(font)
        self.rsync.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rsync.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rsync.setAlignment(QtCore.Qt.AlignCenter)
        self.rsync.setObjectName("rsync")
        self.rsyncn = QtWidgets.QRadioButton(self.frame_5)
        self.rsyncn.setGeometry(QtCore.QRect(140, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsyncn.setFont(font)
        self.rsyncn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rsyncn.setObjectName("rsyncn")
        self.rsyncy = QtWidgets.QRadioButton(self.frame_5)
        self.rsyncy.setGeometry(QtCore.QRect(90, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsyncy.setFont(font)
        self.rsyncy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rsyncy.setObjectName("rsyncy")
        self.frame_10 = QtWidgets.QFrame(firstConf)
        self.frame_10.setGeometry(QtCore.QRect(410, 290, 251, 41))
        self.frame_10.setStyleSheet("border: 2px solid;\n"
"border-width: 3px;\n"
"background: transparent;\n"
"border-radius: 10px; \n"
"color: black;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.rdp = QtWidgets.QLabel(self.frame_10)
        self.rdp.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdp.setFont(font)
        self.rdp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdp.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rdp.setAlignment(QtCore.Qt.AlignCenter)
        self.rdp.setObjectName("rdp")
        self.rdpn = QtWidgets.QRadioButton(self.frame_10)
        self.rdpn.setGeometry(QtCore.QRect(200, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdpn.setFont(font)
        self.rdpn.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rdpn.setObjectName("rdpn")
        self.rdpy = QtWidgets.QRadioButton(self.frame_10)
        self.rdpy.setGeometry(QtCore.QRect(150, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdpy.setFont(font)
        self.rdpy.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.rdpy.setObjectName("rdpy")

        self.retranslateUi(firstConf)
        QtCore.QMetaObject.connectSlotsByName(firstConf)

    def retranslateUi(self, firstConf):
        _translate = QtCore.QCoreApplication.translate
        firstConf.setWindowTitle(_translate("firstConf", "First Time Configuration"))
        self.quit_buttonConf.setText(_translate("firstConf", "Quit"))
        self.confirmbtn.setText(_translate("firstConf", "Confirm"))
        self.fconflbl.setText(_translate("firstConf", "First Time Configurations"))
        self.fconfqalbl.setText(_translate("firstConf", "Does the system require the following services?"))
        self.sshy.setText(_translate("firstConf", "Yes"))
        self.sshn.setText(_translate("firstConf", "No"))
        self.ssh.setText(_translate("firstConf", "SSH"))
        self.vsftpdn.setText(_translate("firstConf", "No"))
        self.vsftpdy.setText(_translate("firstConf", "Yes"))
        self.vsfptd.setText(_translate("firstConf", "Vsftpd"))
        self.proftpdn.setText(_translate("firstConf", "No"))
        self.proftpdy.setText(_translate("firstConf", "Yes"))
        self.proftpd.setText(_translate("firstConf", "Proftpd"))
        self.ftpn.setText(_translate("firstConf", "No"))
        self.ftpy.setText(_translate("firstConf", "Yes"))
        self.ftp.setText(_translate("firstConf", "FTP"))
        self.weby.setText(_translate("firstConf", "Yes"))
        self.web.setText(_translate("firstConf", "Webserver Functionality"))
        self.webn.setText(_translate("firstConf", "No"))
        self.apache.setText(_translate("firstConf", "Apache2"))
        self.apachey.setText(_translate("firstConf", "Yes"))
        self.apachen.setText(_translate("firstConf", "No"))
        self.nginxy.setText(_translate("firstConf", "Yes"))
        self.nginxn.setText(_translate("firstConf", "No"))
        self.nginx.setText(_translate("firstConf", "Nginx"))
        self.https.setText(_translate("firstConf", "HTTPS"))
        self.httpsn.setText(_translate("firstConf", "No"))
        self.httpsy.setText(_translate("firstConf", "Yes"))
        self.smb.setText(_translate("firstConf", "SMB"))
        self.smbn.setText(_translate("firstConf", "No"))
        self.smby.setText(_translate("firstConf", "Yes"))
        self.sqln.setText(_translate("firstConf", "No"))
        self.sqly.setText(_translate("firstConf", "Yes"))
        self.sql.setText(_translate("firstConf", "SQL"))
        self.rsync.setText(_translate("firstConf", "Rsync"))
        self.rsyncn.setText(_translate("firstConf", "No"))
        self.rsyncy.setText(_translate("firstConf", "Yes"))
        self.rdp.setText(_translate("firstConf", "Remote Desktop"))
        self.rdpn.setText(_translate("firstConf", "No"))
        self.rdpy.setText(_translate("firstConf", "Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstConf = QtWidgets.QDialog()
    ui = Ui_firstConf()
    ui.setupUi(firstConf)
    firstConf.show()
    sys.exit(app.exec_())
