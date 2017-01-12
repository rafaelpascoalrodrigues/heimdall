#!/bin/bash

# Create directory
if [ ! -d /usr/lib/heimdall ]; then
  mkdir -p /usr/lib/heimdall
fi

# Copy all files
cp -r . /usr/lib/heimdall/

cd /usr/lib/heimdall

# Create user and give permissions to services
useradd heimdall

chown -R heimdall.heimdall *
chmod 744 monitors/*

# Configure Database
mysql -e "CREATE DATABASE heimdall;"
mysql -e "CREATE USER 'heimdall'@'localhost' IDENTIFIED BY 'heimdall';"
mysql -e "GRANT ALL PRIVILEGES ON heimdall.* TO 'heimdall'@'localhost' IDENTIFIED BY 'heimdall';"
mysql -e "FLUSH PRIVILEGES;"

chmod 744 configure.py
./configure.py