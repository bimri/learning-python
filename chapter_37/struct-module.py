"The struct Binary Data Module"
"""
The Python struct module, used to create and extract packed binary data from strings
not str objects (which makes sense, given that it’s
intended for processing binary data, not decoded text); and “s” data code values must
be bytes as of 3.2 (the former str UTF-8 auto-encode is dropped).
"""

'''
Here are both Pythons in action, packing three objects into a string according to a binary
type specification (they create a 4-byte integer, a 4-byte string, and a 2-byte integer):
'''
from struct import pack 
z = pack('>i4sh', 7, b'spam', 8)                            # bytes in 3.X (8-bit strings)
print(z)


import struct
B = struct.pack('>i4sh', 7, b'spam', 8)
print(B)

vals = struct.unpack('>i4sh', B)
print(vals)

# vals = struct.unpack('>i4sh', B.decode())                 # TypeError: 'str' does not support the buffer interface


'code like this is one of the main places where programmers will notice the bytes object type'
# Write values to a packed binary file
F = open('data.bin', 'wb')                                  # Open binary output file

import struct
data = struct.pack('>i4sh', 7, b'spam', 8)                  # Create packed binary data
print(data)

F.write(data)                                               # Write to file
F.close()


# Read values from a packed binary file
F = open('data.bin', 'rb')                                  # Open binary input file
data = F.read()                                             # Read bytes
print(data)

values = struct.unpack('>i4sh', data)                       # Extract packed binary data
print(values)                                               # Result of struct.unpack


# Accessing bits of parsed integers
print(bin(values[0]))                                       # Can get bits in ints

print(values[0] & 0x01)                                     # Test first(lowerest) bit in int

print(values[0] | 0b1010)                                   # Bitwise or: turn bits on

print(bin(values[0] | 0b1010))                              # 15 decimal is 1111 binary

print(bin(values[0] ^ 0b1010))                              # Bitwise xor: off if both true

print(bool(values[0] & 0b100))                              # Test if bit 3 is on

print(bool(values[0] & 0b1000))                             # Test if bit 4 is set


"""
Since parsed bytes strings are sequences of small integers, we can do similar processing
with their individual bytes:
"""
# Accessing bytes of parsed strings and bits within them
print(
    values[1],
    values[1][0],                                           # bytes string: sequence of ints
    values[1][1:],                                          # Prints as ASCII characters
    bin(values[1][0]),                                      # Can get to bits of bytes in strings
    bin(values[1][0] | 0b1100),                             # Turn bits on
    values[1][0] | 0b1100
)
