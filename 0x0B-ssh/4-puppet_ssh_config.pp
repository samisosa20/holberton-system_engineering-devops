# Use Puppet for ssh_configuration
file_line { 'ssh_config':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
    multiple => true,
}
file_line {'ssh_config2':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    multiple => true,
}
