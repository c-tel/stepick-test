sudo unlink /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 hello:app