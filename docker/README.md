# Installation and Image Setup

```bash
sudo yum install -y yum-utils lvm2 device-mapper-persistent-data

rpm -qa | grep -e yum-utils -e lvm2 -e device-mapper-persistent-data

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

ls /etc/yum.repos.d/ | grep docker

sudo yum install -y docker-ce

sudo systemctl enable docker

sudo systemctl start docker

sudo usermod -a -G docker user
```
Logout and login

```bash
grep docker /etc/group
docker run hello-world
```
