"Using 3.X/2.6+ bytearray Objects"
'''
bytearray - a mutable sequence of integers in the range 0 through 255, 
which is a mutable variant of bytes. As such it supports the same string 
and sequence operations as bytes, as well as many of the mutable in-place
-change operations supported by lists.

Bytearrays support in-place changes to both truly binary data as well as simple forms
of text such as ASCII, which can be represented with 1 byte per character (richer Unicode
text generally requires Unicode strings, which are still immutable).
'''

"Bytearrays in Action"
'We can create bytearray objects by calling the bytearray builtin.'

# Creation in 2.6/2.7: a mutable sequence of small (0..255) ints 
# S = 'spam'

# C = bytearray(S)                            # A back-port from 3.X in 2.6+
# print(C)

"""
In Python 3.X, an encoding name or byte string is required, because text and binary
strings do not mix (though byte strings may reflect encoded Unicode text):
"""
# Creation in 3.X: text/binary do not mix
S = 'spam'
# C = bytearray(S)                          # TypeError: string argument without an encoding

# A content-specific type in 3.X
C = bytearray(S, 'latin1')
print(C)

B = b'spam'                                 # b'..' != '..' in 3.X (bytes/str)
C = bytearray(B)
print(C)


"""
Once created, bytearray objects are sequences of small integers like bytes and are mutable
like lists, though they require an integer for index assignments, not a string
"""
# Mutable, but must assign ints, not strings
print(C[0])

# C[0] = 'x'                                # TypeError: an integer is required
# C[0] = b'x'                               # TypeError: an integer is required
C[0] = ord('x')                             # Use ord() to get a character's ordinal
print(C) 

C[1] = b'Y'[0]                              # Or index a byte string
print(C)


'''
Processing bytearray objects borrows from both strings and lists, since they are mutable
byte strings. While the byterrray’s methods overlap with both str and bytes, it also
has many of the list’s mutable methods. Besides named methods, the __iadd__ and
__setitem__ methods in bytearray implement += in-place concatenation and index assignment,
respectively:
'''
# in bytes but not bytearray
attrs = set(dir(b'abc')) - set(dir(bytearray(b'abc'))) 
print(attrs)

# in bytearray but not bytes
attrs = set(dir(bytearray(b'abc'))) - set(dir(b'abc'))
print(attrs)


"""
You can change a bytearray in place with both index assignment, as you’ve just seen,
and list-like methods like those shown here (to change text in place prior to 2.6, you
would need to convert to and then from a list, with list(str) and ''.join(list)—see
"""
# Mutable method calls
print(C)
# C.append(b'LMN')                            # 2.X requires string of size 1

C.append(ord('L'))
print(C)

C.extend(b'MNO')
print(C)


"""
All the usual sequence operations and string methods work on bytearrays, as you would
expect (notice that like bytes objects, their expressions and methods expect bytes arguments,
not str arguments):
"""
# Sequence operations and string methods
print(); print(C)
print(C + b'!#')
print(C[0])
print(C[1:])
print(len(C))

# C.replace('xY', 'sp')                               # This works in 2.X
print(C.replace(b'xY', b'sp'))
print(C)
print(C * 4)


"Python 3.X String Types Summary"
'''
Finally, by way of summary, the following examples demonstrate how bytes and byte
array objects are sequences of ints, and str objects are sequences of characters:
'''
# Binary versus text
print(B)
print(list(B))

print(B)
print(list(C))

print(S)
print(list(S))

'''
Although all three Python 3.X string types can contain character values and support
many of the same operations, again, you should always:
    • Use str for textual data.
    • Use bytes for binary data.
    • Use bytearray for binary data you wish to change in place.
'''
