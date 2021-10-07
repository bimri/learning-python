'''
Python’s struct module can both create and unpack
packed binary data
'''

# Binary files are useful for processing media, 
# accessing data created by C programs, and so on.

# Python's struct module can both create and unpack
# packed binary data to be written to a file in binary mode.

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('data.bin', 'wb')           # Open binary output file
print(file.write(packed))               # Write packed binary data

file.close()


# Reading binary data back is essentially symmetric
data = open('data.bin', 'rb').read()
print(data)

print(data[4:8])                        # Slice bytes in the middle
print(list(data))                       # A sequence of 8-bit bytes

print(struct.unpack('>i4sh', data))     # unpack into objects again
