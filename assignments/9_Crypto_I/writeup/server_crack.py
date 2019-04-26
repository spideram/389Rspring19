#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    passwords_temp = open("passwords.txt", "r").read().split('\n')# open and read passwords.txt
    passwords_temp.pop()
    characters = string.ascii_lowercase
    passwords = []
    for x in passwords_temp:
        x = x.rstrip()
        passwords.append(x)
    server_ip = '134.209.128.58'
    server_port = 1337
    counter = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while counter < 3:
        data = s.recv(1024)
        hashes = data.split('\n')
        for c in characters:
            for p in passwords:
                result = c + p
                for_hash = result.encode("utf-8")
                encrypt = hashlib.sha256(for_hash).hexdigest()
                if encrypt == hashes[2]:
                    s.send(result + "\n")
        counter = counter + 1

    data = s.recv(1024)
    print(data)
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
