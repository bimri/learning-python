"Using 3.X bytes Objects"
'''
3.X bytes object is a sequence of small integers, each of
which is in the range 0 through 255, that happens to print as ASCII characters when
displayed.

It supports sequence operations and most of the same methods available on
str objects.

However, bytes does not support the for
mat method or the % formatting expression, and you cannot mix and match bytes and
str type objects without explicit conversions—you generally will use all str type objects
and text files for text data, and all bytes type objects and binary files for binary data.
'''

'Method Calls'
"""
If you really want to see what attributes str has that bytes doesn’t, you can always
check their dir built-in function results. The output can also tell you something about
the expression operators they support (e.g., __mod__ and __rmod__ implement the %
operator):
"""
# Attributes in str but not bytes
attrs = set(dir('abc')) - set(dir(b'abc'))
print(attrs)

# Attributes in bytes not str
attrs = set(dir(b'abc')) - set(dir('abc'))
print(attrs)

'''
str and bytes have almost identical functionality. Their unique attributes
are generally methods that don’t apply to the other; for instance, decode translates
a raw bytes into its str representation, and encode translates a string into its raw
bytes representation. Most of the methods are the same, though bytes methods require
bytes arguments (again, 3.X string types don’t mix). Also recall that bytes objects are
immutable, just like str objects in both 2.X and 3.X.
'''
B = b'spam'                                 # b'...' bytes literal
print(B.find(b'pa'))

print(B.replace(b'pa', b'XY'))              # bytes methods expect bytes arguments

print(B.split(b'pa'))                       # bytes methods return bytes results

print(B)

# B[0] = 'x'                                # TypeError: 'bytes' object does not support item assignment


"One notable difference is that string formatting works only on str objects in 3.X, not on bytes objects"
print('%s' % 99)
# b'%s' % 99                                # TypeError: unsupported operand type(s) for %: 'bytes' and 'int'

print('{0}'.format(99))
# b'{0}'.format(99)                         # AttributeError: 'bytes' object has no attribute 'format'
