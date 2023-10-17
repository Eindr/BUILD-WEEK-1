import socket

# Funzione per eseguire la scansione di una singola porta su un host specifico
def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creazione del socket
        sock.settimeout(1)  # Impostazione del timeout di connessione a 1 secondo
        result = sock.connect_ex((host, port))  # Tentativo di connessione alla porta specificata
        if result == 0:  # Se la connessione ha successo, la porta è aperta
            return True
        else:
            return False
    except Exception as e:
        print(f"Si è verificato un errore durante la scansione della porta {port}: {e}")
        return False

# Funzione per verificare i servizi attivi su una lista di porte
def check_services(host, ports):
    open_ports = []  # Lista delle porte aperte
    services = {}  # Dizionario che mappa le porte ai relativi servizi
    for port in ports:
        if port_scan(host, port):  # Se la porta è aperta, aggiungi alla lista delle porte aperte
            open_ports.append(port)
            try:
                service = socket.getservbyport(port)  # Ottieni il nome del servizio associato alla porta
                services[port] = service  # Aggiungi il servizio al dizionario dei servizi
            except:
                services[port] = "Servizio sconosciuto"  # Se il servizio non è noto, inserisci "Servizio sconosciuto"
    return services  # Restituisci la lista delle porte aperte e il dizionario dei servizi

if __name__ == "__main__":
   #host = input("Inserisci l'indirizzo IP o il nome host da scansionare: ")  # Input dell'host da scansionare
    host = "172.20.10.10"
    start_port = int(input("Inserisci la porta di partenza: "))  # Input della porta di partenza
    end_port = int(input("Inserisci la porta di fine: "))  # Input della porta di fine
    ports = range(start_port, end_port+1)  # Genera una sequenza di porte da partenza a fine

    services = check_services(host, ports)  # Esegue la scansione dei servizi attivi sulle porte specificate

    if services:  # Se ci sono porte aperte, stampa i relativi servizi
        print(f"I seguenti servizi sono attivi su {host}:")
        for port in services.keys():
            print(f"Porta {port}: {services[port]}")
    else:  # Se non ci sono porte aperte, stampa un messaggio appropriato
        print(f"Nessun servizio attivo rilevato su {host} nella gamma di porte scansionata.")
