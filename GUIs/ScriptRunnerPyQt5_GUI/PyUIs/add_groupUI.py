# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Group.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Group_UIClass(object):
    def setupUi(self, Add_Group_UIClass):
        Add_Group_UIClass.setObjectName("Add_Group_UIClass")
        Add_Group_UIClass.resize(292, 94)
        Add_Group_UIClass.setStyleSheet("background-color: #212434\n"
"   ")
        self.Confirm_button = QtWidgets.QPushButton(Add_Group_UIClass)
        self.Confirm_button.setGeometry(QtCore.QRect(10, 50, 91, 31))
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
        self.Cancel_button = QtWidgets.QPushButton(Add_Group_UIClass)
        self.Cancel_button.setGeometry(QtCore.QRect(190, 50, 91, 31))
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
        self.group_name_input = QtWidgets.QLineEdit(Add_Group_UIClass)
        self.group_name_input.setGeometry(QtCore.QRect(100, 10, 181, 20))
        self.group_name_input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.group_name_input.setObjectName("group_name_input")
        self.label = QtWidgets.QLabel(Add_Group_UIClass)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setStyleSheet("color: #8B93B2;")
        self.label.setObjectName("label")

        self.retranslateUi(Add_Group_UIClass)
        QtCore.QMetaObject.connectSlotsByName(Add_Group_UIClass)

    def retranslateUi(self, Add_Group_UIClass):
        _translate = QtCore.QCoreApplication.translate
        Add_Group_UIClass.setWindowTitle(_translate("Add_Group_UIClass", "Add Group To System"))
        self.Confirm_button.setText(_translate("Add_Group_UIClass", "Confirm"))
        self.Cancel_button.setText(_translate("Add_Group_UIClass", "Cancel"))
        self.label.setText(_translate("Add_Group_UIClass", "Group Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Group_UIClass = QtWidgets.QDialog()
    ui = Ui_Add_Group_UIClass()
    ui.setupUi(Add_Group_UIClass)
    Add_Group_UIClass.show()
    sys.exit(app.exec_())
