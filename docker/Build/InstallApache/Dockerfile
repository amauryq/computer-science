# Dockerfile based on the lastest CentOS 7 image - Install Apache
FROM centos:latest
LABEL maintainer="Amaury Quintero <amauryq@gmail.com>" version="1.0"

RUN useradd  -ms /bin/bash user

RUN yum update -y
RUN yum install -y httpd net-tools

RUN echo "Hello World from Apache Server!! " >> /var/www/html/index.html

EXPOSE 80

ENTRYPOINT apachectl "-DFOREGROUND"

## Build the image
# docker build -t centos/apache:v1 .
## Map exposed ports to the first available starting 32768
# docker run -d --name apacheweb1 -P centos/apache:v1
