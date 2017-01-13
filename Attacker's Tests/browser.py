import requests

r = requests.get('http://192.168.0.42')
# ' or'1'='1

for objet in r.headers:
    print objet +': '+ r.headers[objet]
