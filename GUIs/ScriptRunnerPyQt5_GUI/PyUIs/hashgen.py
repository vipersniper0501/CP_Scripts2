# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hashGEN.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hashGEN(object):
    def setupUi(self, hashGEN):
        hashGEN.setObjectName("hashGEN")
        hashGEN.resize(431, 179)
        hashGEN.setStyleSheet("background-color: #212434\n"
"            ")
        self.fpath = QtWidgets.QLineEdit(hashGEN)
        self.fpath.setGeometry(QtCore.QRect(70, 10, 281, 20))
        self.fpath.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.fpath.setObjectName("fpath")
        self.label = QtWidgets.QLabel(hashGEN)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label.setStyleSheet("color: #8B93B2;")
        self.label.setObjectName("label")
        self.genhash = QtWidgets.QPushButton(hashGEN)
        self.genhash.setGeometry(QtCore.QRect(110, 50, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.genhash.setFont(font)
        self.genhash.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.genhash.setObjectName("genhash")
        self.frame = QtWidgets.QFrame(hashGEN)
        self.frame.setGeometry(QtCore.QRect(10, 40, 81, 131))
        self.frame.setStyleSheet("border: 2px solid;\n"
"                    border-width: 3px;\n"
"                    background: transparent;\n"
"                    border-radius: 10px;\n"
"                    color: black;\n"
"                ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.HashLbl = QtWidgets.QLabel(self.frame)
        self.HashLbl.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.HashLbl.setStyleSheet("color: #8B93B2;border: none;")
        self.HashLbl.setObjectName("HashLbl")
        self.MD5radio = QtWidgets.QRadioButton(self.frame)
        self.MD5radio.setGeometry(QtCore.QRect(10, 30, 62, 14))
        self.MD5radio.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;\n"
"                    ")
        self.MD5radio.setChecked(True)
        self.MD5radio.setObjectName("MD5radio")
        self.SHA512radio = QtWidgets.QRadioButton(self.frame)
        self.SHA512radio.setGeometry(QtCore.QRect(10, 110, 62, 14))
        self.SHA512radio.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.SHA512radio.setObjectName("SHA512radio")
        self.SHA1radio = QtWidgets.QRadioButton(self.frame)
        self.SHA1radio.setGeometry(QtCore.QRect(10, 50, 62, 14))
        self.SHA1radio.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.SHA1radio.setObjectName("SHA1radio")
        self.SHA256radio = QtWidgets.QRadioButton(self.frame)
        self.SHA256radio.setGeometry(QtCore.QRect(10, 70, 62, 14))
        self.SHA256radio.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.SHA256radio.setObjectName("SHA256radio")
        self.SHA384radio = QtWidgets.QRadioButton(self.frame)
        self.SHA384radio.setGeometry(QtCore.QRect(10, 90, 62, 14))
        self.SHA384radio.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.SHA384radio.setObjectName("SHA384radio")
        self.browsebutton = QtWidgets.QPushButton(hashGEN)
        self.browsebutton.setGeometry(QtCore.QRect(360, 10, 61, 21))
        self.browsebutton.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.browsebutton.setObjectName("browsebutton")

        self.retranslateUi(hashGEN)
        QtCore.QMetaObject.connectSlotsByName(hashGEN)

    def retranslateUi(self, hashGEN):
        _translate = QtCore.QCoreApplication.translate
        hashGEN.setWindowTitle(_translate("hashGEN", "File Hash Generator"))
        self.label.setText(_translate("hashGEN", "File Path:"))
        self.genhash.setText(_translate("hashGEN", "Generate Hash"))
        self.HashLbl.setText(_translate("hashGEN", "Hash Type:"))
        self.MD5radio.setText(_translate("hashGEN", "MD5"))
        self.SHA512radio.setText(_translate("hashGEN", "SHA 512"))
        self.SHA1radio.setText(_translate("hashGEN", "SHA 1"))
        self.SHA256radio.setText(_translate("hashGEN", "SHA 256"))
        self.SHA384radio.setText(_translate("hashGEN", "SHA 384"))
        self.browsebutton.setText(_translate("hashGEN", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hashGEN = QtWidgets.QDialog()
    ui = Ui_hashGEN()
    ui.setupUi(hashGEN)
    hashGEN.show()
    sys.exit(app.exec_())
