import requests
#selezioniamo il target a cui mandare la richiesta 
tgt = '172.20.10.10'

#impostiamo i metodi che vogliamo controllare con l'aggiunta di ASD per verificare l'attendibilità delle risposte
methods = ["GET", "POST", "PUT", "TRACE", "OPTIONS", "ASD"]
#methods = ["GET", "POST", "PUT", "TRACE", "OPTIONS", "ASD", "DELETE"] 

#impostiamo il ciclo for per la pagina DVWA
print ("DVWA")
for m in methods:
  
    
    if (m == "OPTIONS" or m == "TRACE" or m == "ASD"): 
        req = requests.request(m, 'http://172.20.10.10/dvwa/*')
    else:
       req = requests.request(m, 'http://172.20.10.10/dvwa/login.php')  #a differenza dei metodi sopra " OPTION TRACE E ADS" mandiamo la richiesta alla pagina di login per gli altri metodi 

    print(m) #stampiamo il metodo
    if (m == 'OPTIONS'):
        print(req.headers['allow']) #stampiamo i metodi utilizzabili con OPTIONS

    print(req.status_code) #stampiamo il codice relativo al metodo
    print()

print("-----------------------------------------------------------------------------")
print("phpMyAdmin")
# impostiamo un ciclo for per la pagina phpMyAdmin
for m in methods:
    
    
    req = requests.request(m, 'http://172.20.10.10/phpMyAdmin/*') #mandiamo la richiesta al sito
  

    print(m) 
    if (m == 'OPTIONS'): #stampiamo la risposta coi metodi
        print(req.headers['allow'])

    print(req.status_code) #stampiamo il codice relativo al metodo
    print()
