print('sp\xc4m')        # normal str strings are Unicode text
print(b'a\x01c')        # bytes strings are byte-based data
print(u'sp\u00c4m')

# Encoded to 4 bytes in UTF-8 in files
print('spam'.encode('utf-8'))

# But Encoded to 10 bytes in UTF-16
print('spam'.encode('utf16'))


print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))
