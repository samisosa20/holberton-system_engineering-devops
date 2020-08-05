# Install Nginx and config Nginx

exec { 'add-apt-repository':
	command => "/usr/bin/add-apt-repository ppa:nginx/stable"
}

exec { 'apt-update':
	command => "/usr/bin/apt-get update -y"
}

package { 'nginx':
	ensure => installed,
	provider => 'apt',
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  mode    => '0731',
  owner   => 'root',
  group   => 'root',
  content => 'server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /etc/nginx/html;
     index       index.html index.htm;
	 location /redirect_me {
        return 301 http://cuberule.com/;
     }
	}'
}

file { '/etc/nginx/html':
  ensure  => directory,
  path    => '/etc/nginx/html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/etc/nginx/html/index.html':
  ensure  => file,
  path    => '/etc/nginx/html/index.html',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'Holberton School'
}

exec { 'service-restart-nginx':
	command => "/usr/sbin/service nginx restart"
}
