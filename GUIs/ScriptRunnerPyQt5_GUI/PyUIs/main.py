# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(862, 675)
        MainWindow.setStyleSheet("background-color: #212434\n"
"         ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 831, 121))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.header_title = QtWidgets.QLabel(self.header)
        self.header_title.setGeometry(QtCore.QRect(20, 0, 271, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.header_title.setFont(font)
        self.header_title.setStyleSheet("color: #8B93B2;")
        self.header_title.setText("")
        self.header_title.setObjectName("header_title")
        self.descriptions = QtWidgets.QLabel(self.header)
        self.descriptions.setGeometry(QtCore.QRect(360, 0, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptions.setFont(font)
        self.descriptions.setStyleSheet("color: #8B93B2;")
        self.descriptions.setObjectName("descriptions")
        self.quit_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button_3.setGeometry(QtCore.QRect(740, 590, 110, 50))
        self.quit_button_3.setMinimumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quit_button_3.setFont(font)
        self.quit_button_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.quit_button_3.setObjectName("quit_button_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 600, 311, 31))
        self.label.setStyleSheet("color: #CCD2E6")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 841, 442))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.macCom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.macCom.setMinimumSize(QtCore.QSize(170, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.macCom.setFont(font)
        self.macCom.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.macCom.setObjectName("macCom")
        self.gridLayout.addWidget(self.macCom, 6, 2, 1, 1)
        self.univPIC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.univPIC.setMinimumSize(QtCore.QSize(100, 100))
        self.univPIC.setPixmap(QtGui.QPixmap(":/Pictures/pictures/Universal-partner-icon(1).png\n"
"                                     "))
        self.univPIC.setObjectName("univPIC")
        self.gridLayout.addWidget(self.univPIC, 0, 0, 1, 1)
        self.linCom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.linCom.setMinimumSize(QtCore.QSize(170, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.linCom.setFont(font)
        self.linCom.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.linCom.setObjectName("linCom")
        self.gridLayout.addWidget(self.linCom, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.uniCom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.uniCom.setMinimumSize(QtCore.QSize(170, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.uniCom.setFont(font)
        self.uniCom.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.uniCom.setObjectName("uniCom")
        self.gridLayout.addWidget(self.uniCom, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 1, 1, 1)
        self.winCom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.winCom.setMinimumSize(QtCore.QSize(170, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.winCom.setFont(font)
        self.winCom.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.winCom.setObjectName("winCom")
        self.gridLayout.addWidget(self.winCom, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.winPIC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.winPIC.setMinimumSize(QtCore.QSize(100, 100))
        self.winPIC.setPixmap(QtGui.QPixmap(":/Pictures/pictures/windows-8-png-icon-7(1).png\n"
"                                     "))
        self.winPIC.setObjectName("winPIC")
        self.gridLayout.addWidget(self.winPIC, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 5, 2, 1, 1)
        self.macPIC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.macPIC.setMinimumSize(QtCore.QSize(100, 100))
        self.macPIC.setPixmap(QtGui.QPixmap(":/Pictures/pictures/MacOSx.png"))
        self.macPIC.setObjectName("macPIC")
        self.gridLayout.addWidget(self.macPIC, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 1, 1, 1)
        self.linPIC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.linPIC.setMinimumSize(QtCore.QSize(100, 100))
        self.linPIC.setPixmap(QtGui.QPixmap(":/Pictures/pictures/linuxICON(1).png"))
        self.linPIC.setObjectName("linPIC")
        self.gridLayout.addWidget(self.linPIC, 4, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(535, 440))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Universal_Page = QtWidgets.QWidget()
        self.Universal_Page.setObjectName("Universal_Page")
        self.frame = QtWidgets.QFrame(self.Universal_Page)
        self.frame.setGeometry(QtCore.QRect(0, 30, 541, 371))
        self.frame.setStyleSheet("background-color: #2E344A;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 528, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Updates_buttonUNI = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Updates_buttonUNI.setEnabled(True)
        self.Updates_buttonUNI.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Updates_buttonUNI.setFont(font)
        self.Updates_buttonUNI.setAcceptDrops(False)
        self.Updates_buttonUNI.setToolTip("")
        self.Updates_buttonUNI.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.Updates_buttonUNI.setCheckable(False)
        self.Updates_buttonUNI.setDefault(False)
        self.Updates_buttonUNI.setObjectName("Updates_buttonUNI")
        self.gridLayout_2.addWidget(self.Updates_buttonUNI, 0, 0, 1, 1)
        self.srchmedbuttonUNI = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.srchmedbuttonUNI.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.srchmedbuttonUNI.setFont(font)
        self.srchmedbuttonUNI.setToolTip("")
        self.srchmedbuttonUNI.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.srchmedbuttonUNI.setObjectName("srchmedbuttonUNI")
        self.gridLayout_2.addWidget(self.srchmedbuttonUNI, 0, 1, 1, 1)
        self.rmvprosoftbuttonUNI = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.rmvprosoftbuttonUNI.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rmvprosoftbuttonUNI.setFont(font)
        self.rmvprosoftbuttonUNI.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvprosoftbuttonUNI.setObjectName("rmvprosoftbuttonUNI")
        self.gridLayout_2.addWidget(self.rmvprosoftbuttonUNI, 1, 0, 1, 1)
        self.chkhashfile_buttonUNI = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.chkhashfile_buttonUNI.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.chkhashfile_buttonUNI.setFont(font)
        self.chkhashfile_buttonUNI.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.chkhashfile_buttonUNI.setObjectName("chkhashfile_buttonUNI")
        self.gridLayout_2.addWidget(self.chkhashfile_buttonUNI, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 511, 51))
        self.label_8.setStyleSheet("color: #8B93B2;")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.Universal_Page)
        self.Windows_Page = QtWidgets.QWidget()
        self.Windows_Page.setStyleSheet("")
        self.Windows_Page.setObjectName("Windows_Page")
        self.winTAB = QtWidgets.QTabWidget(self.Windows_Page)
        self.winTAB.setGeometry(QtCore.QRect(-10, 0, 581, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.winTAB.setFont(font)
        self.winTAB.setAutoFillBackground(False)
        self.winTAB.setStyleSheet("background-color: #2E344A;")
        self.winTAB.setObjectName("winTAB")
        self.windows_mainCOM = QtWidgets.QWidget()
        self.windows_mainCOM.setAutoFillBackground(False)
        self.windows_mainCOM.setObjectName("windows_mainCOM")
        self.label_13 = QtWidgets.QLabel(self.windows_mainCOM)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 451, 31))
        self.label_13.setStyleSheet("color: #8B93B2;")
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.windows_mainCOM)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(22, 0, 528, 171))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.basicConfbutton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.basicConfbutton_2.setMinimumSize(QtCore.QSize(260, 40))
        self.basicConfbutton_2.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.basicConfbutton_2.setFont(font)
        self.basicConfbutton_2.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.basicConfbutton_2.setObjectName("basicConfbutton_2")
        self.gridLayout_3.addWidget(self.basicConfbutton_2, 0, 1, 1, 1)
        self.rmvprosoftbutton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.rmvprosoftbutton_2.setMinimumSize(QtCore.QSize(260, 40))
        self.rmvprosoftbutton_2.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rmvprosoftbutton_2.setFont(font)
        self.rmvprosoftbutton_2.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvprosoftbutton_2.setObjectName("rmvprosoftbutton_2")
        self.gridLayout_3.addWidget(self.rmvprosoftbutton_2, 1, 0, 1, 1)
        self.enblBitLockerbutton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.enblBitLockerbutton.setMinimumSize(QtCore.QSize(260, 40))
        self.enblBitLockerbutton.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.enblBitLockerbutton.setFont(font)
        self.enblBitLockerbutton.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.enblBitLockerbutton.setObjectName("enblBitLockerbutton")
        self.gridLayout_3.addWidget(self.enblBitLockerbutton, 1, 1, 1, 1)
        self.fwlbutton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.fwlbutton_2.setMinimumSize(QtCore.QSize(260, 40))
        self.fwlbutton_2.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.fwlbutton_2.setFont(font)
        self.fwlbutton_2.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.fwlbutton_2.setObjectName("fwlbutton_2")
        self.gridLayout_3.addWidget(self.fwlbutton_2, 0, 0, 1, 1)
        self.servicesConfButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.servicesConfButton_4.setMinimumSize(QtCore.QSize(260, 40))
        self.servicesConfButton_4.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.servicesConfButton_4.setFont(font)
        self.servicesConfButton_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.servicesConfButton_4.setObjectName("servicesConfButton_4")
        self.gridLayout_3.addWidget(self.servicesConfButton_4, 2, 0, 1, 1)
        self.browserConf = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.browserConf.setMinimumSize(QtCore.QSize(260, 40))
        self.browserConf.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.browserConf.setFont(font)
        self.browserConf.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.browserConf.setObjectName("browserConf")
        self.gridLayout_3.addWidget(self.browserConf, 2, 1, 1, 1)
        self.winTAB.addTab(self.windows_mainCOM, "")
        self.windows_usrgruCOM = QtWidgets.QWidget()
        self.windows_usrgruCOM.setObjectName("windows_usrgruCOM")
        self.label_14 = QtWidgets.QLabel(self.windows_usrgruCOM)
        self.label_14.setGeometry(QtCore.QRect(20, 340, 471, 31))
        self.label_14.setStyleSheet("color: #8B93B2;")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.windows_usrgruCOM)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 0, 528, 341))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rmvusrfrosys_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.rmvusrfrosys_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrosys_3.setFont(font)
        self.rmvusrfrosys_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrosys_3.setObjectName("rmvusrfrosys_3")
        self.gridLayout_4.addWidget(self.rmvusrfrosys_3, 0, 1, 1, 1)
        self.rmvgrufrosys_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.rmvgrufrosys_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvgrufrosys_3.setFont(font)
        self.rmvgrufrosys_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvgrufrosys_3.setObjectName("rmvgrufrosys_3")
        self.gridLayout_4.addWidget(self.rmvgrufrosys_3, 1, 1, 1, 1)
        self.lsmemgru_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.lsmemgru_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsmemgru_3.setFont(font)
        self.lsmemgru_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsmemgru_3.setObjectName("lsmemgru_3")
        self.gridLayout_4.addWidget(self.lsmemgru_3, 4, 0, 1, 1)
        self.adusrtosys_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.adusrtosys_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtosys_3.setFont(font)
        self.adusrtosys_3.setAcceptDrops(False)
        self.adusrtosys_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtosys_3.setObjectName("adusrtosys_3")
        self.gridLayout_4.addWidget(self.adusrtosys_3, 0, 0, 1, 1)
        self.rmvusrfrogru_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.rmvusrfrogru_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrogru_3.setFont(font)
        self.rmvusrfrogru_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrogru_3.setObjectName("rmvusrfrogru_3")
        self.gridLayout_4.addWidget(self.rmvusrfrogru_3, 2, 1, 1, 1)
        self.lslocausr_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.lslocausr_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocausr_3.setFont(font)
        self.lslocausr_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocausr_3.setObjectName("lslocausr_3")
        self.gridLayout_4.addWidget(self.lslocausr_3, 3, 0, 1, 1)
        self.adusrtogru_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.adusrtogru_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtogru_3.setFont(font)
        self.adusrtogru_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtogru_3.setObjectName("adusrtogru_3")
        self.gridLayout_4.addWidget(self.adusrtogru_3, 2, 0, 1, 1)
        self.adgrutosys_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.adgrutosys_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adgrutosys_3.setFont(font)
        self.adgrutosys_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adgrutosys_3.setObjectName("adgrutosys_3")
        self.gridLayout_4.addWidget(self.adgrutosys_3, 1, 0, 1, 1)
        self.lslocagru_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.lslocagru_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocagru_3.setFont(font)
        self.lslocagru_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocagru_3.setObjectName("lslocagru_3")
        self.gridLayout_4.addWidget(self.lslocagru_3, 3, 1, 1, 1)
        self.lsgruusrin_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.lsgruusrin_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsgruusrin_3.setFont(font)
        self.lsgruusrin_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsgruusrin_3.setObjectName("lsgruusrin_3")
        self.gridLayout_4.addWidget(self.lsgruusrin_3, 4, 1, 1, 1)
        self.chngusrpas_3 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.chngusrpas_3.setMinimumSize(QtCore.QSize(260, 40))
        self.chngusrpas_3.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chngusrpas_3.setFont(font)
        self.chngusrpas_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.chngusrpas_3.setObjectName("chngusrpas_3")
        self.gridLayout_4.addWidget(self.chngusrpas_3, 5, 0, 1, 1)
        self.winTAB.addTab(self.windows_usrgruCOM, "")
        self.stackedWidget.addWidget(self.Windows_Page)
        self.Linux_Page = QtWidgets.QWidget()
        self.Linux_Page.setStyleSheet("")
        self.Linux_Page.setObjectName("Linux_Page")
        self.linTAB = QtWidgets.QTabWidget(self.Linux_Page)
        self.linTAB.setGeometry(QtCore.QRect(-10, 0, 581, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linTAB.setFont(font)
        self.linTAB.setStyleSheet("background-color: #2E344A;")
        self.linTAB.setObjectName("linTAB")
        self.linux_mainCOM = QtWidgets.QWidget()
        self.linux_mainCOM.setObjectName("linux_mainCOM")
        self.label_15 = QtWidgets.QLabel(self.linux_mainCOM)
        self.label_15.setGeometry(QtCore.QRect(20, 340, 511, 31))
        self.label_15.setStyleSheet("color: #8B93B2;")
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayoutWidget = QtWidgets.QWidget(self.linux_mainCOM)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 528, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rmvprosoftbutton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rmvprosoftbutton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvprosoftbutton_3.setFont(font)
        self.rmvprosoftbutton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvprosoftbutton_3.setObjectName("rmvprosoftbutton_3")
        self.gridLayout_5.addWidget(self.rmvprosoftbutton_3, 1, 0, 1, 1)
        self.fwlbutton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fwlbutton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fwlbutton_3.setFont(font)
        self.fwlbutton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.fwlbutton_3.setObjectName("fwlbutton_3")
        self.gridLayout_5.addWidget(self.fwlbutton_3, 0, 0, 1, 1)
        self.malrembutton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.malrembutton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malrembutton_3.setFont(font)
        self.malrembutton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.malrembutton_3.setObjectName("malrembutton_3")
        self.gridLayout_5.addWidget(self.malrembutton_3, 0, 1, 1, 1)
        self.basicConfbutton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.basicConfbutton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.basicConfbutton_3.setFont(font)
        self.basicConfbutton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.basicConfbutton_3.setObjectName("basicConfbutton_3")
        self.gridLayout_5.addWidget(self.basicConfbutton_3, 1, 1, 1, 1)
        self.auditbutton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.auditbutton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.auditbutton_3.setFont(font)
        self.auditbutton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.auditbutton_3.setObjectName("auditbutton_3")
        self.gridLayout_5.addWidget(self.auditbutton_3, 2, 0, 1, 1)
        self.servicesConfButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.servicesConfButton_2.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.servicesConfButton_2.setFont(font)
        self.servicesConfButton_2.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.servicesConfButton_2.setObjectName("servicesConfButton_2")
        self.gridLayout_5.addWidget(self.servicesConfButton_2, 2, 1, 1, 1)
        self.linTAB.addTab(self.linux_mainCOM, "")
        self.linux_usrgruCOM = QtWidgets.QWidget()
        self.linux_usrgruCOM.setObjectName("linux_usrgruCOM")
        self.label_16 = QtWidgets.QLabel(self.linux_usrgruCOM)
        self.label_16.setGeometry(QtCore.QRect(20, 340, 511, 31))
        self.label_16.setStyleSheet("color: #8B93B2;")
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.linux_usrgruCOM)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 0, 528, 321))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.adgrutosys_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.adgrutosys_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adgrutosys_4.setFont(font)
        self.adgrutosys_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adgrutosys_4.setObjectName("adgrutosys_4")
        self.gridLayout_6.addWidget(self.adgrutosys_4, 1, 0, 1, 1)
        self.adusrtogru_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.adusrtogru_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtogru_4.setFont(font)
        self.adusrtogru_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtogru_4.setObjectName("adusrtogru_4")
        self.gridLayout_6.addWidget(self.adusrtogru_4, 2, 0, 1, 1)
        self.rmvgrufrosys_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.rmvgrufrosys_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvgrufrosys_4.setFont(font)
        self.rmvgrufrosys_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvgrufrosys_4.setObjectName("rmvgrufrosys_4")
        self.gridLayout_6.addWidget(self.rmvgrufrosys_4, 1, 1, 1, 1)
        self.lslocagru_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.lslocagru_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocagru_4.setFont(font)
        self.lslocagru_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocagru_4.setObjectName("lslocagru_4")
        self.gridLayout_6.addWidget(self.lslocagru_4, 3, 1, 1, 1)
        self.rmvusrfrosys_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.rmvusrfrosys_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrosys_4.setFont(font)
        self.rmvusrfrosys_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrosys_4.setObjectName("rmvusrfrosys_4")
        self.gridLayout_6.addWidget(self.rmvusrfrosys_4, 0, 1, 1, 1)
        self.adusrtosys_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.adusrtosys_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtosys_4.setFont(font)
        self.adusrtosys_4.setAcceptDrops(False)
        self.adusrtosys_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtosys_4.setObjectName("adusrtosys_4")
        self.gridLayout_6.addWidget(self.adusrtosys_4, 0, 0, 1, 1)
        self.rmvusrfrogru_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.rmvusrfrogru_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrogru_4.setFont(font)
        self.rmvusrfrogru_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrogru_4.setObjectName("rmvusrfrogru_4")
        self.gridLayout_6.addWidget(self.rmvusrfrogru_4, 2, 1, 1, 1)
        self.lslocausr_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.lslocausr_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocausr_4.setFont(font)
        self.lslocausr_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocausr_4.setObjectName("lslocausr_4")
        self.gridLayout_6.addWidget(self.lslocausr_4, 3, 0, 1, 1)
        self.lsgruusrin_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.lsgruusrin_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsgruusrin_4.setFont(font)
        self.lsgruusrin_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsgruusrin_4.setObjectName("lsgruusrin_4")
        self.gridLayout_6.addWidget(self.lsgruusrin_4, 4, 1, 1, 1)
        self.lsmemgru_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.lsmemgru_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsmemgru_4.setFont(font)
        self.lsmemgru_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsmemgru_4.setObjectName("lsmemgru_4")
        self.gridLayout_6.addWidget(self.lsmemgru_4, 4, 0, 1, 1)
        self.chngusrpas_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.chngusrpas_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chngusrpas_4.setFont(font)
        self.chngusrpas_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.chngusrpas_4.setObjectName("chngusrpas_4")
        self.gridLayout_6.addWidget(self.chngusrpas_4, 5, 0, 1, 1)
        self.linTAB.addTab(self.linux_usrgruCOM, "")
        self.stackedWidget.addWidget(self.Linux_Page)
        self.MacOS_Page = QtWidgets.QWidget()
        self.MacOS_Page.setStyleSheet("")
        self.MacOS_Page.setObjectName("MacOS_Page")
        self.macTAB = QtWidgets.QTabWidget(self.MacOS_Page)
        self.macTAB.setGeometry(QtCore.QRect(-10, 0, 581, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.macTAB.setFont(font)
        self.macTAB.setStyleSheet("background-color: #2E344A;")
        self.macTAB.setObjectName("macTAB")
        self.mac_mainCOM = QtWidgets.QWidget()
        self.mac_mainCOM.setAutoFillBackground(False)
        self.mac_mainCOM.setObjectName("mac_mainCOM")
        self.label_17 = QtWidgets.QLabel(self.mac_mainCOM)
        self.label_17.setGeometry(QtCore.QRect(20, 340, 421, 31))
        self.label_17.setStyleSheet("color: #8B93B2;")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.mac_mainCOM)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(19, 0, 528, 141))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.rmvprosoftbutton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.rmvprosoftbutton_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvprosoftbutton_4.setFont(font)
        self.rmvprosoftbutton_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvprosoftbutton_4.setObjectName("rmvprosoftbutton_4")
        self.gridLayout_7.addWidget(self.rmvprosoftbutton_4, 0, 0, 1, 1)
        self.malrembutton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.malrembutton_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.malrembutton_4.setFont(font)
        self.malrembutton_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.malrembutton_4.setObjectName("malrembutton_4")
        self.gridLayout_7.addWidget(self.malrembutton_4, 0, 1, 1, 1)
        self.servicesConfButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.servicesConfButton_3.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.servicesConfButton_3.setFont(font)
        self.servicesConfButton_3.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.servicesConfButton_3.setObjectName("servicesConfButton_3")
        self.gridLayout_7.addWidget(self.servicesConfButton_3, 1, 0, 1, 1)
        self.basicConfbutton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.basicConfbutton_4.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.basicConfbutton_4.setFont(font)
        self.basicConfbutton_4.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.basicConfbutton_4.setObjectName("basicConfbutton_4")
        self.gridLayout_7.addWidget(self.basicConfbutton_4, 1, 1, 1, 1)
        self.macTAB.addTab(self.mac_mainCOM, "")
        self.mac_usrgruCOM = QtWidgets.QWidget()
        self.mac_usrgruCOM.setObjectName("mac_usrgruCOM")
        self.label_18 = QtWidgets.QLabel(self.mac_usrgruCOM)
        self.label_18.setGeometry(QtCore.QRect(20, 340, 421, 31))
        self.label_18.setStyleSheet("color: #8B93B2;")
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.mac_usrgruCOM)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(20, 0, 528, 321))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.rmvusrfrosys_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.rmvusrfrosys_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrosys_5.setFont(font)
        self.rmvusrfrosys_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrosys_5.setObjectName("rmvusrfrosys_5")
        self.gridLayout_8.addWidget(self.rmvusrfrosys_5, 0, 1, 1, 1)
        self.adgrutosys_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.adgrutosys_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adgrutosys_5.setFont(font)
        self.adgrutosys_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adgrutosys_5.setObjectName("adgrutosys_5")
        self.gridLayout_8.addWidget(self.adgrutosys_5, 1, 0, 1, 1)
        self.lsmemgru_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.lsmemgru_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsmemgru_5.setFont(font)
        self.lsmemgru_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsmemgru_5.setObjectName("lsmemgru_5")
        self.gridLayout_8.addWidget(self.lsmemgru_5, 4, 0, 1, 1)
        self.adusrtogru_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.adusrtogru_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtogru_5.setFont(font)
        self.adusrtogru_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtogru_5.setObjectName("adusrtogru_5")
        self.gridLayout_8.addWidget(self.adusrtogru_5, 2, 0, 1, 1)
        self.lslocausr_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.lslocausr_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocausr_5.setFont(font)
        self.lslocausr_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocausr_5.setObjectName("lslocausr_5")
        self.gridLayout_8.addWidget(self.lslocausr_5, 3, 0, 1, 1)
        self.lslocagru_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.lslocagru_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lslocagru_5.setFont(font)
        self.lslocagru_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lslocagru_5.setObjectName("lslocagru_5")
        self.gridLayout_8.addWidget(self.lslocagru_5, 3, 1, 1, 1)
        self.lsgruusrin_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.lsgruusrin_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lsgruusrin_5.setFont(font)
        self.lsgruusrin_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.lsgruusrin_5.setObjectName("lsgruusrin_5")
        self.gridLayout_8.addWidget(self.lsgruusrin_5, 4, 1, 1, 1)
        self.rmvgrufrosys_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.rmvgrufrosys_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvgrufrosys_5.setFont(font)
        self.rmvgrufrosys_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvgrufrosys_5.setObjectName("rmvgrufrosys_5")
        self.gridLayout_8.addWidget(self.rmvgrufrosys_5, 1, 1, 1, 1)
        self.rmvusrfrogru_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.rmvusrfrogru_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rmvusrfrogru_5.setFont(font)
        self.rmvusrfrogru_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.rmvusrfrogru_5.setObjectName("rmvusrfrogru_5")
        self.gridLayout_8.addWidget(self.rmvusrfrogru_5, 2, 1, 1, 1)
        self.adusrtosys_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.adusrtosys_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.adusrtosys_5.setFont(font)
        self.adusrtosys_5.setAcceptDrops(False)
        self.adusrtosys_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.adusrtosys_5.setObjectName("adusrtosys_5")
        self.gridLayout_8.addWidget(self.adusrtosys_5, 0, 0, 1, 1)
        self.chngusrpas_5 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.chngusrpas_5.setMinimumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chngusrpas_5.setFont(font)
        self.chngusrpas_5.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.chngusrpas_5.setObjectName("chngusrpas_5")
        self.gridLayout_8.addWidget(self.chngusrpas_5, 5, 0, 1, 1)
        self.macTAB.addTab(self.mac_usrgruCOM, "")
        self.stackedWidget.addWidget(self.MacOS_Page)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color: #8B93B2; background-color: #2E344A;")
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("")
        self.menuHelp.setObjectName("menuHelp")
        self.menuLighting_Mode = QtWidgets.QMenu(self.menubar)
        self.menuLighting_Mode.setObjectName("menuLighting_Mode")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_Creator = QtWidgets.QAction(MainWindow)
        self.actionAbout_Creator.setObjectName("actionAbout_Creator")
        self.actionHow_To_Use_Program = QtWidgets.QAction(MainWindow)
        self.actionHow_To_Use_Program.setObjectName("actionHow_To_Use_Program")
        self.actionLight_Mode = QtWidgets.QAction(MainWindow)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionCommand_Descriptions = QtWidgets.QAction(MainWindow)
        self.actionCommand_Descriptions.setObjectName("actionCommand_Descriptions")
        self.actionChange_Configurations = QtWidgets.QAction(MainWindow)
        self.actionChange_Configurations.setObjectName("actionChange_Configurations")
        self.menuHelp.addAction(self.actionAbout_Creator)
        self.menuHelp.addAction(self.actionHow_To_Use_Program)
        self.menuHelp.addAction(self.actionCommand_Descriptions)
        self.menuHelp.addAction(self.actionChange_Configurations)
        self.menuLighting_Mode.addAction(self.actionLight_Mode)
        self.menuLighting_Mode.addAction(self.actionDark_Mode)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLighting_Mode.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.winTAB.setCurrentIndex(0)
        self.linTAB.setCurrentIndex(0)
        self.macTAB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.uniCom, self.winCom)
        MainWindow.setTabOrder(self.winCom, self.linCom)
        MainWindow.setTabOrder(self.linCom, self.macCom)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apple CIDR"))
        self.descriptions.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.quit_button_3.setText(_translate("MainWindow", "Quit"))
        self.quit_button_3.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.label.setText(_translate("MainWindow", "Note: any command with a * is not completed yet"))
        self.macCom.setText(_translate("MainWindow", "MacOS Only Commands"))
        self.univPIC.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/images/Universal-partner-icon(1).png\"/></p></body></html>"))
        self.linCom.setText(_translate("MainWindow", "Linux Only Commands"))
        self.uniCom.setText(_translate("MainWindow", "Universal Commands"))
        self.winCom.setText(_translate("MainWindow", "Windows Only Commands"))
        self.winPIC.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/images/windows-8-png-icon-7(1).png\"/></p></body></html>"))
        self.macPIC.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/images/MacOSx.png\"/></p></body></html>"))
        self.linPIC.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/images/linuxICON(1).png\"/></p></body></html>"))
        self.Updates_buttonUNI.setText(_translate("MainWindow", "Update System"))
        self.srchmedbuttonUNI.setText(_translate("MainWindow", "Search For Prohibited Media"))
        self.rmvprosoftbuttonUNI.setText(_translate("MainWindow", "Remove Prohibited Software*"))
        self.chkhashfile_buttonUNI.setText(_translate("MainWindow", "Check the Hash of a File"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>All\n"
"                                             Commands here will\n"
"                                             work across all\n"
"                                             Operating Systems</p></body></html>\n"
"                                         "))
        self.label_13.setText(_translate("MainWindow", "All Commands here will work on Windows 10"))
        self.basicConfbutton_2.setText(_translate("MainWindow", "Security Policies Configurations"))
        self.rmvprosoftbutton_2.setText(_translate("MainWindow", "Remove Prohibited Software*"))
        self.enblBitLockerbutton.setText(_translate("MainWindow", "Enable BitLocker"))
        self.fwlbutton_2.setText(_translate("MainWindow", "Windows Firewall Settings"))
        self.servicesConfButton_4.setText(_translate("MainWindow", "Services Configurations*"))
        self.browserConf.setText(_translate("MainWindow", "Configure Browser Settings [Firefox]"))
        self.winTAB.setTabText(self.winTAB.indexOf(self.windows_mainCOM), _translate("MainWindow", "Main Commands"))
        self.label_14.setText(_translate("MainWindow", "All Commands here will work on Windows 10"))
        self.rmvusrfrosys_3.setText(_translate("MainWindow", "Remove User From System"))
        self.rmvgrufrosys_3.setText(_translate("MainWindow", "Remove Group from System"))
        self.lsmemgru_3.setText(_translate("MainWindow", "List Members of Group*"))
        self.adusrtosys_3.setText(_translate("MainWindow", "Add User to System"))
        self.rmvusrfrogru_3.setText(_translate("MainWindow", "Remove User from Group*"))
        self.lslocausr_3.setText(_translate("MainWindow", "List Local Users"))
        self.adusrtogru_3.setText(_translate("MainWindow", "Add User to Group*"))
        self.adgrutosys_3.setText(_translate("MainWindow", "Add Group to System*"))
        self.lslocagru_3.setText(_translate("MainWindow", "List Local Groups"))
        self.lsgruusrin_3.setText(_translate("MainWindow", "List Groups an User is in*"))
        self.chngusrpas_3.setText(_translate("MainWindow", "Change all User Passwords at Once"))
        self.winTAB.setTabText(self.winTAB.indexOf(self.windows_usrgruCOM), _translate("MainWindow", "User / Group Settings"))
        self.label_15.setText(_translate("MainWindow", "All Commands here will work on Debian/Ubuntu/Manjaro Linux distributions"))
        self.rmvprosoftbutton_3.setText(_translate("MainWindow", "Remove Prohibited Software*"))
        self.fwlbutton_3.setText(_translate("MainWindow", "Linux Firewall Settings"))
        self.malrembutton_3.setText(_translate("MainWindow", "Malware Removal"))
        self.basicConfbutton_3.setText(_translate("MainWindow", "Basic Configurations"))
        self.auditbutton_3.setText(_translate("MainWindow", "Audit System"))
        self.servicesConfButton_2.setText(_translate("MainWindow", "Services Configurations"))
        self.linTAB.setTabText(self.linTAB.indexOf(self.linux_mainCOM), _translate("MainWindow", "Main Commands"))
        self.label_16.setText(_translate("MainWindow", "All Commands here will work on Debian/Ubuntu/Manjaro Linux distributions"))
        self.adgrutosys_4.setText(_translate("MainWindow", "Add Group to System*"))
        self.adusrtogru_4.setText(_translate("MainWindow", "Add User to Group*"))
        self.rmvgrufrosys_4.setText(_translate("MainWindow", "Remove Group from System*"))
        self.lslocagru_4.setText(_translate("MainWindow", "List Local Groups*"))
        self.rmvusrfrosys_4.setText(_translate("MainWindow", "Remove User From System*"))
        self.adusrtosys_4.setText(_translate("MainWindow", "Add User to System*"))
        self.rmvusrfrogru_4.setText(_translate("MainWindow", "Remove User from Group*"))
        self.lslocausr_4.setText(_translate("MainWindow", "List Local Users*"))
        self.lsgruusrin_4.setText(_translate("MainWindow", "List Groups an User is in*"))
        self.lsmemgru_4.setText(_translate("MainWindow", "List Members of Group*"))
        self.chngusrpas_4.setText(_translate("MainWindow", "Change all User Passwords at Once*"))
        self.linTAB.setTabText(self.linTAB.indexOf(self.linux_usrgruCOM), _translate("MainWindow", "User / Group Settings"))
        self.label_17.setText(_translate("MainWindow", "All Commands here will work on MacOS X"))
        self.rmvprosoftbutton_4.setText(_translate("MainWindow", "Remove Prohibited Software*"))
        self.malrembutton_4.setText(_translate("MainWindow", "Malware Removal*"))
        self.servicesConfButton_3.setText(_translate("MainWindow", "Services Configurations*"))
        self.basicConfbutton_4.setText(_translate("MainWindow", "Basic Configurations*"))
        self.macTAB.setTabText(self.macTAB.indexOf(self.mac_mainCOM), _translate("MainWindow", "Main Commands"))
        self.label_18.setText(_translate("MainWindow", "All Commands here will work on MacOS X"))
        self.rmvusrfrosys_5.setText(_translate("MainWindow", "Remove User From System*"))
        self.adgrutosys_5.setText(_translate("MainWindow", "Add Group to System*"))
        self.lsmemgru_5.setText(_translate("MainWindow", "List Members of Group*"))
        self.adusrtogru_5.setText(_translate("MainWindow", "Add User to Group*"))
        self.lslocausr_5.setText(_translate("MainWindow", "List Local Users*"))
        self.lslocagru_5.setText(_translate("MainWindow", "List Local Groups*"))
        self.lsgruusrin_5.setText(_translate("MainWindow", "List Groups an User is in*"))
        self.rmvgrufrosys_5.setText(_translate("MainWindow", "Remove Group from System*"))
        self.rmvusrfrogru_5.setText(_translate("MainWindow", "Remove User from Group*"))
        self.adusrtosys_5.setText(_translate("MainWindow", "Add User to System*"))
        self.chngusrpas_5.setText(_translate("MainWindow", "Change all User Passwords at Once*"))
        self.macTAB.setTabText(self.macTAB.indexOf(self.mac_usrgruCOM), _translate("MainWindow", "User / Group Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLighting_Mode.setTitle(_translate("MainWindow", "Light/Dark Mode Settings"))
        self.actionAbout_Creator.setText(_translate("MainWindow", "About Creators and the Program"))
        self.actionHow_To_Use_Program.setText(_translate("MainWindow", "How To Use Program"))
        self.actionLight_Mode.setText(_translate("MainWindow", "Light Mode"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionCommand_Descriptions.setText(_translate("MainWindow", "Command Descriptions"))
        self.actionChange_Configurations.setText(_translate("MainWindow", "Change Configurations"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
