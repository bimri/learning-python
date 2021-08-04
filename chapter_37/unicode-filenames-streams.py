"Unicode Filenames and Streams"
# Python also supports the notion of non-ASCII file names.
import sys
print(sys.getdefaultencoding(), sys.getfilesystemencoding())            # File content, names

'Filenames: Text versus bytes'
"""
Filename encoding is often a nonissue. In short, for filenames given as Unicode text
strings, the open call encodes automatically to and from the underlying platform’s filename
conventions. Passing arbitrarily pre-encoded filenames as byte strings to file tools
(including open and directory walkers and listers) overrides automatic encodings, and
forces filename results to be returned in encoded byte string form too—useful if filenames
are undecodable per the underlying platform’s conventions (I’m using Windows,
but some of the following may fail on other platforms):
    >>> f = open('xxx\u00A5', 'w') # Non-ASCII filename
    >>> f.write('\xA5999\n') # Writes five characters
    >>> f.close()
    >>> print(open('xxx\u00A5').read()) # Text: auto-encoded
    ¥999
    >>> print(open(b'xxx\xA5').read()) # Bytes: pre-encoded
    ¥999
    
    >>> import glob # Filename expansion tool
    >>> glob.glob('*\u00A5*') # Get decoded text for decoded text
    ['xxx¥']
    >>> glob.glob(b'*\xA5*') # Get encoded bytes for encoded bytes
    [b'xxx\xa5']
"""


'Stream content: PYTHONIOENCODING'
'''
In addition, the environment variable PYTHONIOENCODING can be used to set the encoding
used for text in the standard streams—input, output, and error. This setting overrides
Python’s default encoding for printed text, which on Windows currently uses a Win-
'''
