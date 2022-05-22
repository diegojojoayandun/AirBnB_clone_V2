# Puppet manifest - preprares web server for deploy, update, install nginx
# create some needed directorys, files and symbolic link
exec { 'apt-get-update':
  command => 'apt-get -y update',
  path    => '/usr/sbin/env',
}
exec {'Install Nginx':
  command => 'apt-get -y install nginx',
  path    => '/usr/sbin/env',
}
exec {'Create test directory':
  command => 'mkdir -p /data/web_static/releases/test/',
  path    => '/usr/sbin/env',
}
exec {'Create shared directory':
  command => 'mkdir -p /data/web_static/shared/',
  path    => '/usr/sbin/env',
}
exec {'create index.html':
  command => 'echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html',
  path    => '/usr/sbin/env',
}
exec {'changed ownership':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/usr/sbin/env',
}
exec {'create symbolic link':
  command => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  path    => '/usr/sbin/env',
}
exec {'change default':
  command => 'sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  path    => '/usr/sbin/env',
}
exec {'restart nginx sevice':
  command => 'service nginx restart',
  path    => '/usr/sbin/env',
}
