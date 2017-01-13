import requests

r = requests.get('http://192.168.0.42/controller/controller_login.php?username=maya&password=hi')

print r.status_code
# ' or'1'='1

# for objet in r.headers:
#     print objet +': '+ r.headers[objet]
