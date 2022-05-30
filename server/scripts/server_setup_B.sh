#!/usr/bin/env bash

# Rin Setup_A FIRST
# Update Python

# Create a virtual env for the app.
cd /apps
python3 -m venv venv
source /apps/venv/bin/activate

# add source command to ~/.zshrc

pip install --upgrade pip setuptools wheel
pip install --upgrade httpie glances
pip install --upgrade gunicorn uvloop httptools

# clone the repo:
cd /apps

## Clone the weather API here
git clone https://github.com/talkpython/modern-apis-with-fastapi app_repo

# Setup the web app:
cd /apps/huey
pip install -r requirements.txt

# can run with python main.py and check output with http localhost:8000

## TEST the daemon start command first
# Copy and enable the daemon
cp /apps/huey/server/units/weather.service /etc/systemd/system/

systemctl start weather
systemctl status weather
systemctl enable weather

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/huey/server/nginx/weather.nginx /etc/nginx/sites-enabled/
update-rc.d nginx enable
service nginx restart


# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

## DEPRECATED
# add-apt-repository ppa:certbot/certbot
# apt install python3-certbot-nginx
# certbot --nginx -d weatherapi.talkpython.com

## NO - from https://certbot.eff.org:
sudo snap install core; sudo snap refresh core
# Install
snap install --classic
# Test the link command (?? actual intent here)
ln -s /snap/bin/certbot /usr/bin/certbot
# Install cert and configure nginx
certbot --nginx
# test automatic renewal
certbot renew --dry-run

