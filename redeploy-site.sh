#!/bin/bash

# 1. cd into your project folder
cd /root/practice_portfolio

# 2. Pull the latest changes
git fetch && git reset origin/main --hard

# 3. Enter the virtual environment and install dependencies
./python3-virtualenv/bin/pip install -r requirements.txt

# 4. Restart the myportfolio service
systemctl restart myportfolio
