"Text and Binary Files"
# File I/O (input and output)

'''
Python now makes a sharp platform-independent distinction between text files and binary files;
    ~ Text files
When a file is opened in text mode, reading its data automatically decodes its content
and returns it as a str; writing takes a str and automatically encodes it before
transferring it to the file. Both reads and writes translate per a platform default or
a provided encoding name. Text-mode files also support universal end-of-line
translation and additional encoding specification arguments. Depending on the
encoding name, text files may also automatically process the byte order mark sequence
at the start of a file.

~ Binary files
When a file is opened in binary mode by adding a b (lowercase only) to the modestring
argument in the built-in open call, reading its data does not decode it in any
way but simply returns its content raw and unchanged, as a bytes object; writing
similarly takes a bytes object and transfers it to the file unchanged. Binary-mode
files also accept a bytearray object for the content to be written to the file.

'''


"""
Because the language sharply differentiates between str and bytes, you must decide
whether your data is text or binary in nature and use either str or bytes objects to
represent its content in your script, as appropriate. Ultimately, the mode in which you
open a file will dictate which type of object your script will use to represent its content:
• If you are processing image files, data transferred over networks, packed binary
    data whose content you must extract, or some device data streams, chances are
    good that you will want to deal with it using bytes and binary-mode files. You might
    also opt for bytearray if you wish to update the data without making copies of it
    in memory.

• If instead you are processing something that is textual in nature, such as program
    output, HTML, email content, or CSV or XML files, you’ll probably want to use
    str and text-mode files.

"""


'''
Notice that the mode string argument to built-in function open (its second argument)
becomes fairly crucial in Python 3.X—its content not only specifies a file processing
mode, but also implies a Python object type. By adding a b to the mode string, you specify
binary mode and will receive, or must provide, a bytes object to represent the file’s
content when reading or writing. Without the b, your file is processed in text mode,
and you’ll use str objects to represent its content in your script. For example, the modes
rb, wb, and rb+ imply bytes; r, w+, and rt (the default) imply str.
'''


"""
Text-mode files also handle the byte order marker (BOM) sequence that may appear at
the start of files under some encoding schemes.
"""
