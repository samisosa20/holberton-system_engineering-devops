# Create a file

file { '/tmp/holberton': # the path of the new file
    ensure => 'present', # just means that the resource should be a file, directory, or link; if it does not exist, create a file.
    content => 'I love Puppet', # this text will be inside the file
    owner => 'www-data',
    group => 'www-data',
    mode => '0744', # permission
}
