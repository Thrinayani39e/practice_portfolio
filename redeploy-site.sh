#!/bin/bash

# Kill tmux
tmux kill-server

# Move to the project folder
cd /root/practice_portfolio

# Fetch latest changes
git fetch && git reset origin/main --hard

# Activate using the correct folder name
source /root/practice_portfolio/python3-virtualenv/bin/activate

# Install requirements
/root/practice_portfolio/python3-virtualenv/bin/pip install -r requirements.txt

# Start Flask
tmux new-session -d -s flask-session 'source /root/practice_portfolio/python3-virtualenv/bin/activate && export FLASK_APP=app && flask run --host=0.0.0.0'
