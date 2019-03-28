# Docker

## Installation

```bash
sudo yum install -y yum-utils lvm2 device-mapper-persistent-data

rpm -qa | grep -e yum-utils -e lvm2 -e device-mapper-persistent-data

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

ls /etc/yum.repos.d/ | grep docker

sudo yum install -y docker-ce

sudo systemctl enable docker

sudo systemctl start docker

sudo usermod -a -G docker user

grep docker /etc/group
```

## Verification

Logout and login again

```bash
docker run hello-world

docker pull alpine:latest

docker images | grep alpine

docker pull nginx:1.15

docker images | grep nginx

docker history nginx:1.15

docker run -it --name="test_ssh" -p 8022:22 docker.io/centos:6 /bin/bash

```

### Make changes to a docker images

```bash
docker pull ubuntu

docker run -it ubuntu /bin/bash

# Install required software

apt install python

exit

# Make changes persistent

docker commit -m "install python" -a "amauryq@mail.com" <id|name> amauryq/ubuntu_python:v1

docker images

# The new image must be shown

docker run -it amauryq/ubuntu_python:v1 /bin/bash

# Verify python is already installed

python --version
```