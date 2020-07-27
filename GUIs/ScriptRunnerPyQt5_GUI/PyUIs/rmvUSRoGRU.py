# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rmv_usr_o_gru.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rmvusrogru(object):
    def setupUi(self, rmvusrogru):
        rmvusrogru.setObjectName("rmvusrogru")
        rmvusrogru.resize(302, 334)
        rmvusrogru.setWindowTitle("")
        rmvusrogru.setStyleSheet("background-color: #212434\n"
"            ")
        self.Username_Input = QtWidgets.QLineEdit(rmvusrogru)
        self.Username_Input.setGeometry(QtCore.QRect(100, 250, 191, 21))
        self.Username_Input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.Username_Input.setObjectName("Username_Input")
        self.label2 = QtWidgets.QLabel(rmvusrogru)
        self.label2.setGeometry(QtCore.QRect(10, 250, 91, 21))
        self.label2.setStyleSheet("color: #8B93B2;")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label = QtWidgets.QLabel(rmvusrogru)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 21))
        self.label.setStyleSheet("color: #8B93B2;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Cancel_button = QtWidgets.QPushButton(rmvusrogru)
        self.Cancel_button.setGeometry(QtCore.QRect(200, 290, 91, 31))
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
        self.Confirm_button = QtWidgets.QPushButton(rmvusrogru)
        self.Confirm_button.setGeometry(QtCore.QRect(10, 290, 91, 31))
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
        self.listOFnames = QtWidgets.QListWidget(rmvusrogru)
        self.listOFnames.setGeometry(QtCore.QRect(10, 40, 281, 191))
        self.listOFnames.setStyleSheet("color: #8B93B2;")
        self.listOFnames.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listOFnames.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listOFnames.setObjectName("listOFnames")

        self.retranslateUi(rmvusrogru)
        QtCore.QMetaObject.connectSlotsByName(rmvusrogru)

    def retranslateUi(self, rmvusrogru):
        _translate = QtCore.QCoreApplication.translate
        self.Cancel_button.setText(_translate("rmvusrogru", "Cancel"))
        self.Confirm_button.setText(_translate("rmvusrogru", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rmvusrogru = QtWidgets.QDialog()
    ui = Ui_rmvusrogru()
    ui.setupUi(rmvusrogru)
    rmvusrogru.show()
    sys.exit(app.exec_())
