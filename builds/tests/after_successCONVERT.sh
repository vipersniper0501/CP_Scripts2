#!/bin/bash

setup_git() {
    git config --global user.email "travis@travis-ci.org"
    git config --global user.name "Travis CI"
}

commit_compiled_executables() {

    git checkout GUI-Updates
    echo "checked out GUI-Updates"
    echo "./dist directory BEFORE"
    ls ./dist
    echo "./builds directory BEFORE"
    ls ./builds
    if [ $TRAVIS_OS_NAME = 'windows' ]; then
        mv "./dist/AppleCIDR_Windows_x64" "./builds/AppleCIDR_Windows_x64"
        echo "Moved AppleCIDR_Windows_x64 from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        git add "./builds/AppleCIDR_Windows_x64"
        git status
    elif [ $TRAVIS_OS_NAME = 'linux' ]; then
        mv "./dist/AppleCIDR_Linux_x64" "./builds/AppleCIDR_Linux_x64"
        echo "Moved AppleCIDR_Linux_x64 from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        chmod +x "./builds/AppleCIDR_Linux_x64"
        git add "./builds/AppleCIDR_Linux_x64"
        git status
    elif [ $TRAVIS_OS_NAME = 'osx' ]; then
        mv "./dist/AppleCIDR_MacOS_x64" "./builds/AppleCIDR_MacOS_x64"
        echo "Moved AppleCIDR_MacOS_x64 from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        chmod +x "./builds/AppleCIDR_MacOS_x64"
        git add "./builds/AppleCIDR_MacOS_x64"
        git status
    fi
    git commit --message "[skip travis-ci] Travis build: $TRAVIS_BUILD_NUMBER"
    echo "git committed created. Ready to push"
}

upload_files() {
    git push -f -q https://vipersniper0501:${GH_TOKEN}@github.com/vipersniper0501/CP_Scripts2.git GUI-Updates
    echo "Pushed to GUI-Updates"
}

#if [ $TRAVIS_OS_NAME = 'osx' ]; then
#    echo "This is not a windows or linux machine. Will not upload to github yet"
#else
setup_git
commit_compiled_executables
upload_files
#fi
