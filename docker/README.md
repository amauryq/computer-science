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

#### Directly creating or modifying an image

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

#### Using a Dockerfile

Create a Dockerfile
```bash
# This is a custom docker image with telnet and openssh server installed
FROM ubuntu:xenial
MAINTAINER Amaury Quintero <amauryq@gmail.com>
RUN apt update
RUN apt install -y telnet openssh-server
```

Build the image and run

```bash
docker build -t "amauryq/ubuntu_telnet_ssh:v2" .

# The new docker images must be available and you can run it

docker run -it amauryq/ubuntu_telnet_ssh:v2 /bin/bash
```

## Exposing our Container with Port Redirects

**Pull the image and run it**
```bash
docker pull nginx:latest
docker run -d nginx:latest
```

**Look for the container IP address**
```bash
docker inspect <id|name> | grep IP
```

**This works**
```bash
elinks http://172.17.0.2
```

**This doesn't work because ports are note exposed**
```bash
elinks http://localhost
```

**Expose ports**
```bash
docker run -d -p 80:80 nginx:latest
```

**Now using localhost works**

## Docker Useful Commands

```bash
docker version
docker info
docker ps -a
docker pull
docker images
docker inspect
docker run 
docker restart
docker rm
docker rmi
```

## TODO

```bash
docker run -i -t -d ubuntu:xenial /bin/bash
docker attach <id|name>

exit inside the container stop the container use
docker restart 

docker ps -a
docker logs <id|name>

# execute a command in a running docker
docker exec <id|name> /bin/cat /etc/profile
docker stop <id|name>

docker run <id|name> echo "Hello from a container"
docker restart <id|name>
docker log <id|name>

docker run -d ubuntu:xenial /bin/bash -c "while true;do echo Hello;sleep 1;done"
docker logs <id|name> | wc -l # check if lines count are increasing
```
