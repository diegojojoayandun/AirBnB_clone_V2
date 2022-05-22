# Puppet manifest - preprares web server for deploy, update, install nginx

exec { 'apt-get-update':
  command  => 'sudo apt-get -y update',
  provider => 'shell',
}
exec {'Install Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => 'shell',
}
exec {'Create test directory':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
}
exec {'Create shared directory':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => 'shell',
}
exec {'create index.html':
  command  => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html',
  provider => 'shell',
}
exec {'create symbolic link':
  command  => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  provider => 'shell',
}
exec {'changed ownership':
  command  => 'sudo chown -R ubuntu:ubuntu /data',
  provider => 'shell',
}
exec {'change default':
  command  => 'sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  provider => 'shell',
}
exec {'restart nginx sevice':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
