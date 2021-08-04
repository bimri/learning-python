"Sequence Operations"
'''
Besides method calls, all the usual generic sequence operations from strings
and lists; work as expected on both str and bytes. Including indexing, slicing,
concatenation, and so on.

bytes really is a sequence of 8-bit integers, but for convenience prints as a 
string of ASCII-coded characters where possible when displayed as a whole.
To check a given byte’s value, use the chr built-in to convert it back to its 
character.
'''
B = b'spam'                             # A sequence of small ints
print(B)                                # Prints as ASCII characters (and/or hex escapes)
print(B[0])                             # Indexing yields an int
print(B[-1])
print(chr(B[0]))                        # Show characeter for int
print(list(B))                          # Show all the byte's int value
print(B[1:],B[:-1]) 
print(len(B)) 
print(B + b'lmn')
print(B * 4)


'Other Ways to Make bytes Objects'
"""
So far, we’ve been mostly making bytes objects with the b'...' literal syntax. We can
also create them by calling the bytes constructor with a str and an encoding name,
calling the bytes constructor with an iterable of integers representing byte values, or
encoding a str object per the default (or passed-in) encoding.

As we’ve seen, encoding
takes a text str and returns the raw encoded byte values of the string per the encoding
specified; conversely, decoding takes a raw bytes sequence and translates it to its str
text string representation—a series of Unicode characters. Both operations create new
string objects:
"""
B = b'abc'                              # Literal
print(B) 

B = bytes('bimri', 'ascii')                # Constructor with encoding name
print(B)

print(ord('b'))

B = bytes([97, 98, 99])                     # Integer iterable
print(B)

B = 'spam'.encode()                         # str.encode() (or bytes())
print(B)

S = B.decode()                              # bytes.decode() (or str())
print(S)

'''
From a functional perspective, the last two of these operations are really tools for
converting between str and bytes
'''
