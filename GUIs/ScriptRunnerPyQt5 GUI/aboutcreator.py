# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutCreator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutCreator(object):
    def setupUi(self, AboutCreator):
        AboutCreator.setObjectName("AboutCreator")
        AboutCreator.resize(371, 144)
        self.centralwidget = QtWidgets.QWidget(AboutCreator)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 331, 101))
        self.textBrowser.setObjectName("textBrowser")
        AboutCreator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AboutCreator)
        self.statusbar.setObjectName("statusbar")
        AboutCreator.setStatusBar(self.statusbar)

        self.retranslateUi(AboutCreator)
        QtCore.QMetaObject.connectSlotsByName(AboutCreator)

    def retranslateUi(self, AboutCreator):
        _translate = QtCore.QCoreApplication.translate
        AboutCreator.setWindowTitle(_translate("AboutCreator", "About Creator"))
        self.textBrowser.setHtml(_translate("AboutCreator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">+---------------------------+</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">|   A P P L E    C I D R   |</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">+---------------------------+</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">This program/Application/Script was made by and for the Apple Cidr Cyber Patriot team</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Creator: Michael Brenner</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutCreator = QtWidgets.QMainWindow()
    ui = Ui_AboutCreator()
    ui.setupUi(AboutCreator)
    AboutCreator.show()
    sys.exit(app.exec_())
