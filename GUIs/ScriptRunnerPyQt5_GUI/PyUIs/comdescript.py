# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comDescript.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comDescript(object):
    def setupUi(self, comDescript):
        comDescript.setObjectName("comDescript")
        comDescript.resize(531, 365)
        comDescript.setStyleSheet("background-color: #414E6E; color: #CCD2E6")
        self.buttonBox = QtWidgets.QDialogButtonBox(comDescript)
        self.buttonBox.setGeometry(QtCore.QRect(470, 340, 51, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(comDescript)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 531, 331))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(comDescript)
        self.buttonBox.accepted.connect(comDescript.accept)
        self.buttonBox.rejected.connect(comDescript.reject)
        QtCore.QMetaObject.connectSlotsByName(comDescript)

    def retranslateUi(self, comDescript):
        _translate = QtCore.QCoreApplication.translate
        comDescript.setWindowTitle(_translate("comDescript", "Hey! These are descriptions for each command!"))
        self.textBrowser.setHtml(_translate("comDescript", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt;\">This is a list of descriptions for each command:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">Universal Commands</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Updates:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will update your Operating System (Only the Operating System if you are using Windows 10 or Mac OS) When using on windows 10, it will continue to keep cheking for updates until there are none left compared to Settings &gt; Updates which will only check once and update. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; text-decoration: underline;\">NOTE:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> For other updates to third party apps, I recommend using software such as PatchMyPc which will update up 250+ apps at once. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Search For Prohibited Media:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will search through the entire system looking for the following file types: .jpg, .mp4, .flv, .avi, .wmv, .mov, .png, .tif, .gif, .mp3, .wma, .aif, .jar  This command will output it\'s results into a text file on the Desktop.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Remove Prohibited Software:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will search through your system looking for known games and software that is known to be against the rules of Cyber Patriots. E.g. Wireshark and BitTorrent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">_________________________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Check the Hash of a File:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will check the hash of a file of your choosing. (helpful for Forensics Questions)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Services Configurations:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will apply premade configurations to services like ssh, ftp, and samba.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">Windows Specific Commands</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Windows Firewall Settings:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will open or close certain ports based upon the configurations you made when you first opened the app. Along with those changes it will also close a couple of other ports that are known vulnerabilities.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Windows Basic Configurations:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will install prebuilt Local Policies (E.g. Lockout policies, audit policies, and password policies) and Group Policies and making sure that IE is also installed, because that will always be required. I have missed too many points due to forgetting about Internet Explorer </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Linux Specific Commands</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Linux Firewall Settings:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will open or close certain ports based upon the configurations you made when you first opened the app. Along with those changes it will also close a couple of other ports that are known vulnerabilities.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Audit System:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will install an auditing program called Lynis that checks for vulnerabilities that you will want to change. It will ouput the results into a text file on the Desktop</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Malware Removal:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"> This command will use the program called ClamAV/ClamTK to search for Malware on this machine.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">______________________________________________</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Linux Basic Configurations: </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">This command will install premade Local Policies (E.g. Lockout Policies and Password Policies)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:16pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    comDescript = QtWidgets.QDialog()
    ui = Ui_comDescript()
    ui.setupUi(comDescript)
    comDescript.show()
    sys.exit(app.exec_())
