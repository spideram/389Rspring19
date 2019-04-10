#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------\n")
print("MAGIC: %s\n" % hex(magic))
print("VERSION: %d\n" % int(version))

counter = 8

timestamp = struct.unpack_from("<I", data, counter)
counter += 4
author = struct.unpack_from("8s", data, counter)
counter += 8

print("TIMESTAMP: %d\n" % int(timestamp[0]))
print("AUTHOR: %s\n" % author[0].decode("ascii"))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------\n")

while (1):
    stype = struct.unpack_from("32s", data, counter)
    counter += sys.getsizeof(stype)
    slen = struct.unpack_from("<L", data, counter)
    counter += sys.getsizeof(slen)
    slength = int(slen[0])
    if (slength != 0):
        if (stype[0].decode("ascii") == "SECTION_ASCII"):
            svalue = struct.unpack_from(slength + "s", data, counter)
