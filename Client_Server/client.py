import socket

HOST = '127.0.0.1'
PORT = 65432

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to server")
    message = input("Enter message to send :")
    if message == "exit":
        break
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024)
    print(f"Received response :{response.decode()}")
    
