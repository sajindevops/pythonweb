#!/bin/bash
cd /opt/maindir
python3 manage.py makemigrations<<EOF
Y
EOF
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9000