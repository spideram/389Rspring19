#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt", "r").read().split('\n')# open and read hashes.txt
    hashes.pop()
    passwords_temp = open("passwords.txt", "r").read().split('\n')# open and read passwords.txt
    passwords_temp.pop()
    characters = string.ascii_lowercase
    passwords = []
    for x in passwords_temp:
        x = x.rstrip()
        passwords.append(x)

    for c in characters:
        for p in passwords:
            result = c + p
            for_hash = result.encode("utf-8")
            encrypt = hashlib.sha256(for_hash).hexdigest()
            for h in hashes:
                if encrypt == h:
                    print(result + ":" + encrypt + "\n")
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
