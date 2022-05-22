# Puppet manifest - preprares web server for deploy, update, install nginx
# create some needed directorys, files and symbolic link
exec { 'apt-get-update':
  command  => '/usr/bin/env apt-get -y update',
  provider => shell,
}
exec {'b':
  command  => '/usr/bin/env apt-get -y install nginx',
  provider => shell,
}
exec {'c':
  command  => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
  provider => shell,
}
exec {'d':
  command  => '/usr/bin/env mkdir -p /data/web_static/shared/',
  provider => shell,
}
exec {'e':
  command  => '/usr/bin/env echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html',
  provider => shell,
}
exec {'f':
  command  => '/usr/bin/env chown -R ubuntu:ubuntu /data',
  provider => shell,
}
exec {'g':
  command  => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}
exec {'h':
  command  => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  provider => shell,
}
exec {'i':
  command  => '/usr/bin/env service nginx restart',
  provider => shell,
}
