#!/bin/bash

echo 'stopping app...'

PYTHON_PID_NAME=python
cat $PYTHON_PID_NAME.pid | xargs kill