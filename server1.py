import socket
import threading
from final_RSA import encrypt as encrypt2 , decrypt as decrypt2 , generate_key_pair as generate_key_pair2

n1=0
n2=0
e=0
d=0

with open("keys.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            n1 = int(line)
        elif i == 1:
            e = int(line)
        elif i == 2:
            n2 = int(line)
        elif i == 3:
            d = int(line)
        elif i > 3:
            break

f.close()

public_key = (n1, e)
private_key = (n2, d)

def receive_message(sock):
    while True:
        message = sock.recv(1024).decode()
        decrypted_plaintext = decrypt2(int(message), private_key)
        print(f"Received message: {decrypted_plaintext}")

def send_message(sock):
    while True:
        message = input("Enter message: ")
        ciphertext = encrypt2(message, public_key)
        sock.send(repr(ciphertext).encode())

if __name__ == "__main__":
    # Create a socket object
    s = socket.socket()

    # Get local machine name
    host = socket.gethostname()

    # Reserve a port for your service.
    port = 12345

    # Bind the socket to a public host, and a well-known port
    s.bind((host, port))

    # Listen for incoming connections
    s.listen(1)

    print(f"Waiting for incoming connections on {host}:{port}...")

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection established with {addr[0]}:{addr[1]}")

    # Start threads to send and receive messages
    receive_thread = threading.Thread(target=receive_message, args=(conn,))
    send_thread = threading.Thread(target=send_message, args=(conn,))
    receive_thread.start()
    send_thread.start()