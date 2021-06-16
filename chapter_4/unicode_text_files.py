S = 'sp\xc4m'                                           # Non-ASCII Unicode text
print(S)

print(S[2])                                             # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8')       # Write/encode utf-8 text
print(file.write(S))
file.close()

text = open('unidata.txt', encoding='utf-8').read()     # Read/decode utf-8 text 
print(text)
print(len(text))


# To see how its stored in-file
raw = open('unidata.txt', 'rb').read()                  # Read raw encoded bytes
print(raw)
print(len(raw))                                         # Really 5 bytes in UTF-8


# Manual encode & decode
print(text.encode('utf-8'))     # Encode
print(raw.decode('utf-8'))      # Decode


# Different encoding names
print(text.encode('latin-1'))
print(text.encode('utf-16'))

print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))
