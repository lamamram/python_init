from socket import *
import threading
from time import sleep
from crypto.caesar import *

key = generate_key()

# création et démarrage du serveur TCP 
def server_start():
    # socket réseau TCP
    server = socket(AF_INET, SOCK_STREAM)
    # socket réseau UDP
    # server = socket(AF_INET, SOCK_DGRAM)
    # détermination de la scoket (ip + port)
    server.bind(('127.0.0.1', 26026))
    # on détermine la profondeur de a file d'attente des connexions
    server.listen(5)
    print("server started")
    return server


def server_accept(server):
    # attente d'une connexion (socket client)
    conn, addr = server.accept()

    # ouverture de la connexion
    with conn:
        # boucle de réception des données
        while True:
            s_data = conn.recv(1024)
            clear_msg = uncrypt(s_data.decode('utf-8'), key)
            
            # condition d'arrêt du serveur
            if clear_msg == "quit": break
            
            print(f"server received: {clear_msg} from {addr}")
            conn.send(bytes(crypt(f"{clear_msg}bienrecu", key), "utf-8"))


if __name__ == "__main__":
    server = server_start()
    # (,) => tuple à 1 élément
    # on veut lancer la réception de socket client dans un thread
    thread = threading.Thread(target=server_accept, args=(server,))
    thread.start()

    with socket(AF_INET, SOCK_STREAM) as client:
        client.connect(('127.0.0.1', 26026))
        while True:
            msg = input("entrer message: ")
            crypted = crypt(msg, key)
            binar = bytes(crypted, "utf-8")
            
            # méthode d'envoi
            # send => envoie au + le paramètre int octets et retourne le nb d'octets envoyés
            client.send(binar)
            # sendall => boucle sur send jusqu'à envoi total des données           
            # client.sendall(binar)
            # !! sendto => UDP


            # binaire literal
            # client.send(b"send some data\nEnd")
            if msg == "quit":
                sleep(1)
                server.close()
                break
            else:
                # !! bloquant
                s_data = client.recv(1024)
                clear_data = uncrypt(s_data.decode('utf-8'), key)
                print(f"server returned: {clear_data}")
        