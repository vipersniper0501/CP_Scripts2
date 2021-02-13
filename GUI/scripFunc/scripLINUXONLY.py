import configparser
import subprocess as sub
from sys import platform
import distro
from scripFunc.AppleCIDR_Util import NewThread, Check_Password
import logging as log

from PyQt5 import QtGui
from PyQt5.QtWidgets import QListWidgetItem, QDialog, QMessageBox, QTreeWidgetItem
from PyUIs.add_groupUI import Ui_Add_Group_UIClass
from PyUIs.addusrUI import Ui_addUSR
from PyUIs.changepass import Ui_chngpass
from PyUIs.rmvUSRoGRU import Ui_rmvusrogru
from PyUIs.user_group_modifyUI import Ui_user_group_list_modifiers


OS = distro.linux_distribution()[0]

config = configparser.ConfigParser()
config.read('config.ini')


def Linux_Find_Names():
    """
    This function seaerches for local usernames on the current system.

    :return: Returns three lists, Standard Users, Admins, and all users.
    """
    def find_names():
        # Local users are added to a list of standardUsers
        args = "ls /home"
        output = sub.Popen(args.split(), shell=False, stdout=sub.PIPE).communicate()[0].decode("utf-8").split("\n")
        allUsers = []
        standardUsers = []
        admins = []
        for _, i in enumerate(output):
            standardUsers.append(i)
        
        # Local Administrators are added to list of admins

        # Use this as an example for sub.Popen commands
        args = "cat /etc/group"
        process_catGroup = sub.Popen(args.split(), shell=False, stdout=sub.PIPE).communicate()[0].decode("utf-8").split("\n")
        args = "grep 'root'"
        output = sub.Popen(args.split(), shell-False, stdin=process_catGroup.stdout, stdout=sub.PIPE).communicate()[0].decode("utf-8").split("\n")

        output[0] = output[0][9:]
        for _, i in enumerate(output):
            admins.append(i)
        print(standardUsers)
        log.debug(standardUsers)
        for _, i in enumerate(standardUsers):
            if i not in allUsers:
                allUsers.append(i)
        for _, i in enumerate(admins):
            if i not in allUsers:
                allUsers.append(i)
        return standardUsers, admins, allUsers
    return NewThread(find_names, True, "Finding Names")


# Need to be configured for linux
def Find_Groups(users_n_groups: bool):
    """
    This is to find local groups and users on the windows 10 operating system
        
    :param users_n_groups: True/False  Do you need the users in each group also.
    :return: Returns a list of local groups and if users_n_groups is True, also returns a dictionary of users in each group
    """
    def find_groups(users_n_groups: bool):
        stdout, _ = sub.Popen(["powershell", "& {net localgroup}"], stdout=sub.PIPE).communicate()
        output = stdout.decode("utf-8").split("\n")
        groups = []
        for i in range(4, len(output) - 3):
            w = output[i].split('\r')[0].split('*')[1]
            groups.append(w)
        
        users_in_groups = {}
        # TODO: SPEED THIS UP
        if users_n_groups:
            for _, group in enumerate(groups):
                print(group)
                stdout2, _ = sub.Popen(["powershell", "net localgroup '" + group + "'"], stdout=sub.PIPE).communicate()
                try:
                    output = stdout2.decode("utf-8").split("\n")
                    user_names = []
                    for i3 in range(6, len(output) - 3):
                        y = output[i3].split('\r')[0]
                        print(y)
                        user_names.append(y)
                    if len(user_names) == 0:
                        users_in_groups[group] = ['No Users']
                    elif len(user_names) == 1:
                        users_in_groups[group] = [user_names[0]]
                    else:
                        for i4 in range(0, len(user_names)):
                            users_in_groups[group] = user_names
                except Exception as e:
                    print('\n\nException occurred: ' + str(e))
        
        print(groups)
        print(users_in_groups)
        return users_in_groups, groups
    return NewThread(find_groups, True, "Finding Groups", users_n_groups)


def malRem():
    def malrem():
            if OS == 'Manjaro Linux':
                sub.Popen("sudo pacman -S clamav -y", shell=True)
            else:
                sub.Popen("sudo apt install clamav -y", shell=True)
            command = ['sudo freshclam', 'sudo touch CLAMresults.txt',
                       'sudo clamscan -r --remove / | tee CLAMresults.txt']
            for _, i in enumerate(command):
                sub.Popen(command[i], shell=True)
    NewThread(malrem, False, "Malware Removal")


def alyn():
    def audit_w_lynis():
        if OS in ('Ubuntu', 'debian'):
            output = sub.Popen("sudo lynis --version", stdout=sub.PIPE, shell=True).communicate()[0].decode("utf-8").split("\n")
            if len(output) != 5:
                sub.Popen("sudo apt install lynis -y", shell=True)
            sub.Popen("touch ~/Desktop/audit_results.txt", shell=True)
            sub.Popen("sudo lynis audit system | tee ~/Desktop/audit_results.txt", shell=True)
        elif OS == 'Manjaro Linux':
            command = 'sudo pacman -S lynis --noconfirm'
            sub.Popen(command.split())
            command = 'sudo touch audit_results.txt'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system | tee audit_results.txt'
            sub.Popen(command2.split())
    NewThread(audit_w_lynis, False, "Auditing with lynis")


def Linux_addusr():
    class add_user_to_system(QDialog, Ui_addUSR):
        def __init__(self, parent=None):
            super(add_user_to_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(345, 187)
            self.setupUi(self)
            self.EXECUTE()
        
        def EXECUTE(self):
            self.adminyn = 'n'
            
            def adminy(selected):
                if selected:
                    print('This user will be an admin and have root permissions')
                    self.adminyn = 'y'
            
            def adminn(selected):
                if selected:
                    print('This user will NOT be an admin and not have root permissions')
                    self.adminyn = 'n'
            
            self.admin_y.toggled.connect(adminy)
            self.admin_n.toggled.connect(adminn)
            
            def CONFIRM():
                username = self.username_input.text()
                passwd = self.Password1_input.text()
                
                def completedPOP():
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        'User ' + username + ' has been successfully added to system.')
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.close()
                
                # Need to make error message if could not add user. Currently popup will still activate
                # announcing success even if the command failed.
                if self.adminyn == 'y':
                    print('This user will be an admin')
                    if Check_Password(self.Password1_input.text(),
                                      self.Password2_input.text()):
                        sub.Popen(f"sudo useradd -G users,admin,sudo -m -d /home/{username} -p $(echo {passwd} | openssl passwd -1 -stdin) {username}", shell=True)
                        sub.Popen(f"sudo echo '%/# User privelage specfication\na\n{username}    ALL=(ALL:ALL) ALL\n.\nwq' | ed /etc/sudoers", shell=True)
                        log.info(f"User {username} has been successfully added!")
                        completedPOP()
                elif self.adminyn == 'n':
                    log.info('This user will not be an admin')
                    if Check_Password(self.Password1_input.text(),
                                      self.Password2_input.text()):
                        output = sub.Popen(f"echo '{passwd}' | openssl passwd -1 -stdin", stdout=sub.PIPE, shell=True).communicate()[0].decode("utf-8").split("\n")
                        sub.Popen(f"useradd -g users -m -d /home/{username} -p '{output[0]}' {username}", shell=True)
                        log.info(f"User {username} has been successfully added!")
                        completedPOP()
            
            def cancel_button():
                self.close()
            
            self.Confirm_button.clicked.connect(lambda: NewThread(CONFIRM, False, "Adding User"))
            self.Cancel_button.clicked.connect(cancel_button)
    
        def begin(self):
            super(add_user_to_system, self).exec_()

    auts = add_user_to_system()
    NewThread(auts.begin, False, "Add User To System")


def Linux_remusr():
    class remove_user_from_system(QDialog, Ui_rmvusrogru):
        def __init__(self, parent = None):
            super(remove_user_from_system, self).__init__(parent)
            self.setWindowIcon(QtGui.QIcon(':/Pictures/images/cup2.png'))
            self.setFixedSize(302, 410)
            self.setupUi(self)
            self.EXECUTE()
        
        def EXECUTE(self):
            self.setWindowTitle('Remove User From System')
            self.label.setText('Current Users:')
            self.label2.setText('Username: ')
            
            listo_names = Linux_Find_Names()[2]
           
            for _, name in enumerate(listo_names):
                QListWidgetItem(name, self.listOFnames)
            
            def removal():
                username = self.Name_Input.text()
                
                def completedPOP(username):
                    COMPLETE = QMessageBox()
                    COMPLETE.setIcon(QMessageBox.Question)
                    COMPLETE.setWindowTitle('Hey! Listen!')
                    COMPLETE.setText(
                        'User ' + username + ' has been successfully removed from the system.')
                    COMPLETE.setStandardButtons(QMessageBox.Close)
                    COMPLETE.exec_()
                    self.listOFnames.clear()
                    self.Name_Input.clear()
                    for _, name in enumerate(listo_names):
                        QListWidgetItem(name, self.listOFnames)
                
                if len(username) == 0:
                    print('no username entered')
                    ERROR_NO_USER = QMessageBox()
                    ERROR_NO_USER.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER.setText(
                        'No username was entered. No user was removed.')
                    ERROR_NO_USER.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER.exec_()
                elif username not in listo_names:
                    print('User not found')
                    ERROR_NO_USER_FOUND = QMessageBox()
                    ERROR_NO_USER_FOUND.setIcon(QMessageBox.Warning)
                    ERROR_NO_USER_FOUND.setWindowTitle('Hey! Listen!')
                    ERROR_NO_USER_FOUND.setText(
                        'User was not found on system. No user was removed.')
                    ERROR_NO_USER_FOUND.setStandardButtons(QMessageBox.Close)
                    ERROR_NO_USER_FOUND.exec_()
                else:
                    sub.Popen(f"sudo killall -u {username}", shell=True)
                    sub.Popen(f"sudo userdel -f -r {username}", shell=True)
                    completedPOP(username)
            
            def confirmation():
                CONFIRM = QMessageBox()
                CONFIRM.setWindowTitle('Hey! Listen!')
                CONFIRM.setText("Hey! Are you sure you want to do this?")
                CONFIRM.setIcon(QMessageBox.Question)
                CONFIRM.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                CONFIRM.setWindowIcon(QtGui.QIcon(':/Pictures/images/HEY.png'))
                x = CONFIRM.exec_()
                if x == QMessageBox.Yes:
                    print('Removing user...')
                    removal()
                elif x == QMessageBox.No:
                    print('Cancelling...')
            
            def cancel_button():
                self.close()
            
            self.Cancel_button.clicked.connect(cancel_button)
            self.Confirm_button.clicked.connect(lambda: confirmation())
    
        def begin(self):
            super(remove_user_from_system, self).exec_()

    rufg = remove_user_from_system()
    NewThread(rufg.begin, False, "Remove User From System")

