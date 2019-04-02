sudo echo "127.0.0.1 www.miami.local" >> /etc/hosts

mkdir -p /home/amauryq/Docker/Builds/Miami
cd /home/amauryq/Docker/Builds/Miami

curl  http://www.openwebdesign.org/download.phtml/151.zip?id=6387 --output 151.zip

unzip 151.zip

mv 15/ www/

# Prepare docker image

# Run containers

docker run -itd --name=devweb1 -p 8081:80 -v /home/amauryq/Docker/Builds/Miami/www/:/var/www/html centos6:serverv2 /bin/bash

docker run -itd --name=devweb2 -p 8082:80 -v /home/amauryq/Docker/Builds/Miami/www/:/var/www/html centos6:serverv2 /bin/bash

# Configure nginx

vi /etc/nginx/conf.d/miami.conf

    upstream miamiwebapp {
        server localhost:8081;
        server localhost:8082;
    }

    server {
        access_log /var/log/nginx/miamiweb.access.log;
        error_log  /var/log/nginx/miamiweb.error.log;

        listen 80;
        server_name www.miami.local;

        index index.html index.htm index.php;

        location / {
	    proxy_pass http://miamiwebapp;
        }
    }

service nginx restart
