import Crypto_funcs
import socket
import time


def gen_message(text, pubkey_pem):
    aes_key = Crypto_funcs.aes_key_generate()
    ciphertext = Crypto_funcs.aes_encryption(text, aes_key)
    cipherkey = Crypto_funcs.rsa_encryption(pubkey_pem, aes_key)
    return [cipherkey, ciphertext]


def send_to_another(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SENDING_HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    conn.send(message)
    conn.close()


def receive_from_another():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((RECEIVING_HOST, PORT))
    data = (sock.recv(1024))
    sock.close()
    return data


def A_communication(message):
    your_message = message

    pubkey_pem = receive_from_another()
    time.sleep(0.05)

    finmes = gen_message(your_message, pubkey_pem)
    send_to_another(finmes[0])
    time.sleep(0.05)

    send_to_another(finmes[1])
    print('Check input of Bob.py')


SENDING_HOST = socket.gethostname()
print('Your name in network is:', SENDING_HOST)
RECEIVING_HOST = input("Type server's ip/name: ")
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

print('''
This is the second program you need to start.
Write there a message, which you want to send (only latin letters).
    ''')

text = input('Type your text: ')
A_communication(text)
