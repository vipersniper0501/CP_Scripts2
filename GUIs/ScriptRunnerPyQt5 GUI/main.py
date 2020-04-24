# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 427)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.102273 rgba(0, 105, 173, 255), stop:0.926136 rgba(0, 173, 155, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menulist = QtWidgets.QTabWidget(self.centralwidget)
        self.menulist.setGeometry(QtCore.QRect(0, 0, 611, 411))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menulist.setFont(font)
        self.menulist.setStyleSheet("color: white;")
        self.menulist.setTabPosition(QtWidgets.QTabWidget.North)
        self.menulist.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.menulist.setIconSize(QtCore.QSize(12, 12))
        self.menulist.setTabBarAutoHide(False)
        self.menulist.setObjectName("menulist")
        self.mmtab = QtWidgets.QWidget()
        self.mmtab.setObjectName("mmtab")
        self.fwlbutton = QtWidgets.QPushButton(self.mmtab)
        self.fwlbutton.setGeometry(QtCore.QRect(50, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fwlbutton.setFont(font)
        self.fwlbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.fwlbutton.setObjectName("fwlbutton")
        self.auditbutton = QtWidgets.QPushButton(self.mmtab)
        self.auditbutton.setGeometry(QtCore.QRect(50, 210, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.auditbutton.setFont(font)
        self.auditbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.auditbutton.setObjectName("auditbutton")
        self.servsetbutton = QtWidgets.QPushButton(self.mmtab)
        self.servsetbutton.setGeometry(QtCore.QRect(330, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.servsetbutton.setFont(font)
        self.servsetbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.servsetbutton.setObjectName("servsetbutton")
        self.rmvprosoftbutton = QtWidgets.QPushButton(self.mmtab)
        self.rmvprosoftbutton.setGeometry(QtCore.QRect(50, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rmvprosoftbutton.setFont(font)
        self.rmvprosoftbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.rmvprosoftbutton.setObjectName("rmvprosoftbutton")
        self.malrembutton = QtWidgets.QPushButton(self.mmtab)
        self.malrembutton.setGeometry(QtCore.QRect(330, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.malrembutton.setFont(font)
        self.malrembutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.malrembutton.setObjectName("malrembutton")
        self.srchmedbutton = QtWidgets.QPushButton(self.mmtab)
        self.srchmedbutton.setGeometry(QtCore.QRect(330, 210, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.srchmedbutton.setFont(font)
        self.srchmedbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.srchmedbutton.setObjectName("srchmedbutton")
        self.quit_button = QtWidgets.QPushButton(self.mmtab)
        self.quit_button.setGeometry(QtCore.QRect(490, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_button.setFont(font)
        self.quit_button.setStyleSheet("color: black;")
        self.quit_button.setObjectName("quit_button")
        self.mmlbl = QtWidgets.QLabel(self.mmtab)
        self.mmlbl.setGeometry(QtCore.QRect(230, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        self.mmlbl.setFont(font)
        self.mmlbl.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.mmlbl.setObjectName("mmlbl")
        self.Updates_button = QtWidgets.QPushButton(self.mmtab)
        self.Updates_button.setEnabled(True)
        self.Updates_button.setGeometry(QtCore.QRect(50, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Updates_button.setFont(font)
        self.Updates_button.setAcceptDrops(False)
        self.Updates_button.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.Updates_button.setCheckable(False)
        self.Updates_button.setDefault(False)
        self.Updates_button.setObjectName("Updates_button")
        self.basicConfbutton = QtWidgets.QPushButton(self.mmtab)
        self.basicConfbutton.setGeometry(QtCore.QRect(330, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.basicConfbutton.setFont(font)
        self.basicConfbutton.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.basicConfbutton.setObjectName("basicConfbutton")
        self.menulist.addTab(self.mmtab, "")
        self.usrgrutab = QtWidgets.QWidget()
        self.usrgrutab.setObjectName("usrgrutab")
        self.usrgrulbl = QtWidgets.QLabel(self.usrgrutab)
        self.usrgrulbl.setGeometry(QtCore.QRect(180, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        self.usrgrulbl.setFont(font)
        self.usrgrulbl.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px; color: black;")
        self.usrgrulbl.setObjectName("usrgrulbl")
        self.lslocausr = QtWidgets.QPushButton(self.usrgrutab)
        self.lslocausr.setGeometry(QtCore.QRect(50, 210, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lslocausr.setFont(font)
        self.lslocausr.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.lslocausr.setObjectName("lslocausr")
        self.rmvusrfrogru = QtWidgets.QPushButton(self.usrgrutab)
        self.rmvusrfrogru.setGeometry(QtCore.QRect(330, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rmvusrfrogru.setFont(font)
        self.rmvusrfrogru.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.rmvusrfrogru.setObjectName("rmvusrfrogru")
        self.adgrutosys = QtWidgets.QPushButton(self.usrgrutab)
        self.adgrutosys.setGeometry(QtCore.QRect(50, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adgrutosys.setFont(font)
        self.adgrutosys.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.adgrutosys.setObjectName("adgrutosys")
        self.rmvgrufrosys = QtWidgets.QPushButton(self.usrgrutab)
        self.rmvgrufrosys.setGeometry(QtCore.QRect(330, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rmvgrufrosys.setFont(font)
        self.rmvgrufrosys.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.rmvgrufrosys.setObjectName("rmvgrufrosys")
        self.quit_button_3 = QtWidgets.QPushButton(self.usrgrutab)
        self.quit_button_3.setGeometry(QtCore.QRect(490, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_button_3.setFont(font)
        self.quit_button_3.setStyleSheet("color: black;")
        self.quit_button_3.setObjectName("quit_button_3")
        self.adusrtosys = QtWidgets.QPushButton(self.usrgrutab)
        self.adusrtosys.setGeometry(QtCore.QRect(50, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adusrtosys.setFont(font)
        self.adusrtosys.setAcceptDrops(False)
        self.adusrtosys.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.adusrtosys.setObjectName("adusrtosys")
        self.lslocagru = QtWidgets.QPushButton(self.usrgrutab)
        self.lslocagru.setGeometry(QtCore.QRect(330, 210, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lslocagru.setFont(font)
        self.lslocagru.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.lslocagru.setObjectName("lslocagru")
        self.adusrtogru = QtWidgets.QPushButton(self.usrgrutab)
        self.adusrtogru.setGeometry(QtCore.QRect(50, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adusrtogru.setFont(font)
        self.adusrtogru.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.adusrtogru.setObjectName("adusrtogru")
        self.rmvusrfrosys = QtWidgets.QPushButton(self.usrgrutab)
        self.rmvusrfrosys.setGeometry(QtCore.QRect(330, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rmvusrfrosys.setFont(font)
        self.rmvusrfrosys.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.rmvusrfrosys.setObjectName("rmvusrfrosys")
        self.lsmemgru = QtWidgets.QPushButton(self.usrgrutab)
        self.lsmemgru.setGeometry(QtCore.QRect(50, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lsmemgru.setFont(font)
        self.lsmemgru.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.lsmemgru.setObjectName("lsmemgru")
        self.lsgruusrin = QtWidgets.QPushButton(self.usrgrutab)
        self.lsgruusrin.setGeometry(QtCore.QRect(330, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lsgruusrin.setFont(font)
        self.lsgruusrin.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.lsgruusrin.setObjectName("lsgruusrin")
        self.chngusrpas = QtWidgets.QPushButton(self.usrgrutab)
        self.chngusrpas.setGeometry(QtCore.QRect(50, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chngusrpas.setFont(font)
        self.chngusrpas.setStyleSheet("border: 2px solid;\n"
"border-color: grey;\n"
"border-style: outset;\n"
"border-width: 2.5px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;\n"
"color: black;\n"
"")
        self.chngusrpas.setObjectName("chngusrpas")
        self.menulist.addTab(self.usrgrutab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("border: 2px solid;\n"
"border-width: 1px;\n"
"background-color: lightblue;\n"
"border-radius: 10px;")
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuChange_Configurations = QtWidgets.QMenu(self.menubar)
        self.menuChange_Configurations.setObjectName("menuChange_Configurations")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_Creator = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionAbout_Creator.setFont(font)
        self.actionAbout_Creator.setObjectName("actionAbout_Creator")
        self.actionHow_To_Use = QtWidgets.QAction(MainWindow)
        self.actionHow_To_Use.setObjectName("actionHow_To_Use")
        self.menuAbout.addAction(self.actionAbout_Creator)
        self.menuAbout.addAction(self.actionHow_To_Use)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuChange_Configurations.menuAction())

        self.retranslateUi(MainWindow)
        self.menulist.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apple CIDR Script Runner"))
        self.fwlbutton.setText(_translate("MainWindow", "Firewall Settings"))
        self.auditbutton.setText(_translate("MainWindow", "Audit System"))
        self.servsetbutton.setText(_translate("MainWindow", "Services Settings"))
        self.rmvprosoftbutton.setText(_translate("MainWindow", "Remove Prohibited Software"))
        self.malrembutton.setText(_translate("MainWindow", "Malware Removal"))
        self.srchmedbutton.setText(_translate("MainWindow", "Search For Prohibited Media"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
        self.quit_button.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.mmlbl.setText(_translate("MainWindow", "Main Menu"))
        self.Updates_button.setText(_translate("MainWindow", "Updates"))
        self.basicConfbutton.setText(_translate("MainWindow", "Basic Configurations"))
        self.menulist.setTabText(self.menulist.indexOf(self.mmtab), _translate("MainWindow", "Main Menu"))
        self.usrgrulbl.setText(_translate("MainWindow", "User / Group Settings"))
        self.lslocausr.setText(_translate("MainWindow", "List Local Users"))
        self.rmvusrfrogru.setText(_translate("MainWindow", "Remove User from Group"))
        self.adgrutosys.setText(_translate("MainWindow", "Add Group to System"))
        self.rmvgrufrosys.setText(_translate("MainWindow", "Remove Group from System"))
        self.quit_button_3.setText(_translate("MainWindow", "Quit"))
        self.quit_button_3.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.adusrtosys.setText(_translate("MainWindow", "Add User to System"))
        self.lslocagru.setText(_translate("MainWindow", "List Local Groups"))
        self.adusrtogru.setText(_translate("MainWindow", "Add User to Group"))
        self.rmvusrfrosys.setText(_translate("MainWindow", "Remove User From System"))
        self.lsmemgru.setText(_translate("MainWindow", "List Members of Group"))
        self.lsgruusrin.setText(_translate("MainWindow", "List Groups an User is in"))
        self.chngusrpas.setText(_translate("MainWindow", "Change all Users Passwords at Once"))
        self.menulist.setTabText(self.menulist.indexOf(self.usrgrutab), _translate("MainWindow", "User / Group Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuChange_Configurations.setTitle(_translate("MainWindow", "Change Configurations"))
        self.actionAbout_Creator.setText(_translate("MainWindow", "About Creator"))
        self.actionHow_To_Use.setText(_translate("MainWindow", "How To Use"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
