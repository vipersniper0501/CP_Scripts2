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
        mv ./dist/AppleCIDR.exe ./builds/AppleCIDR.exe
        echo "Moved AppleCIDR.exe from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        git add ./builds/AppleCIDR.exe
        echo "Added AppleCIDR.exe to commit"
    elif [ $TRAVIS_OS_NAME = 'linux' ]; then
        mv "./dist/AppleCIDR(Linux_x64)" "./builds/AppleCIDR(Linux_x64)"
        echo "Moved AppleCIDR(Linux_x64) from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        git add "./builds/AppleCIDR(Linux_x64)"
        echo "Added AppleCIDR(Linux_x64) to commit"
    elif [ $TRAVIS_OS_NAME = 'osx' ]; then
        mv "./dist/AppleCIDR(MacOS_x64)" "./builds/AppleCIDR(MacOS_x64)"
        echo "Moved AppleCIDR(MacOS_x64) from ./dist to ./builds"
        echo "./dist directory AFTER"
        ls ./dist
        echo "./builds directory AFTER"
        ls ./builds
        git add "./builds/AppleCIDR(MacOS_x64)"
        echo "Added AppleCIDR(MacOS_x64) to commit"
    fi
    git commit --message "[skip travis-ci] Travis build: $TRAVIS_BUILD_NUMBER"
    echo "git committed created. Ready to push"
}

upload_files() {
    git branch --show-current
    echo "^ Is the current branch"
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
