import socket
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer



IP_DDRESS = "127.0.0.1"
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
client = {}


def ftp():
    global IP_ADDRESS

    authorizer = DummyAuthorizer
    authorizer.add_user("lftpd" , "lftpd",".", perm = "elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    ftp_server = FTPServer((IP_ADDRESS, 21), handler)
    ftp_server.serve_forever()

setup_thread = Thread(target = setup)
setup_thread.start()

ftp_thread = Thread(target = ftp)
ftp_thread.start()


def setup():
    print("\n\t\t\t\t\t\t IP MESSANGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_DDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS")
    print("\n")

    acceptConnections()

    setup_thread = Thread(target = setup)
    setup_thread.start()

    def acceptConnections():
        global SERVER
        global client

        while True:
            client, addr = SERVER .accept()
            client_name = client.recv(4096).decode().lower()
            clients[client_name] = {
                "Client"             : client,
                "address"            : addr,
                "connected_with"     : "",
                "file_Name"          : "",
                "file_size"          : 4096
            }

            print(f"Connection established with (client_name) : (addr)")

            thread = Thread(target = handleClient, args = (client , client_name,))
            thread.start()