#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv

# Stop the hackers
sudo apt install fail2ban -y

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable


apt install acl -y
useradd -M apiuser
usermod -L apiuser


# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/weather_api
mkdir /apps/logs/weather_api/app_log
# chmod 777 /apps/logs/weather_api
setfacl -m u:apiuser:rwx /apps/logs/weather_api
# cd /apps

# NEXT upgrade Python and run setup_B
# Create a virtual env for the app.

