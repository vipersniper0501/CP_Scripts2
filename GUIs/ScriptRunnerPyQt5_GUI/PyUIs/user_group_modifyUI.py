# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_group_modify.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_group_list_modifiers(object):
    def setupUi(self, user_group_list_modifiers):
        user_group_list_modifiers.setObjectName("user_group_list_modifiers")
        user_group_list_modifiers.resize(790, 419)
        user_group_list_modifiers.setWindowTitle("")
        user_group_list_modifiers.setStyleSheet("background-color: #212434\n"
"            ")
        self.listWidget = QtWidgets.QListWidget(user_group_list_modifiers)
        self.listWidget.setGeometry(QtCore.QRect(220, 40, 261, 361))
        self.listWidget.setStyleSheet("color: #8B93B2;")
        self.listWidget.setObjectName("listWidget")
        self.list_label1 = QtWidgets.QLabel(user_group_list_modifiers)
        self.list_label1.setGeometry(QtCore.QRect(220, 10, 261, 21))
        self.list_label1.setStyleSheet("color: #8B93B2;")
        self.list_label1.setText("")
        self.list_label1.setObjectName("list_label1")
        self.list_label2 = QtWidgets.QLabel(user_group_list_modifiers)
        self.list_label2.setGeometry(QtCore.QRect(510, 10, 261, 21))
        self.list_label2.setStyleSheet("color: #8B93B2;")
        self.list_label2.setText("")
        self.list_label2.setObjectName("list_label2")
        self.Title_label = QtWidgets.QLabel(user_group_list_modifiers)
        self.Title_label.setGeometry(QtCore.QRect(10, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: #8B93B2;")
        self.Title_label.setText("")
        self.Title_label.setObjectName("Title_label")
        self.Confirm_button = QtWidgets.QPushButton(user_group_list_modifiers)
        self.Confirm_button.setGeometry(QtCore.QRect(10, 370, 91, 31))
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
        self.Cancel_button_2 = QtWidgets.QPushButton(user_group_list_modifiers)
        self.Cancel_button_2.setGeometry(QtCore.QRect(120, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_button_2.setFont(font)
        self.Cancel_button_2.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.Cancel_button_2.setObjectName("Cancel_button_2")
        self.Name_Input = QtWidgets.QLineEdit(user_group_list_modifiers)
        self.Name_Input.setGeometry(QtCore.QRect(10, 170, 191, 21))
        self.Name_Input.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.Name_Input.setObjectName("Name_Input")
        self.Name_Input_Label1 = QtWidgets.QLabel(user_group_list_modifiers)
        self.Name_Input_Label1.setGeometry(QtCore.QRect(10, 130, 191, 21))
        self.Name_Input_Label1.setStyleSheet("color: #8B93B2;")
        self.Name_Input_Label1.setText("")
        self.Name_Input_Label1.setObjectName("Name_Input_Label1")
        self.Name_Input_Label2 = QtWidgets.QLabel(user_group_list_modifiers)
        self.Name_Input_Label2.setGeometry(QtCore.QRect(10, 220, 191, 21))
        self.Name_Input_Label2.setStyleSheet("color: #8B93B2;")
        self.Name_Input_Label2.setText("")
        self.Name_Input_Label2.setObjectName("Name_Input_Label2")
        self.Name_Input_2 = QtWidgets.QLineEdit(user_group_list_modifiers)
        self.Name_Input_2.setGeometry(QtCore.QRect(10, 260, 191, 21))
        self.Name_Input_2.setStyleSheet("background-color: #414E6E;color: #CCD2E6;border: none;")
        self.Name_Input_2.setObjectName("Name_Input_2")
        self.treeWidget = QtWidgets.QTreeWidget(user_group_list_modifiers)
        self.treeWidget.setGeometry(QtCore.QRect(500, 40, 271, 361))
        self.treeWidget.setStyleSheet("color: #8B93B2;")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget.headerItem().setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(0, brush)

        self.retranslateUi(user_group_list_modifiers)
        QtCore.QMetaObject.connectSlotsByName(user_group_list_modifiers)

    def retranslateUi(self, user_group_list_modifiers):
        _translate = QtCore.QCoreApplication.translate
        self.Confirm_button.setText(_translate("user_group_list_modifiers", "Confirm"))
        self.Cancel_button_2.setText(_translate("user_group_list_modifiers", "Cancel"))
        self.treeWidget.headerItem().setText(0, _translate("user_group_list_modifiers", "Groups"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_group_list_modifiers = QtWidgets.QDialog()
    ui = Ui_user_group_list_modifiers()
    ui.setupUi(user_group_list_modifiers)
    user_group_list_modifiers.show()
    sys.exit(app.exec_())
