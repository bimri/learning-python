"Other String Tool Changes in 3.X"
'The re Pattern-Matching Module'
"""
Python’s re pattern-matching module supports text processing that is more general
than that afforded by simple string method calls such as find, split, and replace.

With re, strings that designate searching and splitting targets can be described by general
patterns, instead of absolute text.

This module has been generalized to work on objects
of any string type in 3.X—str, bytes, and bytearray—and returns result substrings of
the same type as the subject string. In 2.X it supports both unicode and str.

Within pattern strings, (.*) means any character (the .), zero or more times (the *), 
saved away as a matched substring (the ()).
"""
import re

S = 'Bugger all down here on earth!'                                # Line of text
B = b'Bugger all down here on earth!'                               # Usually from a file

print(                                                              # Match line to pattern
    re.match('(.*) down (.*) on (.*)', S).groups()                  
)                                                                   # Matched substrings

print(
    re.match(b'(.*) down (.*) on (.*)', B).groups()                 # bytes substrings
)


"""
Since bytes and str support essentially the same operation sets, this type distinction is
largely transparent. But note that, like in other APIs, you can’t mix str and bytes types
in its calls’ arguments in 3.X (although if you don’t plan to do pattern matching on
binary data, you probably don’t need to care):
C:\code> C:\python33\python
    >>> import re
    >>> S = 'Bugger all down here on earth!'
    >>> B = b'Bugger all down here on earth!'
    
    >>> re.match('(.*) down (.*) on (.*)', B).groups()
    TypeError: can't use a string pattern on a bytes-like object
    
    >>> re.match(b'(.*) down (.*) on (.*)', S).groups()
    TypeError: can't use a bytes pattern on a string-like object
    
    >>> re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups()
    (bytearray(b'Bugger all'), bytearray(b'here'), bytearray(b'earth!'))
    
    >>> re.match('(.*) down (.*) on (.*)', bytearray(B)).groups()
    TypeError: can't use a string pattern on a bytes-like object
"""
