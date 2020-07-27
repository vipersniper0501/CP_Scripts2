#!/bin/bash

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_compiled_executables() {
  if [ $TRAVIS_OS_NAME = 'windows' ]; then
    git checkout -b GUI-Updates
    git add ./dist/AppleCIDR.exe
    git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
  fi
}

upload_files() {
  git remote add GUI-Updates https://${GH_TOKEN}@github.com/vipersniper0501/CP_Scripts2.git
  git push GUI-Updates
}

if [ $TRAVIS_OS_NAME = 'windows' ]; then
    setup_git
    commit_compiled_executables
    upload_files
else
    echo "This is not a windows machine. Will not upload to github yet"
fi
