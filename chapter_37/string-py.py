"Python’s String Types"

'''

Python 3.X comes with three string object types—one for textual data and
two for binary data:
    • str for representing decoded Unicode text (including ASCII)
    • bytes for representing binary data (including encoded text)
    • bytearray, a mutable flavor of the bytes type

'''
# All three string types in 3.X support similar operation sets
# but have different roles


'''
3.X stores text in a redefined str type—an immutable sequence of
characters (not necessarily bytes), which may contain either simple text such as ASCII
whose character values fit in single bytes, or richer character set text such as UTF-8
whose character values may require multiple bytes. Strings processed by your script
with this type are stored generically in memory, and are encoded to and decoded from
byte strings per either the platform Unicode default or an explicit encoding name. This
allows scripts to translate text to different encoding schemes, both in memory and when
transferring to and from files.
'''


"""
While 3.X’s new str type does achieve the desired string/unicode merging, many programs
still need to process raw binary data that is not encoded per any text format.
Image and audio files, as well as packed data used to interface with devices or C programs
you might process with Python’s struct module, fall into this category. Because
Unicode strings are decoded from bytes, they cannot be used to represent bytes.

To support processing of such truly binary data, a new string type, bytes, also was
introduced—an immutable sequence of 8-bit integers representing absolute byte values,
which prints as ASCII characters when possible. Though a distinct object type, bytes
supports almost all the same operations that the str type does; this includes string
methods, sequence operations, and even re module pattern matching, but not string
formatting.

In more detail, a 3.X bytes object really is a sequence of small integers, each of which
is in the range 0 through 255; indexing a bytes returns an int, slicing one returns
another bytes, and running the list built-in on one returns a list of integers, not characters.
When processed with operations that assume characters, though, the contents
of bytes objects are assumed to be ASCII-encoded bytes (e.g., the isalpha method
assumes each byte is an ASCII character code). Further, bytes objects are printed as
character strings instead of integers for convenience.
"""


'''
While they were at it, Python developers also added a bytearray type in 3.X. bytear
ray is a variant of bytes that is mutable and so supports in-place changes. It supports
the usual string operations that str and bytes do, as well as many of the same in-place
change operations as lists (e.g., the append and extend methods, and assignment to
indexes). This can be useful both for truly binary data and simple types of text. Assuming
your text strings can be treated as raw 8-bit bytes (e.g., ASCII or Latin-1 text),
bytearray finally adds direct in-place mutability for text data—
'''
