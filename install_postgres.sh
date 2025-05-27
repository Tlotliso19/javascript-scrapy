#!/bin/bash
set -e

# Update package list
sudo apt update

# Add PostgreSQL repository for your distro
sudo sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main' > /etc/apt/sources.list.d/pgdg.list"

# Add the PostgreSQL signing key
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc > /dev/null

# Update package list again after adding new repo
sudo apt update

# Install PostgreSQL server and client
sudo apt install -y postgresql postgresql-client

# Check psql version
psql --version


sudo apt update
sudo apt install dnsutils -y

