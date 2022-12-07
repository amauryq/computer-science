# http server
# python -m SimpleHTTPServer 80
# python3 -m http.server 80
# custom
echo "${http_server}" > /home/${user}/http-server.b64
base64 --decode /home/${user}/http-server.b64 > /home/${user}/http-server.py
chown ${user}:${user} /home/${user}/http-server.py
chmod +x /home/${user}/http-server.py
python3 /home/${user}/http-server.py
