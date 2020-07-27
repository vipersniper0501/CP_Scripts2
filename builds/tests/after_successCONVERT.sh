#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_compiled_executables() {
  if [ $TRAVIS_OS_NAME = 'windows' ]; then
    git checkout GUI-Updates
    echo "checked out GUI-Updates"
    mv ./dist/AppleCIDR.exe ./builds/AppleCIDR.exe
    echo "Moved AppleCIDR.exe from ./dist to ./builds"
    git add ./builds/AppleCIDR.exe
    echo "Added AppleCIDR.exe to commit"
    git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
    echo "git committed created. Ready to push"
  fi
}

upload_files() {
  git branch --show-current
  git push -f -q https://${GH_TOKEN}@github.com/vipersniper0501/CP_Scripts2.git GUI-Updates
  # echo "Remote add GUI-Updates"
  # git push
  echo "Pushed to GUI-Updates"
}

if [ $TRAVIS_OS_NAME = 'windows' ]; then
    setup_git
    commit_compiled_executables
    upload_files
else
    echo "This is not a windows machine. Will not upload to github yet"
fi
