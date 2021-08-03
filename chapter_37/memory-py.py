"How Python Stores Strings in Memory"
'''
In memory, Python always stores decoded text
strings in an encoding-neutral format, which may or may not use multiple bytes for each
character. All text processing occurs in this uniform internal format. Text is translated
to and from an encoding-specific format only when it is transferred to or from external
text files, byte strings, or APIs with specific encoding requirements. Once in memory,
though, strings have no encoding.
'''

# The way Python actually stores text in memory is prone to change over time
# Built-in ord function now returns a character’s Unicode code point ordinal

"Thinking in terms of characters allows us to abstract away the details of external and internal storage."
# Encoding pertains mostly to files and transfers


'''
Once loaded into a Python string, text in memory has no notion of an “encoding,” and is
simply a sequence of Unicode characters (a.k.a. code points) stored generically. In your
script, that string is accessed as a Python string object
'''
