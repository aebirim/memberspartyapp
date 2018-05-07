#!/bin/bash

echo 'installing python packages...'
pip install -r requirements.txt

echo 'launching app...'

PYTHON_PID_NAME=python

python app.py >> log.txt 2>&1 &

PID=$!

echo $PID > $PYTHON_PID_NAME.pid

