#!/usr/bin/python3
import os
import subprocess as sub
from sys import platform
from Script_Runner import *
from threading import *
from tkinter import *
from tkinter.ttk import *
from Script_Runner import *


def changeVar(function, var, change):
    var = change
    print(var)
    print(function)
    function


class usrGruFuncEXECUTION:
    def addusrEXEC():
        usrgru = usrGruFunc()
        username = usrgru.name.get()
        print(username)
        print('Not ready yet')


class usrGruFunc:

    # This class will be used for data collection to be used in the execution of the command in usrGruFuncEXECUTION


    def addusr():
        rootusr = Tk()
        rootusr.title('Add User To System')
        usrgruEXEC = usrGruFuncEXECUTION()

        def addusrEXEC():
            #usrgru = usrGruFunc()
            username = name.get()
            passwords = password.get()
            admin = group.get()
            print(username)
            print(passwords)
            print(admin)

            if admin == 'yes' or admin == 'Yes':
                command = "sudo useradd -m " + username + " -p " + passwords + "; sudo usermod -a -G sudo " + username + "; sudo usermod -a -G adm " + username
                #command="sudo useradd -m " + username + "; sudo passwd " + username + "; sudo usermod -a -G sudo " + username + "; sudo usermod -a -G adm " + username
            elif admin == 'no' or admin == 'No':
                command = "sudo useradd -m " + username + " -p " + passwords
            # print('Not ready yet')


        if platform == 'debian' or platform == 'ubuntu' or platform == 'win32' or platform == 'linux':
            useryon = 0
            name = StringVar()
            password = StringVar()
            group = StringVar()

            userlbl = Label(rootusr, text='What is the name of the user you would like to add?')
            userlbl.grid(row='1', column='1', sticky='W')
            name = Entry(rootusr, textvariable=name)
            name.grid(row='2', column='1', sticky='W', padx='5', pady='2')

            passlbl = Label(rootusr, text='Please insert secure password here:')
            passlbl.grid(row='3', column='1', sticky='W')
            passwd = Entry(rootusr, textvariable=password, show='*', width='40')
            passwd.grid(row='4', column='1', sticky='W', padx='5', pady='2')

            grouplbl = Label(rootusr, text='Is this user an admin? [yes/no]')
            grouplbl.grid(row='5', column='1', sticky='W')
            group = Entry(rootusr, textvariable=group)
            group.grid(row='6', column='1', sticky='W', padx='5', pady='2')

            Confirm = Button(rootusr, text='Confirm', command=addusrEXEC)
            Confirm.grid(row='7', column='2', sticky='W', padx='5', pady='5')

            cancel = Button(rootusr, text='Cancel', command=rootusr.destroy)
            cancel.grid(row='7', column='1', sticky='W', padx='5', pady='5')

            #while useryon == 1:
            #    print('test')

            #usery = Radiobutton(rootusr, text='Yes', variable=useryon, value=1)
            #usery.grid(row='2', column='1', sticky='W')
            #usern = Radiobutton(rootusr, text='No', variable=useryon, value=0)
            #usern.grid(row='2', column='1', padx='50', sticky='W')

            #print(useryon)


            command = """read -p 'Would you like to add a user? [y/n] : ' aduseryn
        if [ $aduseryn = 'y' ]; then
            aduser=1
            while [ $aduser = 1 ]; do
                read -p 'What would you like to name this new user? : ' name
                read -p 'Is this user an Admin? [y/n] : ' adminyn
                if [ $adminyn = 'y' ]; then
                    sudo useradd -m $name
                    sudo passwd $name
                    sudo usermod -a -G sudo $name		#adds user to sudo group
                    sudo usermod -a -G adm $name   #adds user to admin group
                    echo "User ${name} has been created and has been added to admin and sudo groups"
                else
                    sudo useradd -m $name
                    sudo passwd $name
                    echo "User ${name} has been added!"
                fi
                read -p 'Would you like to add another user? [y/n] : ' aga
                if [ $aga = 'n' ]; then
                    $aduser=0
                fi
            done
            sleep 1s
        else
            usr_gru
        fi"""

            #sub.Popen(command.split(), shell=True)
            #print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')
        rootusr.mainloop()

    def rmuser():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def adgru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def rmgru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def adusrtogru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def rmusrfrogru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lslocausr():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lslocagru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lsmemgru():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lsgruusrin():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def chngusrspass():
        if platform == 'debian' or platform == 'ubuntu':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

targets = [chngTOmm, usrGruFunc.addusr, usrGruFunc.rmuser, usrGruFunc.adgru, usrGruFunc.rmgru, usrGruFunc.adusrtogru, usrGruFunc.rmusrfrogru, usrGruFunc.lslocausr, usrGruFunc.lslocagru, usrGruFunc.lsmemgru, usrGruFunc.lsgruusrin, usrGruFunc.chngusrspass]

class ThreadUGMfunc:
    def threader(self, com):
        try:
            print(targets[com])
            threader = Thread(target=targets[com])
            threader.start()
        except Exception as e:
            print(e)
            print('Could not start thread')

    #def threaderADDusr(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.addusr)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderRMVusr(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.rmuser)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderADDgru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.adgru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderRMVgru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.rmgru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderUSRtoGru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.adusrtogru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderUSRfroGru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.rmusrfrogru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderLSusr(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.lslocausr)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderLSgru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.lslocagru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderLSmemGru(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.lsmemgru)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderLSgruMemin(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.lsgruusrin)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')

    #def threaderCHNGpassAll(self):
    #    try:
    #        self.threader = Thread(target=usrGruFunc.chngusrspass)
    #        self.threader.start()
    #    except Exception as e:
    #        print(e)
    #        print('Could not start thread')
