import requests
# arugments from command line
import argparse

parser  = argparse.ArgumentParser()
parser.add_argument('target_ip')
parser.add_argument('-p', '--port')
parser.add_argument('-P', '--protocol')
args    = parser.parse_args()

if (args.protocol == None): args.protocol = 'http'
if (args.port == None): 
    args.port = '80'
    if (args.protocol == 'https'):
        args.port = '443'

url = args.protocol + '://' + args.target_ip + ':' + args.port + '/phpMyAdmin/*'

req = requests.options(url)
print(req.headers['allow'])
