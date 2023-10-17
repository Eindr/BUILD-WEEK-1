tgt = '172.20.10.10'



for m in methods:
  
    if (m == "DELETE"): continue
    if (m == "OPTIONS" or m == "TRACE" or m == "ASD"): 
        req = requests.request(m, 'http://172.20.10.10/dvwa/*')
    else:
        req = requests.request(m, 'http://172.20.10.10/dvwa/login.php')

    print(m)
    if (m == 'OPTIONS'):
        print(req.headers['allow'])

    print(req.status_code)
    print()

for m in methods:
   
    if (m == "DELETE"): continue
    req = requests.request(m, 'http://172.20.10.10/phpMyAdmin/*')
  

    print(m)
    if (m == 'OPTIONS'):
        print(req.headers['allow'])