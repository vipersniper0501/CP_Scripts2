#!/usr/bin/python3
import os
import subprocess as sub
from sys import platform
from Script_Runner import *
from threading import *
from tkinter import *
from tkinter.ttk import *
import tkinter as tk #used to force certain widget type
import tkinter.font as tkFont
from Script_Runner import *
import time
import random
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
        topusr = Toplevel()
        #rootusr = Tk()
        topusr.title('Add User To System')
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
                    os.system(command)
                    os.system(command2)
                    os.system(command3)
                    print(pwd.getpwnam(username))
                elif admin == 'no' or admin == 'No':
                    print('The user will not be an admin')
                    command = "sudo -S useradd -m " + username + " -p " + encrypted_password
                    userCheck = "sudo id -u " + username
                    os.system(command)
                    print(pwd.getpwnam(username))

            elif platform == 'win32':
                username = name.get()
                passwds = passwd.get()
                admin = group.get()
                print(username)
                print(passwds)
                print(admin)
                if admin == 'yes' or admin == 'Yes':
                    print('This user will be an admin')
                    print(os.getcwd())
                    command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwds) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Add-LocalGroupMember -Group "Administrators" -Member $nusnm
Get-LocalUser
                    """
                    print(command)
                    sub.Popen(["powershell","& {" + command + "}"])

                elif admin == 'no' or admin == 'No':
                    print('This user will not be an admin')
                    command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwds) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Get-LocalUser
                    """
                    print(command)
                    sub.Popen(["powershell","& {" + command + "}"])

            elif platform == 'darwin':
                username = name.get()
                passwds = passwd.get()
                admin = group.get()
                print(username)
                print(passwds)
                print(admin)
                numb = random.randint(1001, 5000)
                if admin == 'yes' or admin == 'Yes':
                    print('This user will be an admin')
                    command = 'sudo dscl . -create /Users/' + username
                    command2 = 'sudo dscl . -create /Users/' + username + ' NFSHomeDirectory /Users/' + username
                    command3 = 'sudo dscl . -create /Users/' + username + ' RealName ' + username
                    command4 = 'sudo dscl . -create /Users/' + username + ' UniqueID ' + str(numb)
                    command5 = 'sudo dscl . -create /Users/' + username + ' PrimaryGroupID ' + str(numb)
                    command6 = 'sudo dscl . -passwd /Users/' + username + ' ' + passwds
                    command7 = 'sudo dscl . -append /Groups/admin GroupMembership ' + username
                    sub.Popen(command.split())
                    sub.Popen(command2.split())
                    sub.Popen(command3.split())
                    sub.Popen(command4.split())
                    sub.Popen(command5.split())
                    sub.Popen(command6.split())
                    sub.Popen(command7.split())
                elif admin == 'no' or admin == 'No':
                    print('This user will not be an admin')
                    command = 'sudo dscl . -create /Users/' + username
                    command2 = 'sudo dscl . -create /Users/' + username + ' NFSHomeDirectory /Users/' + username
                    command3 = 'sudo dscl . -create /Users/' + username + ' RealName ' + username
                    command4 = 'sudo dscl . -create /Users/' + username + ' UniqueID ' + str(numb)
                    command5 = 'sudo dscl . -create /Users/' + username + ' PrimaryGroupID ' + str(numb)
                    command6 = 'sudo dscl . -passwd /Users/' + username + ' ' + passwds
                    sub.Popen(command.split())
                    sub.Popen(command2.split())
                    sub.Popen(command3.split())
                    sub.Popen(command4.split())
                    sub.Popen(command5.split())
                    sub.Popen(command6.split())
            else:
                print('This command does not yet support this OS')


        userlbl = Label(topusr, text='What is the name of the user you would like to add?')
        userlbl.grid(row='1', column='1', sticky='W')
        name = Entry(topusr, textvariable=name)
        name.grid(row='2', column='1', sticky='W', padx='5', pady='2')

        passlbl = Label(topusr, text='Please insert secure password here:')
        passlbl.grid(row='3', column='1', sticky='W')
        passwd = Entry(topusr, textvariable=paswd)
        passwd.grid(row='4', column='1', sticky='W', padx='5', pady='2')

        grouplbl = Label(topusr, text='Is this user an admin? [yes/no]')
        grouplbl.grid(row='5', column='1', sticky='W')
        group = Entry(topusr, textvariable=group)
        group.grid(row='6', column='1', sticky='W', padx='5', pady='2')


        Confirm = Button(topusr, text='Confirm', command=addusrEXEC)
        Confirm.grid(row='7', column='2', sticky='W', padx='5', pady='5')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row='7', column='1', sticky='W', padx='5', pady='5')

    def rmuser(self):
        topusr = Toplevel()
        topusr.title('Remove User From System')
        name = StringVar()
        topusr.geometry('650x450')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='USERS')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=1, sticky='nsew')
        # Needs to show list of users to remove

        def rmusrEXEC():
            if platform == 'linux':
                username = name.get()
                command = 'userdel -r ' + username
                sub.Popen(command.split())

            elif platform == 'win32':
                username = name.get()
                command = 'Remove-LocalUser -Name ' + username
                sub.Popen(command.split())
            elif platform == 'darwin':
                username = name.get()
                command = 'sudo dscl . delete /Users/' + username
                command2 = 'sudo rm -r /Users/' + username
                sub.Popen(command.split())
                sub.Popen(command2.split())
            else:
                print('This command does not yet support this OS')

        userlbl = Label(topusr, text='What is the name of the user\nyou would like to remove?')
        userlbl.grid(row=0, column=0, sticky='W')
        name = Entry(topusr, textvariable=name)
        name.grid(row=1, column=0, sticky='W', padx='5', pady='2')

        if platform == 'linux':
            command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
            os.system(command)
            #print(exec)
            with open("userlist.txt", "r") as f:
                for line in f:
                    output = f.read()
                    os.remove("userlist.txt")
                    print(output)
        elif platform == 'win32':
            command = "Get-LocalUser"
            exec = sub.Popen(["powershell","& {Get-LocalUser}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
        elif platform == 'darwin':
            command = "sudo dscl . list /Users | grep -v '_'"
            exec = sub.Popen(command.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")

        outputBOX = Text(framlabel, text=output, background='lightgreen')
        outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

        Confirm = Button(topusr, text='Confirm', command=rmusrEXEC)
        Confirm.grid(row=2, column=1, sticky='e', padx='5', pady='5')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=2, column=0, sticky='e', padx='5', pady='5')

    def adgru(self):
        topusr = Toplevel()
        topusr.title('Create User Group')
        name = StringVar()
        paswd = StringVar()
        group = StringVar()

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
        topusr = Toplevel()
        topusr.title('List Local Users')
        topusr.geometry('950x450')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='OUTPUT')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=1, sticky='nsew')

        def lslocausrEXEC():
            if platform == 'linux':
                command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
                os.system(command)
                #print(exec)
                with open("userlist.txt", "r") as f:
                    for line in f:
                        output = f.read()
                os.remove("userlist.txt")
                print(output)
                outputBOX = Text(framlabel, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

            elif platform == 'win32':
                command = "Get-LocalUser"
                exec = sub.Popen(["powershell","& {Get-LocalUser}"], stdout=sub.PIPE)
                output, _ = exec.communicate()
                print(output.decode("utf-8"))

                OutputBOX = Text(framlabel, text=output.decode("utf-8"), background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            elif platform == 'darwin':
                command = "sudo dscl . list /Users | grep -v '_'"
                exec = sub.Popen(command.split(), stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                OutputBOX = Text(framlabel, text=output.decode("utf-8"), background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            else:
                print('This command does not yet support this OS')

        fontSize = tkFont.Font(size=14)
        lsusrs = tk.Button(topusr, text='List all\nusers on system', width=20, command=lslocausrEXEC)
        lsusrs.config(font=fontSize)
        lsusrs.grid(row=0, column=0, padx=5, pady=10, sticky='nswe')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=1, column=1, sticky='w', padx='5', pady='5')

    def lslocagru(self):
        topusr = Toplevel()
        topusr.title('List Local User Groups')
        topusr.geometry('950x450')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='Local Groups')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=1, sticky='nsew')

        def lsLocaGruEXEC():
            if platform == 'linux':
                command = 'getent group | cut -d: -f1'
                exec = sub.Popen(command.split(), stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                outputBOX = Text(framlabel, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
                print('This command is not complete yet')
            elif platform == 'win32':
                command = 'Get-LocalGroup'
                exec = sub.Popen(["powershell","& {" + command + "}"], stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                outputBOX = Text(framlabel, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            elif platform == 'darwin':
                print('This command is not complete yet')
            else:
                print('This command does not yet support this OS')


        fontSize = tkFont.Font(size=14)
        lsgrus = tk.Button(topusr, text='List all\nusers on system', width=20, command=lsLocaGruEXEC)
        lsgrus.config(font=fontSize)
        lsgrus.grid(row=0, column=0, padx=5, pady=10, sticky='nswe')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=1, column=1, sticky='w', padx='5', pady='5')

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
