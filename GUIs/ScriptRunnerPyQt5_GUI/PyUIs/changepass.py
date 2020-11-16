# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePass.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chngpass(object):
    def setupUi(self, chngpass):
        chngpass.setObjectName("chngpass")
        chngpass.resize(428, 146)
        chngpass.setStyleSheet("background-color: #212434\n"
"            ")
        self.passwd = QtWidgets.QLineEdit(chngpass)
        self.passwd.setGeometry(QtCore.QRect(110, 10, 291, 20))
        self.passwd.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.passwd.setObjectName("passwd")
        self.label = QtWidgets.QLabel(chngpass)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label.setStyleSheet("color: #8B93B2;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(chngpass)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.label_3.setStyleSheet("color: #8B93B2;")
        self.label_3.setObjectName("label_3")
        self.pass_verify = QtWidgets.QLineEdit(chngpass)
        self.pass_verify.setGeometry(QtCore.QRect(110, 40, 291, 20))
        self.pass_verify.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.pass_verify.setObjectName("pass_verify")
        self.chngpass_button = QtWidgets.QPushButton(chngpass)
        self.chngpass_button.setGeometry(QtCore.QRect(110, 80, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.chngpass_button.setFont(font)
        self.chngpass_button.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.chngpass_button.setObjectName("chngpass_button")

        self.retranslateUi(chngpass)
        QtCore.QMetaObject.connectSlotsByName(chngpass)

    def retranslateUi(self, chngpass):
        _translate = QtCore.QCoreApplication.translate
        chngpass.setWindowTitle(_translate("chngpass", "Change Password for All Users"))
        self.label.setText(_translate("chngpass", "Password:"))
        self.label_3.setText(_translate("chngpass", "Confirm Password:"))
        self.chngpass_button.setText(_translate("chngpass", "Change Password for All Users"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chngpass = QtWidgets.QDialog()
    ui = Ui_chngpass()
    ui.setupUi(chngpass)
    chngpass.show()
    sys.exit(app.exec_())
