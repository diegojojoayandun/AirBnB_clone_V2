# Puppet manifest - preprares web server for deploy, update, install nginx
# create some needed directorys, files and symbolic link
exec { 'apt-get-update':
  command => 'apt-get -y update',
  path    => '/usr/bin/env',
}
exec {'Install Nginx':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin/env',
}
exec {'Create test directory':
  command => 'mkdir -p /data/web_static/releases/test/',
  path    => '/usr/bin/env',
}
exec {'Create shared directory':
  command => 'mkdir -p /data/web_static/shared/',
  path    => '/usr/bin/env',
}
exec {'create index.html':
  command => 'echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html',
  path    => '/usr/bin/env',
}
exec {'changed ownership':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/usr/bin/env',
}
exec {'create symbolic link':
  command => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  path    => '/usr/bin/env',
}
exec {'change default':
  command => 'sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  path    => '/usr/bin/env',
}
exec {'restart nginx sevice':
  command => 'service nginx restart',
  path    => '/usr/bin/env',
}
