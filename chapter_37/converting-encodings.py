"Encodings converting"
'''
It’s also
possible to convert a string to a different encoding than its original, but we must provide
an explicit encoding name to encode to and decode from. This is true whether the
original text string originated in a file or a literal.

The term conversion may be a misnomer here—it really just means encoding a text
string to raw bytes per a different encoding scheme than the one it was decoded from.

Still, this scheme allows scripts to read data in one encoding and store it
in another, to support multiple clients of the same data:

Keep in mind that the special Unicode and hex character escapes are only necessary
when you code non-ASCII Unicode strings manually. In practice, you’ll often load such
text from files instead.
'''
B = b'A\xc3\x84B\xc3\xa8C'                              # Text encoded in UTF-8 format originally
S = B.decode('utf-8')                                   # Decode to Unicode text per UTF-8
print(S) 

T = S.encode('cp500')                                   # Convert to encoded bytes per EBCDIC
print(T) 

U = T.decode('cp500')                                   # Convert back to Unicode per EBCDIC
print(U)
print(U.encode())                                       # Per default utf-8 encoding again
