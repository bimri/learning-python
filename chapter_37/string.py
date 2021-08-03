"String Basics"
'Character Encoding Schemes'

'''
Character sets are standards that assign integer codes to individual characters so they
can be represented in computer memory.
ASCII defines character codes from 0 through 127 and allows each character to be stored in one 8-
bit byte, only 7 bits of which are actually used.
'''
print(ord('b'))                     # 'b' is a byte with binary value 98 in ASCII (and others)
print(hex(97))
print(chr(97))                      # Binary value 97 for character 'a'


'''
Sometimes one byte per character isn’t enough, though. Various symbols and accented
characters, for instance, do not fit into the range of possible characters defined by
ASCII. To accommodate special characters, some standards use all the possible values
in an 8-bit byte, 0 through 255, to represent characters, and assign the values 128
through 255 (outside ASCII’s range) to special characters.
'''
# Latin-1 character set
"In Latin-1, character codes above 127 are assigned to accented and otherwise special characters."
print(0xC4)
print(chr(196))                 # Python 3.X result form shown

"This standard allows for a wide array of extra special characters, but still supports ASCII as a 7-bit subset of its 8-bit representation."


"Unicode allows more flexibility"
'''
Unicode text is sometimes referred to as "wide-character" strings, because characters may be represented
with mutiples bytes if needed. Unicode is typically used in internationalized programs, to represent
European, Asian, and other non-Endglish character sets that have more tha 8-bytes can represent.
'''
# Encoding => to store rich text in computer memory, we say that characters are translated to & from raw bytes
'''
encoding — the rules for translating a string of Unicode
characters to a sequence of bytes, and extracting a string from a sequence of bytes.
'''
# Procedurally: - 
    # Encoding is the process of translating a string of characters into its raw bytes form, according to a desired encoding name.
    # Decoding is the process of translating a raw string of bytes into its character string form, according to its encoding name.
# We encode from string to raw bytes, and decode from raw bytes to string

# Encode Method
"Encodings are specified as strings containing the encoding’s name."
S = 'ni'
print(
    S.encode('ascii'),
    S.encode('latin1'),
    S.encode('utf8')
)

# Python comes with roughly 100 different encodings
import encodings
help(encodings)

'''
some are implemented in Python, and
some in C. Some encodings have multiple names, too; for example, latin-1,
iso_8859_1, and 8859 are all synonyms for the same encoding, Latin-1.
'''
