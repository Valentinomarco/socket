#!/usr/bin/env python3
import socket

# lasciando il campo vuoto sarebbe la stessa cosa {localhost}
SERVER_ADDRESS = '127.0.0.1'
# Numero di porta, deve essere >1024 perchè le altre sono riservate.)
SERVER_PORT = 22224

# La funzione avvia_server crea un endpoitn di ascolto dal quale accettare connessioni in entrata
# la socket di ascolto viene passata alla funzione ricevi_comandila quale accetta richieste di connessione
# e per ognuna crea una socket per i datida cui ricevere le richieste e inviare le risposte


def ricevi_comandi(sock_listen):
    while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")
            break

            dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))
            break
             op,n1,n2 = dati.split(";")

        print(op)
        print(n1)
        print(n2)

        if(op=="piu"):
	        risultato= float(n1) + float(n2)
        elif  op=='meno':
	        risultato= float(n1) - float(n2)
        elif op=='per':
	        risultato: float(n1) * float(n2)
        elif op=='diviso':
            if n2 == '0':
                risutato= 'Divisione per zero impossibile'
            else:
                risultato= float(n1) / float(n2)
        
        print(risultato)
        dati = "Il risultato dell'operazione: " + str(op) + " tra " + str(n1) + " e " + str(n2) + "=" +str(risultato)

        dati = dati.encode()

        sock_service.send(dati)

        sock_service.close()
def avvia_server(indirizzo, porta):
    sock_listen = socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))

    ricevi_comandi(sock_listen)

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_POINT)





       