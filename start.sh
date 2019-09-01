#!/bin/bash

echo "start server"
source activate qz_venv

cd ./backend
#python run.py runserver
gunicorn -w 3 -D run:app

echo "start frontend"
cd ../frontend/dist
hs -p 8820 > ../../logs/news_front.log 2>&1 &