#!/bin/bash


mkdir .config/dashboard
cp ./config/config.yaml .config/dashboard/config.yaml
python3 -m venv env

source ./env/bin/activate

#python -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt --break-system-packages