#!/bin/bash
cd /opt/todo-app
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 app.py