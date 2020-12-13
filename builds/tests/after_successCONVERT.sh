#!/bin/bash

setup_git() {
    git config --global user.email "travis@travis-ci.org"
    git config --global user.name "Travis CI"
}

commit_compiled_executables() {

    if [ $TRAVIS_BRANCH = dev ]; then
        git checkout dev
        echo "checked out dev"
        echo "./dist directory BEFORE"
        ls ./dist
        echo "./builds directory BEFORE"
        ls ./builds
        if [ $TRAVIS_OS_NAME = 'windows' ]; then
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
        if [ $TRAVIS_OS_NAME = 'linux' ]; then
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
        if [ $TRAVIS_OS_NAME = 'osx' ]; then
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
        git commit --message "[skip travis-ci] Travis build: $TRAVIS_BUILD_NUMBER"
        echo "git committed created. Ready to push"
    elif [ $TRAVIS_BRANCH = master ]; then
        git checkout master
        echo "checked out master"
        echo "./dist directory BEFORE"
        ls ./dist
        echo "./builds directory BEFORE"
        ls ./builds
        if [ $TRAVIS_OS_NAME = 'windows' ]; then
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
        if [ $TRAVIS_OS_NAME = 'linux' ]; then
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
        if [ $TRAVIS_OS_NAME = 'osx' ]; then
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
        git commit --message "[skip travis-ci] Travis build: $TRAVIS_BUILD_NUMBER"
        echo "git committed created. Ready to push"
    fi
}

upload_files() {
    if [ $TRAVIS_BRANCH = dev ]; then
        git push -f -q https://vipersniper0501:${GH_TOKEN}@github.com/vipersniper0501/CP_Scripts2.git dev
        echo "Pushed to dev"
    elif [ $TRAVIS_BRANCH = master ]; then
        git push -f -q https://vipersniper0501:${GH_TOKEN}@github.com/vipersniper0501/CP_Scripts2.git master
        echo "Pushed to master"
    fi
}

#if [ $TRAVIS_OS_NAME = 'osx' ]; then
#    echo "This is not a windows or linux machine. Will not upload to github yet"
#else
setup_git
commit_compiled_executables
upload_files
#fi
