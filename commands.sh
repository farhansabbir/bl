# primary server
consul agent -server -bootstrap -bind 192.168.0.8 -dns-port 53 -ui -data-dir /var/consul -ui -domain dmarts.com -datacenter dc1 -client 0.0.0.0

# member servers
consul agent -server -retry-join 192.168.0.8 -bind 192.168.0.7 -data-dir /var/data/