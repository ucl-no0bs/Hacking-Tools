import requests

r = requests.get('http://192.168.0.42/controller/controller_login.php?username=maya&password=hi')
s = requests.get('http://192.168.0.42/model/model_home.php?username=maya&snippet=yoyoyoy&isPublic=0')
print s.status_code

url = 'http://192.168.0.42/controller/controller_login.php?username='+'maya'+'&password='+'hi'
r = requests.get(url)
if 'abc' in r.text:
    print 'nope'
else:
    print 'yes'
# if "blah" in "blahaaaaa":
#     print 'woo'
# if 'abc' in r.text:
#     print "nope"
# else:
#     print "yes"

# ' or'1'='1

# for objet in r.headers:
#     print objet +': '+ r.headers[objet]
