import sys
import time
from main import Ui_MainWindow
from aboutcreator import *
#from button_logic import *
#from PyQt5 import QtCore, QtGui, QtWidgets
#from Auto import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from scripFunc.scripEXEC import *
from threading import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Button logic (calls functions in module and connects to other parts of GUI. Does not actually do anything to system)

class Mainstart(QMainWindow, Ui_MainWindow):


    def __init__(self):
        print('Script Runner has started')
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(604, 427)
        self.setWindowIcon(QtGui.QIcon('cup2.png'))
        #self.actionAbout_Creator.clicked.connect(self.Ui_AboutCreator)
        self.funcassign()

    def aboutCre(self):

        #self.about = Ui_AboutCreator()
        #self.about.show()

        #QMainWindow.__init__(self)
        #self.setupUi(self)
        print('Showing about creator window')


#####################################
    def funcassign(self):
        print('Assigning functions')

        scripfunc = ScriptRunnerFunc()

        #self.menubarButtons = [self.actionAbout_Creator]
        #self.menubarActions = [self.aboutCre]

        #buttons = {self.Updates_button:scripfunc.updateos}

        #self.buttonNames = [self.Updates_button, self.servsetbutton, self.fwlbutton, self.malrembutton, self.rmvprosoftbutton, self.basicConfbutton, self.auditbutton, self.srchmedbutton]
        #targets = [scripfunc.updateos, scripfunc.servSet, scripfunc.fwl, scripfunc.malRem, scripfunc.rmProCont, scripfunc.basConf, scripfunc.alyn, scripfunc.srchmedia]

        #menubar
        #for i in range(0, len(self.menubarButtons)):
        #    self.menubarButtons[i].triggered.connect(self.menubarActions[i])

        #for i in range(0, len(self.buttonNames)):
        #    self.buttonNames[i].setCheckable(True)
        #    self.buttonNames[i].clicked.connect(lambda i=i: threader(i))
        #    self.buttonNames[i].pressed.connect(lambda i=i: buttonPress(i))
        #self.quit_button.clicked.connect(self.quitButon)




        def quitButton():
            print('Closing program')
            sys.exit()


        self.quit_button.clicked.connect(quitButton)
        self.Updates_button.clicked.connect(lambda: threader(scripfunc.updateos))
        self.servsetbutton.clicked.connect(lambda: threader(scripfunc.servSet))
        self.fwlbutton.clicked.connect(lambda: threader(scripfunc.fwl))
        self.malrembutton.clicked.connect(lambda: threader(scripfunc.malRem))
        self.rmvprosoftbutton.clicked.connect(lambda: threader(scripfunc.rmProCont))
        self.basicConfbutton.clicked.connect(lambda: threader(scripfunc.basConf))
        self.auditbutton.clicked.connect(lambda: threader(scripfunc.alyn))
        self.srchmedbutton.clicked.connect(lambda: threader(scripfunc.srchmedia))

        def threader(com):
            try:
                threader = Thread(target=com)
                threader.start()
            except Exception as e:
                print(e)
                print('Could not start thread')










        #def buttonPress(button):
            #print('button pressed')
            #print(self.buttonNames[button])
        #    if self.buttonNames[button].isChecked():
        #        self.buttonNames[button].setStyleSheet("""
#border: 2px solid;
#border-color: grey;
#border-style: inset;
#border-width: 2.5px;
#background-color: lightblue;
#border-radius: 10px;
#color: black;
#                """)

#            else:
#               self.buttonNames[button].setStyleSheet("""
#border: 2px solid;
#border-color: grey;
#border-style: outset;
#border-width: 2.5px;
#background-color: lightblue;
#border-radius: 10px;
#color: black;
#                """)




######################








if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = Mainstart()
    main.show()
    sys.exit(app.exec_())
