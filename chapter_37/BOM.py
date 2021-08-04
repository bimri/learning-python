"Handling the BOM in 3.X"
'''
some encoding schemes store a special byte order
marker (BOM) sequence at the start of files, to specify data endianness (which end of
a string of bits is most significant to its value) or declare the encoding type. Python both
skips this marker on input and writes it on output if the encoding name implies it, but
we sometimes must use a specific encoding name to force BOM processing explicitly.

For example, in the UTF-16 and UTF-32 encodings, the BOM specifies big- or littleendian
format. A UTF-8 text file may also include a BOM, but this isn’t guaranteed,
and serves only to declare that it is UTF-8 in general. When reading and writing data
using these encoding schemes, Python automatically skips or writes the BOM if it is
either implied by a general encoding name, or if you provide a more specific encoding
name to force the issue. For instance:
    • In UTF-16, the BOM is always processed for “utf-16,” and the more specific encoding
    name “utf-16-le” denotes little-endian format.
    • In UTF-8, the more specific encoding “utf-8-sig” forces Python to both skip and
    write a BOM on input and output, respectively, but the general “utf-8” does not.

'''
import sys 
print(sys.getdefaultencoding())

try:
    open('temp.txt', 'rb').read()                        # ASCII (UTF-8) text file
    open('temp.txt', 'r').read()                         # Text mode translates line end
except:
    pass

try:
    utf = open('temp.txt', 'r', encoding='utf-8').read()
    print(utf)
except:
    pass


'''
If this file is instead saved as UTF-8 in Notepad, it is prepended with a 3-byte UTF-8
BOM sequence, and we need to give a more specific encoding name (“utf-8-sig”) to
force Python to skip the marker:
    >>> open('spam.txt', 'rb').read() # UTF-8 with 3-byte BOM
    b'\xef\xbb\xbfspam\r\nSPAM\r\n'
    
    >>> open('spam.txt', 'r').read()
    'ï»¿spam\nSPAM\n'
    
    >>> open('spam.txt', 'r', encoding='utf-8').read()
    '\ufeffspam\nSPAM\n'
    
    >>> open('spam.txt', 'r', encoding='utf-8-sig').read()
    'spam\nSPAM\n'
'''


"""
If the file is stored as Unicode big endian in Notepad, we get UTF-16-format data in the
file, with 2-byte (16-bit) characters prepended with a 2-byte BOM sequence—the encoding
name “utf-16” in Python skips the BOM because it is implied (since all UTF-16
files have a BOM), and “utf-16-be” handles the big-endian format but does not skip
the BOM (the second of the following fails to print on older Pythons):
    >>> open('spam.txt', 'rb').read()
    b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
    
    >>> open('spam.txt', 'r').read()
    '\xfeÿ\x00s\x00p\x00a\x00m\x00\n\x00\n\x00S\x00P\x00A\x00M\x00\n\x00\n'
    
    >>> open('spam.txt', 'r', encoding='utf-16').read()
    'spam\nSPAM\n'
    
    >>> open('spam.txt', r', encoding='utf-16-be').read()
    '\ufeffspam\nSPAM\n'

"""


'Dropping the BOM in Python'
'''
The same patterns generally hold true for output. When writing a Unicode file in Python
code, we need a more explicit encoding name to force the BOM in UTF-8—“utf-8”
does not write (or skip) the BOM, but “utf-8-sig” does:
'''
x = open('temp.txt', 'w', encoding='utf-8').write('back at this again,\nthis time with BOO!\n')
print(x)

y = open('temp.txt', 'rb').read()                           # Wrote BOM
print(y)

z = open('temp.txt', 'r').read()
print(z)

q = open('temp.txt', 'r', encoding='utf-8').read()          # Keeps BOM
print(q)

w = open('temp.txt', 'r', encoding='utf-8-sig').read()      # Skips BOM
print(w)


'''
Notice that although “utf-8” does not drop the BOM, data without a BOM can be read
with both “utf-8” and “utf-8-sig”—use the latter for input if you’re not sure whether a
BOM is present in a file
'''
ox = open('temp.txt', 'w').write('bimri\nBIMRI\n')
print(ox)

bx = open('temp.txt', 'rb').read()                          # Data without BOM
print(bx) 

gh = open('temp.txt', 'r').read()                           # Either utf-8 works
print(gh)

jk = open('temp.txt', 'r', encoding='utf-8').read()
print(jk)

jk = open('temp.txt', 'r', encoding='utf-8-sig').read()
print(jk)


"""
Finally, for the encoding name “utf-16,” the BOM is handled automatically: on output,
data is written in the platform’s native endianness, and the BOM is always written;
on input, data is decoded per the BOM, and the BOM is always stripped because it’s
standard in this scheme:
"""
print(sys.byteorder)

ty = open('temp', 'w', encoding='utf-16').write('codes\nCODES')
print(ty)

po = open('temp.txt', 'rb').read()
print(po) 

# er = open('temp.txt', 'r', encoding='utf-16').read()
# print(er)


"""
More specific UTF-16 encoding names can specify different endianness, though you
may have to manually write and skip the BOM yourself in some scenarios if it is required
or present—study the following examples for more BOM-making instructions:
    >>> open('temp.txt', 'w', encoding='utf-16-be').write('\ufeffspam\nSPAM\n')
    11
    
    >>> open('spam.txt', 'rb').read()
    b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
    
    >>> open('temp.txt', 'r', encoding='utf-16').read()
    'spam\nSPAM\n'
    
    >>> open('temp.txt', 'r', encoding='utf-16-be').read()
    '\ufeffspam\nSPAM\n'


The more specific UTF-16 encoding names work fine with BOM-less files, though
“utf-16” requires one on input in order to determine byte order:
    >>> open('temp.txt', 'w', encoding='utf-16-le').write('SPAM')
    4
    
    >>> open('temp.txt', 'rb').read() # OK if BOM not present or expected
    b'S\x00P\x00A\x00M\x00'
    
    >>> open('temp.txt', 'r', encoding='utf-16-le').read()
    'SPAM'
    
    >>> open('temp.txt', 'r', encoding='utf-16').read()
    UnicodeError: UTF-16 stream does not start with BOM
"""
