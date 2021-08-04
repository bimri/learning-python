"Using Unicode Files"
'''
open call accepts an
encoding for text files, and arranges to run the required encoding and decoding for us
automatically as data is transferred. This allows us to process a variety of Unicode text
created with different encodings than the default for the platform, and store the same
text in different encodings for different purposes.
'''

'Reading and Writing Unicode in 3.X'
S = 'A\xc4B\xe8C'                                       # Five-character decoded string, non-ASCII
print(S)
print(len(S))

# Manual encoding with methods
L = S.encode('latin-1')                                 # 5 bytes when encoded as latin-1
print(L)
print(len(L))

U = S.encode('utf-8')                                   # 7 bytes when encoded as utf-8
print(U)
print(len(U))

# File output encoding                                          # Encoding automatically when written
x = open('latindata', 'w', encoding='latin-1').write(S)         # Write as latin-1
print(x)

x = open('utf8data', 'w', encoding='utf-8').write(S)            # Write as utf-8
print(x)

x = open('latindata', 'rb').read()                              # Read raw bytes
print(x)

x = open('utf8data', 'rb').read()                               # Different in files
print(x)


# File input decoding                                           # Decoding automatically when read
y = open('latindata', 'r', encoding='latin-1').read()           # Decoded on input
print(y)

y = open('utf8data', 'r', encoding='utf-8').read()              # Per encoding type
print(y)

X = open('latindata', 'rb').read()                              # Manual decoding:
X.decode('latin-1')                                             # Not necessary

X = open('utf8data', 'rb').read()
X.decode()                                                      # UTF-8 is default


'Decoding mismatches'
'''
Finally, keep in mind that this behavior of files in 3.X limits the kind of content you
can load as text. Python 3.X really must be able to
decode the data in text files into a str string, according to either the default or a passedin
Unicode encoding name. Trying to open a truly binary data file in text mode, for
example, is unlikely to work in 3.X even if you use the correct object types:
'''
file = open(r'C:\Python38\python.exe', 'r')
# print(text = file.read())                                             # UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2: ...

file = open(r'C:\Python38\python.exe', 'rb')
data = file.read()
print(data[:20])
