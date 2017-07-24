sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py   /etc/gunicorn.d/hello.py
gunicorn -b 0.0.0.0:8080 hello:app
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿