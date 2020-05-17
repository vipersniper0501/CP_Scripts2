#!/usr/bin/python3
import os
import subprocess as sub
from sys import platform
from Script_Runner import *
from threading import *
from tkinter import *
from tkinter.ttk import *
import tkinter as tk  # used to force certain widget type
import tkinter.font as tkFont
from Script_Runner import *
import time
import random

if platform == 'linux':
    import crypt
    import pwd
import distro  # for figuring out what linux distro

# global variables
OS = distro.linux_distribution()
ops = OS[0]


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def changeVar(function, var, change):
    var = change
    print(var)
    print(function)
    function


class usrGruFunc:

    def __init__(self):
        pass

    def addusr(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
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
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
                elif admin == 'no' or admin == 'No':
                    print('The user will not be an admin')
                    command = "sudo -S useradd -m " + username + " -p " + encrypted_password
                    userCheck = "sudo id -u " + username
                    os.system(command)
                    print(pwd.getpwnam(username))
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
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
                    sub.Popen(["powershell", "& {" + command + "}"])
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
                elif admin == 'no' or admin == 'No':
                    print('This user will not be an admin')
                    command = """
$nusnm = """ + '"{}"'.format(username) + """
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwds) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Get-LocalUser
                    """
                    print(command)
                    sub.Popen(["powershell", "& {" + command + "}"])
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
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
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
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
                    print('User ' + username + " has been successfully added!")
                    topusr.destroy()
            else:
                print('This command does not yet support this OS')

        userlbl = Label(topusr, text='What is the name of the User you would like to add?')
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
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
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
                print('User ' + username + ' has been successfully removed!')
                topusr.destroy()
            elif platform == 'win32':
                username = name.get()
                command = 'Remove-LocalUser -Name ' + username
                sub.Popen(command.split())
                print('User ' + username + ' has been successfully removed!')
                topusr.destroy()
            elif platform == 'darwin':
                username = name.get()
                command = 'sudo dscl . delete /Users/' + username
                command2 = 'sudo rm -r /Users/' + username
                sub.Popen(command.split())
                sub.Popen(command2.split())
                print('User ' + username + ' has been successfully removed!')
                topusr.destroy()
            else:
                print('This command does not yet support this OS')

        userlbl = Label(topusr, text='What is the name of the user\nyou would like to remove?')
        userlbl.grid(row=0, column=0, sticky='nw', pady=10)
        name = Entry(topusr, textvariable=name)
        name.grid(row=0, column=0, sticky='nw', padx='5', pady='45')

        if platform == 'linux':
            command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
            os.system(command)
            # print(exec)
            with open("userlist.txt", "r") as f:
                for line in f:
                    output = f.read()
                    os.remove("userlist.txt")
                    print(output)
        elif platform == 'win32':
            command = "Get-LocalUser"
            exec = sub.Popen(["powershell", "& {Get-LocalUser}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
        elif platform == 'darwin':
            command = "sudo dscl . list /Users | grep -v '_'"
            exec = sub.Popen(command.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")

        outputBOX = Label(framlabel, text=output, background='lightgreen')
        outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

        Confirm = Button(topusr, text='Confirm', command=rmusrEXEC)
        Confirm.grid(row=2, column=1, sticky='e', padx='5', pady='5')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=2, column=0, sticky='e', padx='5', pady='5')

    def adgru(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('Create User Group')
        name = StringVar()

        def adgruEXEC():
            if platform == 'linux':
                gruname = name.get()
                command = 'sudo groupadd ' + gruname
                print(command)
                sub.Popen(command.split())
                print('Group ' + gruname + ' has been successfully added!')
                topusr.destroy()
            elif platform == 'win32':
                gruname = name.get()
                command = 'New-LocalGroup -Name ' + gruname
                print(command)
                sub.Popen(["powershell", "& {" + command + "}"])
                print('Group ' + gruname + ' has been successfully added!')
                topusr.destroy()
            elif platform == 'darwin':
                gruname = name.get()
                print('This command does not support MacOS')
                topusr.destroy()
            else:
                print('This command does not yet support this OS')

        grulbl = Label(topusr, text='What is the name of the Group you would like to add?')
        grulbl.grid(row=1, column=1, sticky='W')
        name = Entry(topusr, textvariable=name)
        name.grid(row=2, column=1, sticky='W', padx=5, pady=2)

        Confirm = Button(topusr, text='Confirm', command=adgruEXEC)
        Confirm.grid(row=7, column=2, sticky='W', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=1, sticky='W', padx=5, pady=5)

    def rmgru(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('Remove User Group')
        topusr.geometry('950x450')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='Local Groups')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=1, sticky='nsew')

        name = StringVar()

        def rmgruEXEC():
            if platform == 'linux':
                gruname = name.get()
                command = 'sudo groupdel ' + gruname
                sub.Popen(command.split())
                # os.system(command)
                print('Group ' + gruname + ' has been successfully removed!')
                topusr.destroy()
            elif platform == 'win32':
                gruname = name.get()
                command = 'Remove-LocalGroup -Name ' + gruname
                sub.Popen(["powershell", "& {" + command + "}"])
                print('Group ' + gruname + ' has been successfully removed!')
                topusr.destroy()
            elif platform == 'darwin':
                print('This command is does not support MacOS')
            else:
                print('This command does not yet support this OS')

        # Lists groups in box
        if platform == 'linux':
            command = 'getent group | cut -d: -f1 > grouplist.txt'
            os.system(command)
            with open("grouplist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("grouplist.txt")
            print(output)

            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            print('This command is not complete yet')
        elif platform == 'win32':
            command = 'Get-LocalGroup'
            exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

        grulbl = Label(topusr, text='What is the name of the Group you would like to remove?')
        grulbl.grid(row=0, column=0, sticky='nw', pady=10)
        name = Entry(topusr, textvariable=name)
        name.grid(row=0, column=0, sticky='nw', padx=5, pady=30)

        Confirm = Button(topusr, text='Confirm', command=rmgruEXEC)
        Confirm.grid(row=7, column=1, sticky='W', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=0, sticky='W', padx=5, pady=5)

    def adusrtogru(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('Add User to Group')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='USERS')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=0, sticky='nsew')

        framlabel2 = tk.LabelFrame(topusr, text='GROUPS')
        framlabel2.config(bd=5, background='lightgreen')
        framlabel2.grid(row=0, column=1, sticky='nsew')

        name = StringVar()
        gruname = StringVar()

        def adusrtogruEXEC():
            if platform == 'linux':
                username = name.get()
                group = gruname.get()
                if ops == 'Manjaro Linux':
                    command = "sudo -S usermod --append --groups " + group + " " + username
                else:
                    command = "sudo -S usermod -a -G " + group + " " + username
                os.system(command)
                print("User " + username + " has been successfully add to group " + group)
                topusr.destroy()
            elif platform == 'win32':
                username = name.get()
                group = gruname.get()
                command = "Add-LocalGroupMember -Name " + username + " -Member " + group
                sub.Popen(["powershell", "& {" + command + "}"])
                print("User " + username + " has been successfully add to group " + group)
                topusr.destroy()
                print('This command is not complete yet')
            elif platform == 'darwin':
                print('This command does not work on MacOS')
            else:
                print('This command does not yet support this OS')

        # Lists Users
        if platform == 'linux':
            command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
            os.system(command)
            # print(exec)
            with open("userlist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("userlist.txt")
            print(output)
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')

        elif platform == 'win32':
            command = "Get-LocalUser"
            exec = sub.Popen(["powershell", "& {Get-LocalUser}"], stdout=sub.PIPE)
            output, _ = exec.communicate()
            print(output.decode("utf-8"))

            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            command = "sudo dscl . list /Users | grep -v '_'"
            exec = sub.Popen(command.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        else:
            print('This command does not yet support this OS')

        # Lists Groups
        if platform == 'linux':
            command = 'getent group | cut -d: -f1 > grouplist.txt'
            os.system(command)
            with open("grouplist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("grouplist.txt")
            print(output)

            outputBOX = Label(framlabel2, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
            print('This command is not complete yet')
        elif platform == 'win32':
            command = 'Get-LocalGroup'
            exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel2, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

        adlbl = Label(topusr, text='What is the name of the User you would like to add to a group?')
        adlbl.grid(row=1, column=0, sticky='nw')
        usrname = Entry(topusr, textvariable=name)
        usrname.grid(row=2, column=0, sticky='nw', padx='5', pady='2')

        grulbl = Label(topusr, text='What is the name of the Group you would like to add the User to?')
        grulbl.grid(row=1, column=1, sticky='nw')
        gruname = Entry(topusr, textvariable=gruname)
        gruname.grid(row=2, column=1, sticky='nw', padx='5', pady='2')

        Confirm = Button(topusr, text='Confirm', command=adusrtogruEXEC)
        Confirm.grid(row=7, column=0, sticky='w', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=1, sticky='e', padx=5, pady=5)

    def rmusrfrogru(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('Remove User from Group')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='USERS')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=0, sticky='nsew')

        framlabel2 = tk.LabelFrame(topusr, text='GROUPS')
        framlabel2.config(bd=5, background='lightgreen')
        framlabel2.grid(row=0, column=1, sticky='nsew')

        name = StringVar()
        gruname = StringVar()

        def rmusrfrogruEXEC():
            if platform == 'linux':
                username = name.get()
                group = gruname.get()
                command = 'gpasswd -d ' + username + " " + group
                os.system(command)
                print('User ' + username + ' has been removed successfully from group ' + group)
                topusr.destroy()
            elif platform == 'win32':
                username = name.get()
                group = gruname.get()
                command = 'Remove-LocalGroupMember -Group ' + group + ' -Member ' + username
                sub.Popen(["powershell", "& {" + command + "}"])
                topusr.destroy()
            elif platform == 'darwin':
                print('This command does not work on MacOS')
                topusr.destroy()
            else:
                print('This command does not yet support this OS')

        # Lists Users
        if platform == 'linux':
            command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
            os.system(command)
            # print(exec)
            with open("userlist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("userlist.txt")
            print(output)
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')

        elif platform == 'win32':
            command = "Get-LocalUser"
            exec = sub.Popen(["powershell", "& {Get-LocalUser}"], stdout=sub.PIPE)
            output, _ = exec.communicate()
            print(output.decode("utf-8"))

            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            command = "sudo dscl . list /Users | grep -v '_'"
            exec = sub.Popen(command.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        else:
            print('This command does not yet support this OS')

        # Lists Groups
        if platform == 'linux':
            command = 'getent group | cut -d: -f1 > grouplist.txt'
            os.system(command)
            with open("grouplist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("grouplist.txt")
            print(output)

            outputBOX = Label(framlabel2, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
            print('This command is not complete yet')
        elif platform == 'win32':
            command = 'Get-LocalGroup'
            exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel2, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

        adlbl = Label(topusr, text='What is the name of the User you would like to remove from a group?')
        adlbl.grid(row=1, column=0, sticky='nw')
        usrname = Entry(topusr, textvariable=name)
        usrname.grid(row=2, column=0, sticky='nw', padx='5', pady='2')

        grulbl = Label(topusr, text='What is the name of the Group you would like to remove the User from?')
        grulbl.grid(row=1, column=1, sticky='nw')
        gruname = Entry(topusr, textvariable=gruname)
        gruname.grid(row=2, column=1, sticky='nw', padx='5', pady='2')

        Confirm = Button(topusr, text='Confirm', command=rmusrfrogruEXEC)
        Confirm.grid(row=7, column=0, sticky='w', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=1, sticky='e', padx=5, pady=5)

    def lslocausr(self):
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
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
                # print(exec)
                with open("userlist.txt", "r") as f:
                    for line in f:
                        output = f.read()
                os.remove("userlist.txt")
                print(output)
                outputBOX = Label(framlabel, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

            elif platform == 'win32':
                command = "Get-LocalUser"
                exec = sub.Popen(["powershell", "& {Get-LocalUser}"], stdout=sub.PIPE)
                output, _ = exec.communicate()
                print(output.decode("utf-8"))

                outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            elif platform == 'darwin':
                command = "sudo dscl . list /Users | grep -v '_'"
                exec = sub.Popen(command.split(), stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
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
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('List Local User Groups')
        topusr.geometry('950x450')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='Local Groups')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=1, sticky='nsew')

        def lsLocaGruEXEC():
            if platform == 'linux':
                command = 'getent group | cut -d: -f1 > grouplist.txt'
                os.system(command)
                with open("grouplist.txt", "r") as f:
                    for line in f:
                        output = f.read()
                os.remove("grouplist.txt")
                print(output)

                outputBOX = Label(framlabel, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
                print('This command is not complete yet')
            elif platform == 'win32':
                command = 'Get-LocalGroup'
                exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                outputBOX = Label(framlabel, text=output, background='lightgreen')
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

    def lsmemgru(self):  # Missing MacOS commands
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('List Members of Group')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='GROUPS')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=0, sticky='nsew')

        framlabel2 = tk.LabelFrame(topusr, text='GROUP MEMBERS')
        framlabel2.config(bd=5, background='lightgreen')
        framlabel2.grid(row=0, column=1, sticky='nsew')

        gruname = StringVar()

        def lsmemgruEXEC():
            if platform == 'linux':
                group = gruname.get()
                command = 'grep -i --color ' + group + ' /etc/group'
                exec = sub.Popen(command.split(), stdout=PIPE)
                stdout, _ = exec.communicate()
                ouput = stdout.decode("utf-8")
                outputBOX = Label(framlabel2, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

            elif platform == 'win32':
                group = gruname.get()
                command = 'Get-LocalGroupMember -Name ' + group
                exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
                stdout, _ = exec.communicate()
                output = stdout.decode("utf-8")
                outputBOX = Label(framlabel2, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

            elif platform == 'darwin':
                print('This command is not complete yet')
            else:
                print('This command does not yet support this OS')

        if platform == 'linux':
            command = 'getent group | cut -d: -f1 > grouplist.txt'
            os.system(command)
            with open("grouplist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("grouplist.txt")
            print(output)
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            print('This command is not complete yet')
        elif platform == 'win32':
            command = 'Get-LocalGroup'
            exec = sub.Popen(["powershell", "& {" + command + "}"], stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            print('This command is not complete yet')
        else:
            print('This command does not yet support this OS')

        grulbl = Label(topusr, text='What is the name of the Group that you would like to see the Members of?')
        grulbl.grid(row=1, column=0, sticky='nw')
        gruname = Entry(topusr, textvariable=gruname)
        gruname.grid(row=2, column=0, sticky='nw', padx='5', pady='2')

        Confirm = Button(topusr, text='Confirm', command=lsmemgruEXEC)
        Confirm.grid(row=7, column=0, sticky='w', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=1, sticky='e', padx=5, pady=5)

    def lsgruusrin(self):  # Missing Windows Commands and MacOS commands
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('List Members of Group')
        topusr.rowconfigure(0, weight=1)
        topusr.columnconfigure(1, weight=1)

        framlabel = tk.LabelFrame(topusr, text='USERS')
        framlabel.config(bd=5, background='lightgreen')
        framlabel.grid(row=0, column=0, sticky='nsew')

        framlabel2 = tk.LabelFrame(topusr, text='USER IS A MEMBER OF THE FOLLOWING GROUPS')
        framlabel2.config(bd=5, background='lightgreen')
        framlabel2.grid(row=0, column=1, sticky='nsew')

        name = StringVar()

        def lsgruusrinEXEC():
            if platform == 'linux':
                username = name.get()
                command = 'groups ' + username + ' > groupsuserin.txt'
                os.system(command)
                with open("groupsuserin.txt", "r") as f:
                    for line in f:
                        output = f.read()
                os.remove("groupsuserin.txt")
                outputBOX = Label(framlabel2, text=output, background='lightgreen')
                outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
            elif platform == 'win32':
                username = name.get()
                print('This command is not complete yet')
            elif platform == 'darwin':
                username = name.get()
                print('This command is not complete yet')
            else:
                print('This command does not yet support this OS')

        # Lists Users
        if platform == 'linux':
            command = """cat /etc/passwd | grep "/home" | cut -d":" -f1 > userlist.txt"""
            os.system(command)
            # print(exec)
            with open("userlist.txt", "r") as f:
                for line in f:
                    output = f.read()
            os.remove("userlist.txt")
            print(output)
            outputBOX = Label(framlabel, text=output, background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')

        elif platform == 'win32':
            command = "Get-LocalUser"
            exec = sub.Popen(["powershell", "& {Get-LocalUser}"], stdout=sub.PIPE)
            output, _ = exec.communicate()
            print(output.decode("utf-8"))

            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
        elif platform == 'darwin':
            command = "sudo dscl . list /Users | grep -v '_'"
            exec = sub.Popen(command.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode("utf-8")
            outputBOX = Label(framlabel, text=output.decode("utf-8"), background='lightgreen')
            outputBOX.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky='nsew')
        else:
            print('This command does not yet support this OS')

        userlbl = Label(topusr,
                        text='What is the name of the User that you would like to see the groups that they are in?')
        userlbl.grid(row=1, column=0, sticky='W')
        name = Entry(topusr, textvariable=name)
        name.grid(row=2, column=0, sticky='W', padx='5', pady='2')

        Confirm = Button(topusr, text='Confirm', command=lsgruusrinEXEC)
        Confirm.grid(row=7, column=1, sticky='W', padx='5', pady='5')

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=0, sticky='W', padx='5', pady='5')

    def chngusrspass(self):  # Missing windows and MacOS commands
        topusr = Toplevel()
        topusr.iconphoto(False, tk.PhotoImage(file="cup2.png"))
        topusr.title('Add User To System')

        paswd = StringVar()

        def chngusrspassEXEC():
            if platform == 'linux':
                passwds = paswd.get()
                command = """
userlist=( $(eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1) )
echo ${userlist[@]}
usersleft=${#userlist[@]}
echo $usersleft
newpasswd=""" + passwds + """
i=0
while [ $usersleft != 0 ]; do
    sudo echo "${userlist[$i]}:${newpasswd}" | sudo chpasswd
    echo "User ${userlist[$i]} password has been changed successfully!"
    let i=i+1
    echo $i
    let usersleft=usersleft-1
    echo $usersleft
    sleep 0.5s
done
                """
                os.system(command)

                print('This command is not complete yet')
            elif platform == 'win32':
                print('This command is not complete yet')
            elif platform == 'darwin':
                print('This command is not complete yet')
            else:
                print('This command does not yet support this OS')

        passlbl = Label(topusr, text='Please insert secure password here:')
        passlbl.grid(row=0, column=0, sticky='w')
        passwd = Entry(topusr, textvariable=paswd)
        passwd.grid(row=1, column=0, sticky='w', padx=5, pady=2)

        Confirm = Button(topusr, text='Confirm', command=chngusrspassEXEC)
        Confirm.grid(row=7, column=1, sticky='W', padx=5, pady=5)

        cancel = Button(topusr, text='Cancel', command=topusr.destroy)
        cancel.grid(row=7, column=0, sticky='W', padx='5', pady='5')
