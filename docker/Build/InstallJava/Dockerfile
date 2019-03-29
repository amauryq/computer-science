# Dockerfile based on the lastest CentOS 7 image - Install Java
FROM centos:latest
LABEL maintainer="Amaury Quintero <amauryq@gmail.com>" version="1.1"

RUN useradd  -ms /bin/bash user

RUN yum update -y

USER user

RUN cd ~ && curl -v -j -k -L -H 'Cookie: oraclelicense=accept-securebackup-cookie' 'https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz' -o jdk-8u201-linux-x64.tar.gz --compressed
RUN cd ~ && tar zxvf jdk-8u201-linux-x64.tar.gz && rm jdk-8u201-linux-x64.tar.gz

ENV JAVA_HOME ~/jdk1.8.0_201/jre
ENV PATH "$PATH:$JAVA_HOME/bin"
RUN export PATH
