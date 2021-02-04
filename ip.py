import urllib.request
ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode('gbk')
print (ip)