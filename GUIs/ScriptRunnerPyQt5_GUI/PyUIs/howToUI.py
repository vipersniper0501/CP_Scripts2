# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'howTo.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_How_To(object):
    def setupUi(self, How_To):
        How_To.setObjectName("How_To")
        How_To.resize(400, 305)
        How_To.setStyleSheet("background-color: #212434;color: #CCD2E6;   \n"
"")
        self.textBrowser = QtWidgets.QTextBrowser(How_To)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 401, 251))
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(How_To)
        self.pushButton.setGeometry(QtCore.QRect(310, 266, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color:#414E6E;\n"
"color: #CCD2E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgba(139, 147, 178, .75);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(How_To)
        self.pushButton.clicked.connect(How_To.close)
        QtCore.QMetaObject.connectSlotsByName(How_To)

    def retranslateUi(self, How_To):
        _translate = QtCore.QCoreApplication.translate
        How_To.setWindowTitle(_translate("How_To", "Hey! This Tells You How To Use The Program!"))
        self.textBrowser.setHtml(_translate("How_To", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">+ --------------------------------------------------- +</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">|     H o w  T o  U s e  T h e  P r o g r a m     |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">+ --------------------------------------------------- +</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1.) Run as root</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2.) Choose command that you would like to use</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3.) Click it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4.) If needed, fill in required information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5.) Click Confirm/Run/Enter</span></p></body></html>"))
        self.pushButton.setText(_translate("How_To", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    How_To = QtWidgets.QDialog()
    ui = Ui_How_To()
    ui.setupUi(How_To)
    How_To.show()
    sys.exit(app.exec_())
