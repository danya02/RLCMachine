# !/usr/bin/env python3

import Crypto_funcs
import socket
import time


def decryption(cipherkey, ciphertext, privkey_pem):
    aes_key = Crypto_funcs.rsa_decryption(privkey_pem, cipherkey)
    plaintext = Crypto_funcs.aes_decryption(ciphertext, aes_key)
    return plaintext


def send_to_another(HOST, PORT, message):
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #   s.connect((HOST, PORT))
    #   s.sendall(message)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    conn.send(message)
    conn.close()


def receive_from_another(HOST, PORT):
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #   s.bind((HOST, PORT))
    # s.listen()
    # conn, addr = s.accept()
    #    with conn:
    #       while True:
    #          data = conn.recv(1024)
    #         return data
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    data = (sock.recv(1024))
    sock.close()
    return data


def B_main(HOST='127.0.0.1', PORT=8000):
    privkey_pem, pubkey_pem = Crypto_funcs.rsa_keys_generate()

    send_to_another(HOST, PORT, pubkey_pem)
    time.sleep(1)

    cipherkey = receive_from_another(HOST, PORT)
    time.sleep(1)

    ciphertext = receive_from_another(HOST, PORT)

    print(decryption(cipherkey, ciphertext, privkey_pem))


HOST = 'localhost'  # The server's hostname or IP address
PORT = 8000  # The port used by the server

print('''Run this program before Alice.py
Here will be ur message from second program, u are welcome.

Your message: ''', end='')
B_main(HOST, PORT)
