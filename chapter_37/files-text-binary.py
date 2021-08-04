"Using Text and Binary Files"
"""
the mode in which you open a file is crucial—it determines which 
object type you will use to represent the file’s content in your script.

Text mode implies str objects, and binary mode implies bytes objects:
    • Text-mode files interpret file contents according to a Unicode encoding—either the
    default for your platform, or one whose name you pass in. By passing in an encoding
    name to open, you can force conversions for various types of Unicode files. Textmode
    files also perform universal line-end translations: by default, all line-end
    forms map to the single '\n' character in your script, regardless of the platform on
    which you run it. As described earlier, text files also handle reading and writing
    the byte order mark (BOM) stored at the start-of-file in some Unicode encoding
    schemes.

    • Binary-mode files instead return file content to you raw, as a sequence of integers
    representing byte values, with no encoding or decoding and no line-end translations.

# second argument to determines whether you want text or binary processing open

In 3.X, mode argument to open also implies an object type for file content
representation, regardless of the underlying platform—text files return a str for reads
and expect one for writes, but binary files return a bytes for reads and expect one (or
a bytearray) for writes.

"""

'Text File Basics'
# Basic text files (and strings) work the same as in 2.X
file = open('temp', 'w')
size = file.write('bimri codes\n')                  # returns number of characters written
file.close()

file = open('temp')                         # Default mode is "r"(=="rt"): text input
text = file.read()
# text      (compare on CMD output with below output
print(text)


"Text and Binary Modes in 2.X and 3.X"
# there is no major distinction between text and binary 
# files—both accept and return content as str strings
'''
The only major difference is that text files automatically
map \n end-of-line characters to and from \r\n on Windows, 
while binary files do not
'''
open('temp', 'w').write('adding text to temp file\n')                   # Write in text mode: adds\r
rd = open('temp', 'r').read()                                           # Read in text mode: drops\r
print(rd)

bm = open('temp', 'rb').read()                                          # Read in binary mode: verbatim
print(bm)

open('temp', 'wb').write(b'writing now in binary mode -addition\n')      # Write in binary mode
bm = open('temp', 'r').read()                                           # \n not expanded to \r\n
print(bm)


"""
Notice how on Windows text-mode files translate the \n end-of-line character to \r\n
on output; on input, text mode translates the \r\n back to \n, but binary-mode files do
not.
"""

'''
Binary-mode files always return contents as a bytes object, but accept either a bytes or
bytearray object for writing; this naturally follows, given that bytearray is basically just
a mutable variant of bytes. In fact, most APIs in Python 3.X that accept a bytes also
allow a bytearray:
'''
# bytearrays work too
BA = bytearray(b'\x01\x02\x03')

open('temp', 'wb').write(BA)
rBA = open('temp', 'r').read()
print(rBA)

rBA = open('temp', 'rb').read()
print(rBA)


'Type and Content Mismatches in 3.X'
'''
Notice that you cannot get away with violating Python’s str/bytes type distinction
when it comes to files.
'''
# Types are not flexible for file content
open('temp', 'w').write('abc\n')                                    # Text mode makes and requires str
# open('temp', 'w').write(b'abc\n')                                 # TypeError: must be str, not bytes

open('temp', 'wb').write(b'abc\n')                                  # Binary mode makes and requires bytes
# open('temp', 'wb').write('abc\n')                                 # TypeError: 'str' does not support the buffer interface


"""
In addition to type constraints, file content can matter in 3.X. Text-mode output files
require a str instead of a bytes for content
"""
# Can't read truly binary data in text mode
chr(0xFF)                                           # FF is a valid char, FE is not
chr(0xFE)                                           # An error in some Pythons

# open('temp', 'w').write(b'\xFF\xFE\xFD')          # Can't use arbitrary bytes!
open('temp', 'wb').write(b'\xFF\xFE\xFD')           # Can also write in binary mode
open('temp', 'rb').read()                           # Can always read as binary bytes
open('temp', 'r').read()                            # Can't read text unless decodable!

'''
In general, however, because text-mode input files in 3.X must be able to decode content
per a Unicode encoding, there is no way to read truly binary data in text mode
'''
