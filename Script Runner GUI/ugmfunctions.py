#!/usr/bin/python3
import os
import subprocess as sub
from sys import platform
from Script_Runner import *
from threading import *
from tkinter import *
from tkinter.ttk import *
from Script_Runner import *
import time
if platform == 'linux':
    import crypt
    import pwd
import distro #for figuring out what linux distro


#global variables
OS = distro.linux_distribution()
ops = OS[0]


def changeVar(function, var, change):
    var = change
    print(var)
    print(function)
    function



class usrGruFunc:

    # This class will be used for data collection to be used in the execution of the command in usrGruFuncEXECUTION

    def addusr(self):
        rootusr = Tk()
        rootusr.title('Add User To System')
        name = StringVar()
        paswd = StringVar()
        group = StringVar()

        def addusrEXEC():
            if platform == 'linux':
                username = name.get()
                passwds = passwd.get()
                admin = group.get()
                encrypted_password = crypt.crypt(passwds)
                print(username)
                print(encrypted_password)
                print(admin)

                if admin == 'yes' or admin == 'Yes':
                    print('This user will be an admin')
                    command = "sudo -S useradd -m " + username + " -p " + encrypted_password
                    if ops == 'Manjaro Linux':
                        command2 = "sudo -S usermod --append --groups wheel " + username
                        command3 = "sudo -S usermod --append --groups adm " + username
                    else:
                        command2 = "sudo -S usermod -a -G sudo " + username
                        command3 = "sudo -S usermod -a -G adm " + username
                    userCheck = "sudo id -u " + username
                    print(command)
                    print(command2)
                    print(command3)
                    os.system(command)
                    os.system(command2)
                    os.system(command3)
                    print(pwd.getpwnam(username))
                elif admin == 'no' or admin == 'No':
                    print('The user will not be an admin')
                    command = "sudo -S useradd -m " + username + " -p " + encrypted_password
                    userCheck = "sudo id -u " + username
                    print(command)
                    os.system(command)
                    print(pwd.getpwnam(username))

            elif platform == 'win32': #This code is broken
                username = name.get()
                passwds = passwd.get()
                admin = group.get()
                print(username)
                print(passwds)
                print(admin)
                if admin == 'yes' or admin == 'Yes':
                    print('This user will be an admin')
                    secureCom = "ConvertTo-SecureString " + passwds + " -AsPlainText -Force"
                    passSecure = sub.Popen(secureCom.split(), stdout=sub.PIPE)
                    SecurePass = passSecure.stdout.read()
                    command = "New-LocalUser " + username + " -Password " + SecurePass + " -Confirm"
                    command2 = "Add-LocalGroupMember -Group 'Administrators' -Member " + username
                    print(command)
                    print(command2)
                    #os.system(command)
                    #os.system(command2)
                    sub.Popen(command.split())
                    sub.Popen(command2.split())
                elif admin == 'no' or admin == 'No':
                    print('This user will not be an admin')
                    secureCom = "ConvertTo-SecureString " + passwds + " -AsPlainText -Force"
                    passSecure = sub.Popen(secureCom.split(), stdout=sub.PIPE)
                    SecurePass = passSecure.stdout.read()
                    command = "New-LocalUser " + username + " -Password " + SecurePass + " -Confirm"
                    print(command)
                    sub.Popen(command.split())

            elif platform == 'darwin':
                username = name.get()
                passwds = passwd.get()
                admin = group.get()
                print(username)
                print(passwds)
                print(admin)
                if admin == 'yes' or admin == 'Yes':
                    print('This user will be an admin')
                    command = 'sudo dscl / -create /Users/' + username
                    command2 = 'sudo dscl / -passwd /Users/' + username + ' ' + passwds
                    command3 = 'sudo dscl / -append /Groups/admin GroupMembership ' + username
                    print(command)
                    print(command2)
                    print(command3)
                    #os.system(command)
                    #os.system(command2)
                    #os.system(command3)
                    sub.Popen(command.split())
                    sub.Popen(command2.split())
                    sub.Popen(command3.split())
                    print(pwd.getpwnam(username))
                elif admin == 'no' or admin == 'No':
                    print('This user will not be an admin')
                    command = 'sudo dscl / -create /Users/' + username
                    command2 = 'sudo dscl / -passwd /Users/' + username + ' ' + passwds
                    print(command)
                    print(command2)
                    #os.system(command)
                    #os.system(command2)
                    sub.Popen(command.split())
                    sub.Popen(command2.split())
                    print(pwd.getpwnam(username))
            else:
                print('This command does not yet support this OS')


        userlbl = Label(rootusr, text='What is the name of the user you would like to add?')
        userlbl.grid(row='1', column='1', sticky='W')
        name = Entry(rootusr, textvariable=name)
        name.grid(row='2', column='1', sticky='W', padx='5', pady='2')

        passlbl = Label(rootusr, text='Please insert secure password here:')
        passlbl.grid(row='3', column='1', sticky='W')
        passwd = Entry(rootusr, textvariable=paswd)
        passwd.grid(row='4', column='1', sticky='W', padx='5', pady='2')

        grouplbl = Label(rootusr, text='Is this user an admin? [yes/no]')
        grouplbl.grid(row='5', column='1', sticky='W')
        group = Entry(rootusr, textvariable=group)
        group.grid(row='6', column='1', sticky='W', padx='5', pady='2')


        Confirm = Button(rootusr, text='Confirm', command=addusrEXEC)
        Confirm.grid(row='7', column='2', sticky='W', padx='5', pady='5')

        cancel = Button(rootusr, text='Cancel', command=rootusr.destroy)
        cancel.grid(row='7', column='1', sticky='W', padx='5', pady='5')

        rootusr.mainloop()

    def rmuser(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def adgru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def rmgru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def adusrtogru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def rmusrfrogru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lslocausr(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lslocagru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lsmemgru(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def lsgruusrin(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

    def chngusrspass(self):
        if platform == 'linux':
            print('This command is not complete yet')
        elif platform == 'win32':
            print('This command is not complete yet')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

#targets = [chngTOmm, usrGruFunc.addusr, usrGruFunc.rmuser, usrGruFunc.adgru, usrGruFunc.rmgru, usrGruFunc.adusrtogru, usrGruFunc.rmusrfrogru, usrGruFunc.lslocausr, usrGruFunc.lslocagru, usrGruFunc.lsmemgru, usrGruFunc.lsgruusrin, usrGruFunc.chngusrspass]

#class ThreadUGMfunc:
#    def threader(self, com):
#        try:
#            print(targets[com])
#            threader = Thread(target=targets[com])
#            threader.start()
#        except Exception as e:
#            print(e)
#            print('Could not start thread')

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
