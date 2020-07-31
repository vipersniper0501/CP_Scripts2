# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUSR.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addUSR(object):
    def setupUi(self, addUSR):
        addUSR.setObjectName("addUSR")
        addUSR.resize(345, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addUSR.sizePolicy().hasHeightForWidth())
        addUSR.setSizePolicy(sizePolicy)
        addUSR.setStyleSheet("background-color: #212434\n"
"   ")
        self.label = QtWidgets.QLabel(addUSR)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setStyleSheet("color: #8B93B2;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addUSR)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.label_2.setStyleSheet("color: #8B93B2;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addUSR)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.label_3.setStyleSheet("color: #8B93B2;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(addUSR)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 131, 21))
        self.label_4.setStyleSheet("color: #8B93B2;")
        self.label_4.setObjectName("label_4")
        self.username_input = QtWidgets.QLineEdit(addUSR)
        self.username_input.setGeometry(QtCore.QRect(80, 10, 201, 20))
        self.username_input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.username_input.setObjectName("username_input")
        self.Password1_input = QtWidgets.QLineEdit(addUSR)
        self.Password1_input.setGeometry(QtCore.QRect(80, 40, 201, 20))
        self.Password1_input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.Password1_input.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Password1_input.setClearButtonEnabled(False)
        self.Password1_input.setObjectName("Password1_input")
        self.Password2_input = QtWidgets.QLineEdit(addUSR)
        self.Password2_input.setGeometry(QtCore.QRect(120, 70, 201, 20))
        self.Password2_input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.Password2_input.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Password2_input.setObjectName("Password2_input")
        self.admin_y = QtWidgets.QRadioButton(addUSR)
        self.admin_y.setGeometry(QtCore.QRect(150, 100, 41, 21))
        self.admin_y.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;\n"
"    ")
        self.admin_y.setObjectName("admin_y")
        self.admin_n = QtWidgets.QRadioButton(addUSR)
        self.admin_n.setGeometry(QtCore.QRect(240, 100, 41, 21))
        self.admin_n.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;border-radius: 10px;\n"
"    ")
        self.admin_n.setChecked(True)
        self.admin_n.setObjectName("admin_n")
        self.Confirm_button = QtWidgets.QPushButton(addUSR)
        self.Confirm_button.setGeometry(QtCore.QRect(10, 142, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Confirm_button.setFont(font)
        self.Confirm_button.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.Confirm_button.setObjectName("Confirm_button")
        self.Cancel_button = QtWidgets.QPushButton(addUSR)
        self.Cancel_button.setGeometry(QtCore.QRect(240, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_button.setFont(font)
        self.Cancel_button.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.Cancel_button.setObjectName("Cancel_button")

        self.retranslateUi(addUSR)
        QtCore.QMetaObject.connectSlotsByName(addUSR)

    def retranslateUi(self, addUSR):
        _translate = QtCore.QCoreApplication.translate
        addUSR.setWindowTitle(_translate("addUSR", "Add User To System"))
        self.label.setText(_translate("addUSR", "Username:"))
        self.label_2.setText(_translate("addUSR", "Password:"))
        self.label_3.setText(_translate("addUSR", "Confirm Password:"))
        self.label_4.setText(_translate("addUSR", "Is this user an Admin?"))
        self.admin_y.setText(_translate("addUSR", "Yes"))
        self.admin_n.setText(_translate("addUSR", "No"))
        self.Confirm_button.setText(_translate("addUSR", "Confirm"))
        self.Cancel_button.setText(_translate("addUSR", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addUSR = QtWidgets.QDialog()
    ui = Ui_addUSR()
    ui.setupUi(addUSR)
    addUSR.show()
    sys.exit(app.exec_())
