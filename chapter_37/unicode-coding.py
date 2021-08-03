"Coding Unicode Strings"
'Coding ASCII Text'
# ASCII text is a simple type of Unicode, stored as a sequence of byte values that represent characters

print(ord('X'))                         # 'X' is binary code point value 88 in the default encoding
print(chr(88))                          # 88 stands for character 'X'

S = 'BIMRI'                             # A unicode string of ASCII text
print(S)
print(len(S))                           # Three characters long

lc = [ord(c) for c in S]                # Three characters with interget ordinal values
print(lc)

"""
Normal 7-bit ASCII text like this is represented with one character per byte under each
of the Unicode encoding schemes
"""
encd_ascii = S.encode('ascii')                  # Values 0..127 in 1 byte(7 bits) each
print(encd_ascii)

encd_latin = S.encode('latin-1')                # Values 0.255 in 1 byte(8 bits) each
print(encd_latin)

encd_utf   = S.encode('utf-8')                  # Values 0..127 in 1 byte, 128..2047 in 2, others 3 or 4
print(encd_utf)
print()


"""
In fact, the bytes objects returned by encoding ASCII text this way are really a sequence
of short integers, which just happen to print as ASCII characters when possible:
"""
print(
    S.encode('latin-1'),
    S.encode('latin-1')[0],
    list(S.encode('latin-1'))
)
print()


"Coding Non-ASCII Text"
'special accented characters outside the 7-bit range of ASCII'
print(chr(0xc4)); print(chr(0xe8))                      # 0xC4, 0xE8: characters outside ASCII's range

S = '\xc4\xe8'                                          # Single 8-bit value hex escapes: two digits
print(S)

S = '\u00c4\u00e8'                                      # 16-bit Unicode escapes: four digits each
print(S)
print(len(S))


'''
Note that in Unicode text string literals like these, hex and Unicode escapes denote a
Unicode code point value, not byte values. The x hex escapes require exactly two digits
(for 8-bit code point values), and u and U Unicode escapes require exactly four and eight
hexadecimal digits, respectively, for denoting code point values that can be as big as
16 and 32 bits will allow:
'''
S = '\U000000c4\U000000e8'                                          # 32-bit Unicode escapes: eight digits each
print(S)
print()


'Encoding and Decoding Non-ASCII text'
'''
Now, if we try to encode the prior section’s non-ASCII text string into raw bytes using
as ASCII, we’ll get an error, because its characters are outside ASCII’s 7-bit code point
value range:
'''
S = '\u00c4\u00e8'                                          # Non-ASCII text string, two characters long
print(S)
print(len(S))

# S.encode('ascii')                                         # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1:
"Encoding this as Latin-1/utf-8 works"
print(S.encode('latin-1'))                                  # 1 byte per character when encoded
print(S.encode('utf-8'))                                    # 2 bytes per character when encoded
print(len(S.encode('latin-1')))                             # 2 bytes in latin-1, 4 in utf-8
print(len(S.encode('utf-8')))
print()


"""
Note that you can also go the other way, reading raw bytes from a file and decoding
them back to a Unicode string. However, the encoding mode you give
to the open call causes this decoding to be done for you automatically on input (and
avoids issues that may arise from reading partial character sequences when reading by
blocks of bytes):
"""
B = b'\xc4\xe8'                                             # Text encoded per Latin-1
print(B)
print(len(B))                                               # 2 raw bytes, two encoded characters
print(B.decode('latin-1'))                                  # Decode to text per Latin-1

B = b'\xc3\x84\xc3\xa8'                                     # Text encoded per UTF-8
print(len(B))                                               # 4 raw bytes, two encoded characters
print(B.decode('utf-8'))                                    # Decode to text per UTF-8
print(len(B.decode('utf-8')))                               # Two Unicode characters in memory


'Other Encoding Schemes'
# Some encodings use even larger byte sequences to represent characters.
S = 'A\u00c4B\U000000e8C'                                   # A, B, C, and 2 non-ASCII characters
print(S)
print(len(S))                                               # Five characters long
print(S.encode('latin-1'))
print(len(S.encode('latin-1')))                             # # 5 bytes when encoded per latin-1
print(S.encode('utf-8'))
print(len(S.encode('utf-8')))                               # 7 bytes when encoded per utf-8

'''
Technically speaking, you can also build Unicode strings piecemeal using chr instead
of Unicode or hex escapes, but this might become tedious for large strings:
'''
S = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
print(S)

print(S.encode('cp500'))                                    # Two other Western European encodings
print(S.encode('cp850'))                                    # 5 bytes each, different encoded values

S = 'spam'                                                  # ASCII text is the same in most
print(S.encode('latin-1'))
print(S.encode('utf-8'))
print(S.encode('cp500'))                                    # But not in cp500: IBM EBCDIC!
print(S.encode('cp850'))


'''
The same holds true for the UTF-16 and UTF-32 encodings, which use fixed 2- and 4-
byte-per-character schemes with same-sized headers—non-ASCII encodes differently,
and ASCII is not 1 byte per character:
'''
S = 'A\u00c4B\U000000e8C'
print(S.encode('utf-16'))

S = 'spam'
print(S.encode('utf-16'))
print(S.encode('utf-32'))
print()


'Byte String Literals: Encoded Text'
"""
Two cautions here too. First, Python 3.X allows special characters to be coded with
both hex and Unicode escapes in str strings, but only with hex escapes in bytes strings
—Unicode escape sequences are silently taken verbatim in bytes literals, not as escapes.
In fact, bytes must be decoded to str strings to print their non-ASCII characters properly:
"""
S = 'A\xC4B\xE8C'                                           # 3.X: str recognizes hex and Unicode escapes
print(S)

S = 'A\u00C4B\U000000E8C'
print(S)

B = b'A\xC4B\xE8C'                                          # bytes recognizes hex but not Unicode
print(B)

B = b'A\u00C4B\U000000E8C'                                  # Escape sequences taken literally!
print(B)

B = b'A\xC4B\xE8C'                                          # Prints non-ASCII as hex                                          # Use hex escapes for bytes
print(B)

print(B.decode('latin-1'))                                  # Decode as latin-1 to interpret as text


"""
Second, bytes literals require characters either to be ASCII characters or, if their values
are greater than 127, to be escaped; str stings, on the other hand, allow literals containing
any character in the source character set—which, as discussed later, defaults
to UTF-8 unless an encoding declaration is given in the source file:
"""
S = 'AÄBèC'                                                 # Chars from UTF-8 if no encoding declaration
print(S)

# B = b'AÄBèC'                                              # SyntaxError: bytes can only contain ASCII literal characters.

B = b'A\xC4B\xE8C'                                          # Chars must be ASCII, or escapes
print(B)
print(B.decode('latin-1'))
print(S.encode())                                           # Source code encoded per UTF-8 by default
                                                            # Uses system default to encode, unless passed
print(S.encode('utf-8'))

# B.decode()                                                # Raw bytes do not correspond to utf-8

"""
Both these constraints make sense if you remember that byte strings hold bytes-based
data, not decoded Unicode code point ordinals; while they may contain the encoded
form of text, decoded code point values don’t quite apply to byte strings unless the
characters are first encoded.
"""
