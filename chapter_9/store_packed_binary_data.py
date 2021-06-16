'''compose and parse packed binary data'''
import struct

# this is another data-conversion tool that 
# interprets strings in files as binary data

F = open('data.bin', 'wb')                                  # Open binary output file
data = struct.pack('>i4sh', 7, b'spam', 8)                  # Make packed binary data
print(data)
F.write(data)                                               # Write byte string
F.close()


# To parse the values out to normal Python objects,
# read the string back and unpack it using the same format string
F = open('data.bin', 'rb')
data = F.read()                                     # Get packed binary data
print(data)

values = struct.unpack('>i4sh', data)               # Convert to Python objects
print(values)
