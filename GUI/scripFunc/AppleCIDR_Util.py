import logging as log
from threading import Thread
from typing import Any
import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread

log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s",
    handlers=[
        log.FileHandler("AppleCIDR.log"),
        log.StreamHandler()
    ]
)


def NewThread(com, Returning: bool, thread_ID, *arguments) -> Any:
    """
    Will create a new thread for a function/command.

    :param com: Command to be Executed
    :param Returning: True/False Will the command return anything?
    :param thread_ID: Name of thread
    :param arguments: Arguments to be sent to Command

    """

    class NewThreadWorker(Thread):
        def __init__(self, group=None, target=None, name=None, args=(),
                     kwargs=None, *, daemon=None):
            Thread.__init__(self, group, target, name, args, kwargs,
                            daemon=daemon)
            self.daemon = True
            self._return = None

        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)

        def joinThread(self):
            Thread.join(self)
            return self._return

    ntw = NewThreadWorker(target=com, name=thread_ID, args=(*arguments,))
    if Returning:
        ntw.start()
        return ntw.joinThread()
    else:
        ntw.start()


# NOTE: This is in developement. Trying to get rid of the stupid
# QBasic::Timer error that keeps appearing every time a new thread is made.
def QNewThread(com, Returning: bool, thread_ID, *arguments) -> Any:
    """
    Will create a new thread using the PyQt5 QThread module
    """

    class NewQThreadWorker(QThread):
        def __init__(self):
            QThread.__init__(self)

        def __del__(self):
            self.wait()

        def run(self):
            com()


def Check_Password(Password1, Password2):
    """
    The PasswordChecker compares the two user inputted passwords and checks
    them against a set of rules.

    :param Password1: First Password Entry
    :param Password2: Second Password Entry
    :return: True/False (Does the Password meet the complexity requirements)
    """

    def PasswordChecker(Password1, Password2) -> bool:
        if Password1 != Password2:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your passwords do not match!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        # [LowerCase, UpperCase, Numbers, Symbols]
        character_rules = [0, 0, 0, 0]
        symbols = "'`~!@#$%^&*()_+-=[]{};:,./<>?"
        for i in range(0, len(Password1)):
            character = Password1[i]
            if character_rules[0] != 1:
                if character.islower():
                    character_rules[0] = 1
                elif not character.islower():
                    character_rules[0] = 0
            if character_rules[1] != 1:
                if character.isupper():
                    character_rules[1] = 1
                elif not character.isupper():
                    character_rules[1] = 0
            if character_rules[2] != 1:
                if character.isdigit():
                    character_rules[2] = 1
                elif not character.isdigit():
                    character_rules[2] = 0
            if character_rules[3] != 1:
                if character in symbols:
                    character_rules[3] = 1
                elif character not in symbols:
                    character_rules[3] = 0

        print(str(character_rules[0] == 1) + ' Lower Case')
        print(str(character_rules[1] == 1) + ' Upper case')
        print(str(character_rules[2] == 1) + ' number')
        print(str(character_rules[3] == 1) + ' symbols')

        if len(Password1) == 0:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! You don't have a password!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        elif len(Password1) < 8:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your password must have at least 8 characters!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        elif character_rules[0] == 0:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your password must have at "
                        "least 1 lower case letter!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        elif character_rules[1] == 0:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your password must have at "
                        "least 1 Upper Case letter!")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        elif character_rules[2] == 0:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your password must have at "
                        "least 1 number! [Ex: 123456]")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        elif character_rules[3] == 0:
            HEY = QMessageBox()
            HEY.setWindowTitle('Hey! Listen!')
            HEY.setText("Hey! Your password must have at "
                        "least 1 Symbol! [Ex: !@#$%^%&]")
            HEY.setIcon(QMessageBox.Critical)
            HEY.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
            HEY.exec_()
            return False
        else:
            return True
    return NewThread(PasswordChecker, True, "Check_Password",
                     Password1, Password2)


class TimerError(Exception):
    """Custom exception for the Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running")

        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        log.debug(f"Elapsed time: {elapsed_time:0.4f} seconds")
