import socket
import threading
from final_RSA import encrypt as encrypt1 , decrypt as decrypt1 , generate_key_pair as generate_key_pair1

n1=0
n2=0
e=0
d=0

with open("keys.txt") as f:
    for i, line in enumerate(f):
        if i == 4:
            n1 = int(line)
        elif i == 5:
            e = int(line)
        elif i == 6:
            n2 = int(line)
        elif i == 7:
            d = int(line)
        elif i > 7:
            break
f.close()

public_key = (n1, e)
private_key = (n2, d)

def receive_message(sock):
    while True:
        message = sock.recv(1024).decode()
        decrypted_plaintext = decrypt1(int(message), private_key)
        print(f"Received message: {decrypted_plaintext}")

def send_message(sock):
    while True:
        message = input("Enter message: ")
        ciphertext = encrypt1(message, public_key)
        sock.send(repr(ciphertext).encode())

if __name__ == "__main__":
    # Create a socket object
    s = socket.socket()

    # Get local machine name
    host = socket.gethostname()

    # Reserve a port for your service.
    port = 12345

    # Connect to the server
    s.connect((host, port))
    
    print(f"Connected to server at {host}:{port}")

    # Start threads to send and receive messages
    receive_thread = threading.Thread(target=receive_message, args=(s,))
    send_thread = threading.Thread(target=send_message, args=(s,))
    receive_thread.start()
    send_thread.start()