"Coding Basic Strings"
'Python 3.X String Literals'
B = b'bimri'                        # bytes literal make a bytes object(8-bytes)
S = 'codes'                         # str literal makes a Unicode text string

print(type(B)); print(type(S))
print(B)
print(S)


"bytes object is actually a sequence of short integers, though it prints its content as characters whenever possible:"
print(B[0]); print(S[0])            # Indexing returns an int for bytes, str for str
print(B[1:]); print(S[1:])          # SLicing makes another bytes or str object
print(list(B), list(S))


'''
The bytes object is also immutable, just like str (though bytearray, is
not); you cannot assign a str, bytes, or integer to an offset of a bytes object.
'''
"Both are immutable"
# B[0] = 'x'
# S[0] = 'x'


# bytes prefix works on single, double, triple quotes, raw
B = B"""
    xxx
    yyy
    """
print(B)
