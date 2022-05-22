# Puppet manifest - preprares web server for deploy, update, install nginx
# create some needed directorys, files and symbolic link
exec { 'apt-get-update':
  command  => 'apt-get -y update',
  provider => shell,
}
exec {'b':
  command  => 'apt-get -y install nginx',
  provider => shell,
}
exec {'c':
  command  => 'mkdir -p /data/web_static/releases/test/',
  provider => shell,
}
exec {'d':
  command  => 'mkdir -p /data/web_static/shared/',
  provider => shell,
}
exec {'e':
  command  => 'echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html',
  provider => shell,
}
exec {'f':
  command  => 'chown -R ubuntu:ubuntu /data',
  provider => shell,
}
exec {'g':
  command  => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}
exec {'h':
  command  => 'sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  provider => shell,
}
exec {'i':
  command  => 'service nginx restart',
  provider => shell,
}
