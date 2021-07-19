#!/usr/bin/env bash
## To be edited to reflect Mongo setup on a separate server to the website

# *** edit wget and echo below to reflect the correct mongo and linux versions ***
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

# get Linux version
cat /proc/version

# echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update

sudo apt-get install -y mongodb-org

service mongod start
service mongod status

systemctl enable mongod

# Error status=14 on install
chown -R mongodb:mongodb /var/lib/mongodb
chown mongodb:mongodb /tmp/mongodb-27017.sock

# to remove
sudo apt remove mongodb
sudo apt purge mongodb
sudo apt autoremove

# ** secure the db **

# create a self signed certificate
cd /etc/ssl
openssl req -newkey rsa:2048 -new -x509 -days 3650 -nodes -out mongodb-cert.crt -keyout mongodb-cert.key
cat mongodb-cert.key mongodb-cert.crt > mongodb.pem

# edit the mongo config
nano /etc/mongod.conf

net:
  port: 10042
  ssl:
    mode: requireSSL
    PEMKeyFile: /etc/ssl/mongodb.pem

# restart mongo
service mongod restart

# connect with:
mongo --port 10042 --sslAllowInvalidCertificates --ssl

# generate a password
print('another-password-{}'.format(uuid.uuid4()))

# add the password to the .env file

# while connected to the database:
use admin
db.createUser({user: "all_mongo_admin", pwd: "pw", roles: ["userAdminAnyDatabase", "readWriteAnyDatabase", "dbAdminAnyDatabase", "clusterAdmin"]})

# if need to change password
db.changeUserPassword("user", "password")

# edit mongod.conf again
security:
  authorization: enabled

# restart mongo again
service mongod restart

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Done >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

mongo --port 10042 --sslAllowInvalidCertificates --ssl -u all_mongo_admin -p the pw HERE --authenticationDatabase admin

mongodump --port=10042 --sslAllowInvalidCertificates --ssl --username=all_mongo_admin -p=password --authenticationDatabase=admin --db=sk

mongorestore --port=10001 --sslAllowInvalidCertificates --ssl --username=all_mongo_admin -p=password --authenticationDatabase=admin --db=sk dump\sk
mongorestore --port=10002 --db=salt dump\salt

ssh -f root@157.245.225.59 -L 10001:localhost:27017 -N
mongo --port 10001
mongorestore --port 10001 --db salt dump\salt