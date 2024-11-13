import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

def client_handler(client_socket, client_address):
    print(f"Connected to {client_address}:{client_socket}")
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message Received from {client_address}: {data.decode()}")
            client_socket.sendall(data)
        except ConnectionResetError:
            print("Connection with {client_address} terminated forcefully.")
            break
    
    client_socket.close()
    print(f"Client Connection closed.")
    
def startServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    print(f"Server listening on {HOST}/{PORT}")
    server.listen()
    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target = client_handler, args = (client_socket, client_address))
        client_thread.start()
        print(f"Started thread for {client_address}")
    
startServer()