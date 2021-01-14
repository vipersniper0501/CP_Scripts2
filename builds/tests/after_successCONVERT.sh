#!/bin/bash

OS_Name="$1"


setup_git() {
    git config --global user.email "github@github-actions.org"
    git config --global user.name "Runner"
}

commit_compiled_executables() {

    Branch_Name=$(git rev-parse --abbrev-ref HEAD)
    Branch_Commit_Number=$(git rev-list --count $Branch_Name)

    echo "Branch Name: $Branch_Name"
    echo "Branch Commit Number: $Branch_Commit_Number"
    echo "OS Name: $OS_Name"

    if [ $Branch_Name = dev ]; then
        git checkout dev
        echo "checked out dev"
        echo "./dist directory BEFORE"
        ls ./dist
        echo "./builds directory BEFORE"
        ls ./builds
        if [ $OS_Name = 'windows' ]; then
            mv "./dist/AppleCIDR_Windows_x64.exe" "./builds/PyQt5_Executables/AppleCIDR_Windows_x64.exe"
            echo "Moved AppleCIDR_Windows_x64.exe from ./dist to ./builds"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            git pull
            git add "./builds"
            git status
        fi
        if [ $OS_Name = 'linux' ]; then
            mv "./dist/AppleCIDR_Linux_x64" "./builds/PyQt5_Executables/AppleCIDR_Linux_x64"
            echo "Moved AppleCIDR_Linux_x64 from ./dist to ./builds"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            chmod +x "./builds/PyQt5_Executables/AppleCIDR_Linux_x64"
            git pull
            git add "./builds"
            git status
        fi
        if [ $OS_Name = 'osx' ]; then
            mv "./dist/AppleCIDR_MacOS_x64" "./builds/PyQt5_Executables/AppleCIDR_MacOS_x64"
            echo "Moved AppleCIDR_MacOS_x64 from ./dist to ./builds/PyQt5_Executables/"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            chmod +x "./builds/PyQt5_Executables/AppleCIDR_MacOS_x64"
            git pull
            git add "./builds"
            git status
        fi
        git commit --message "Branch: $Branch_Name, Build Number [$Branch_Commit_Number]"
        echo "git committed created. Ready to push"
    elif [ $Branch_Name = master ]; then
        git checkout master
        echo "checked out master"
        echo "./dist directory BEFORE"
        ls ./dist
        echo "./builds directory BEFORE"
        ls ./builds
        if [ $OS_Name = 'windows' ]; then
            mv "./dist/AppleCIDR_Windows_x64.exe" "./builds/PyQt5_Executables/AppleCIDR_Windows_x64.exe"
            echo "Moved AppleCIDR_Windows_x64.exe from ./dist to ./builds"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            git pull
            git add "./builds"
            git status
        fi
        if [ $OS_Name = 'linux' ]; then
            mv "./dist/AppleCIDR_Linux_x64" "./builds/PyQt5_Executables/AppleCIDR_Linux_x64"
            echo "Moved AppleCIDR_Linux_x64 from ./dist to ./builds"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            chmod +x "./builds/PyQt5_Executables/AppleCIDR_Linux_x64"
            git pull
            git add "./builds"
            git status
        fi
        if [ $OS_Name = 'osx' ]; then
            mv "./dist/AppleCIDR_MacOS_x64" "./builds/PyQt5_Executables/AppleCIDR_MacOS_x64"
            echo "Moved AppleCIDR_MacOS_x64 from ./dist to ./builds/PyQt5_Executables/"
            echo "./dist directory AFTER"
            ls ./dist
            echo "./builds directory AFTER"
            ls ./builds/PyQt5_Executables
            chmod +x "./builds/PyQt5_Executables/AppleCIDR_MacOS_x64"
            git pull
            git add "./builds"
            git status
        fi
        git commit --message "Branch: $Branch_Name, Build Number [$Branch_Commit_Number]"
        echo "git committed created. Ready to push"
    fi
}

upload_files() {
    if [ $Branch_Name = dev ]; then
        git push -f -q https://vipersniper0501:${GH_TOKEN_DEV}@github.com/vipersniper0501/CP_Scripts2.git dev
        echo "Pushed to dev"
    elif [ $Branch_Name = master ]; then
        git push -f -q https://vipersniper0501:${GH_TOKEN_DEV}@github.com/vipersniper0501/CP_Scripts2.git master
        echo "Pushed to master"
    fi
}

setup_git
commit_compiled_executables
upload_files
