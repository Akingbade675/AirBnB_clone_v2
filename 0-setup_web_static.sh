#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install nginx if it's not already installed
if !( which nginx >/dev/null );
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    echo -e "\e[1;34m Nginx installed successfully\e[0m"
    sudo ufw allow 'Nginx HTTP'
fi;

# creates folders and file if not exists
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;34m Folders created\e[0m"

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chmod -R 755 /data/web_static/releases/test/

# with simple content, to test your Nginx configuration
echo "Hello World!
I am Abdulbasit
I did this and
I am so happy of my progress" > /data/web_static/releases/test/index.html

# creates a symlink
# If the symbolic link already exists,
# it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test/ /data/web_static/current
echo -e "\e[1;34Symlink /data/web/static/current \
-> /data/web_static/releases/test/"

sudo chown -hR ubuntu:ubuntu /data

# Update the Nginx configuration to serve the 
# content of /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static).
server_block="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root /var/www/html/;
    index index.html index.htm index.nginx_debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://youtube.com/devbhobo/;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404.html {
        internal;
    }
}
"
echo "$server_block" > /etc/nginx/sites-available/hbnb_static
ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/default

if pgrep -x "nginx" > /dev/null
then
    sudo service nginx restart
else
    sudo service nginx start
fi;
