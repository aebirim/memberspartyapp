#!/bin/bash

echo 'installing python packages...'
pip install -r requirements.txt

echo 'launching app...'
python app.py >> log.txt 2>&1 &

