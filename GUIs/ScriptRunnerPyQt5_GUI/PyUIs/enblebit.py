# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitlockerENBL.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bitlockerGUI(object):
    def setupUi(self, bitlockerGUI):
        bitlockerGUI.setObjectName("bitlockerGUI")
        bitlockerGUI.resize(483, 323)
        bitlockerGUI.setStyleSheet("background-color: #212434\n"
                                   "")
        self.frame = QtWidgets.QFrame(bitlockerGUI)
        self.frame.setGeometry(QtCore.QRect(15, 70, 160, 241))
        self.frame.setStyleSheet("border: 2px solid;\n"
                                 "border-width: 3px;\n"
                                 "background: transparent;\n"
                                 "border-radius: 10px; \n"
                                 "color: black;\n"
                                 "padding: 3px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 140, 15))
        self.label.setStyleSheet("color: #8B93B2;border: none;")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.radioButton.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.radioButton_2.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.radioButton_3.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.radioButton_4.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 150, 121, 21))
        self.radioButton_5.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 180, 121, 21))
        self.radioButton_6.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 210, 121, 21))
        self.radioButton_7.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;")
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.enblBIT = QtWidgets.QPushButton(bitlockerGUI)
        self.enblBIT.setGeometry(QtCore.QRect(194, 70, 281, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.enblBIT.setFont(font)
        self.enblBIT.setStyleSheet("background-color: #414E6E;color: #CCD2E6;")
        self.enblBIT.setObjectName("enblBIT")
        self.label_2 = QtWidgets.QLabel(bitlockerGUI)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_2.setStyleSheet("color: #8B93B2;")
        self.label_2.setObjectName("label_2")
        self.encrypPASS = QtWidgets.QLineEdit(bitlockerGUI)
        self.encrypPASS.setGeometry(QtCore.QRect(150, 10, 311, 20))
        self.encrypPASS.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.encrypPASS.setObjectName("encrypPASS")
        self.frame_2 = QtWidgets.QFrame(bitlockerGUI)
        self.frame_2.setGeometry(QtCore.QRect(185, 210, 291, 61))
        self.frame_2.setStyleSheet("border: 2px solid;\n"
                                   "border-width: 3px;\n"
                                   "background: transparent;\n"
                                   "border-radius: 10px; \n"
                                   "color: black;\n"
                                   "padding: 3px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #8B93B2;border: none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #8B93B2;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.cancelbutton = QtWidgets.QPushButton(bitlockerGUI)
        self.cancelbutton.setGeometry(QtCore.QRect(320, 280, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancelbutton.setFont(font)
        self.cancelbutton.setStyleSheet("background-color: #414E6E;color: #CCD2E6;")
        self.cancelbutton.setObjectName("cancelbutton")
        self.encrypPASS_2 = QtWidgets.QLineEdit(bitlockerGUI)
        self.encrypPASS_2.setGeometry(QtCore.QRect(150, 40, 311, 20))
        self.encrypPASS_2.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.encrypPASS_2.setObjectName("encrypPASS_2")
        self.label_5 = QtWidgets.QLabel(bitlockerGUI)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.label_5.setStyleSheet("color: #8B93B2;")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(bitlockerGUI)
        QtCore.QMetaObject.connectSlotsByName(bitlockerGUI)
        bitlockerGUI.setTabOrder(self.encrypPASS, self.encrypPASS_2)
        bitlockerGUI.setTabOrder(self.encrypPASS_2, self.radioButton)
        bitlockerGUI.setTabOrder(self.radioButton, self.radioButton_2)
        bitlockerGUI.setTabOrder(self.radioButton_2, self.radioButton_3)
        bitlockerGUI.setTabOrder(self.radioButton_3, self.radioButton_4)
        bitlockerGUI.setTabOrder(self.radioButton_4, self.radioButton_5)
        bitlockerGUI.setTabOrder(self.radioButton_5, self.radioButton_6)
        bitlockerGUI.setTabOrder(self.radioButton_6, self.radioButton_7)
        bitlockerGUI.setTabOrder(self.radioButton_7, self.enblBIT)
        bitlockerGUI.setTabOrder(self.enblBIT, self.cancelbutton)

    def retranslateUi(self, bitlockerGUI):
        _translate = QtCore.QCoreApplication.translate
        bitlockerGUI.setWindowTitle(_translate("bitlockerGUI", "Enable Bitlocker"))
        self.label.setText(_translate("bitlockerGUI", "Current available drive(s):"))
        self.enblBIT.setText(_translate("bitlockerGUI", "Enable BitLocker"))
        self.label_2.setText(_translate("bitlockerGUI", "Encryption Password:"))
        self.label_3.setText(_translate("bitlockerGUI", "Encryption Status:"))
        self.cancelbutton.setText(_translate("bitlockerGUI", "Cancel"))
        self.label_5.setText(_translate("bitlockerGUI", "Verify Encryption Password:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bitlockerGUI = QtWidgets.QDialog()
    ui = Ui_bitlockerGUI()
    ui.setupUi(bitlockerGUI)
    bitlockerGUI.show()
    sys.exit(app.exec_())
