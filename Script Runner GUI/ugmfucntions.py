#!/usr/bin/python3
import os
import subprocess as sub
from sys import platform


class usrGruFunc:
    def addusr():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is in progress')
        elif platform == 'win32':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')
