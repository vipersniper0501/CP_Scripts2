#!/bin/bash

if [ $TRAVIS_OS_NAME = 'linux' ]; then
    # Install some custom requirements on Linux
    git commit ../../README.adoc
fi