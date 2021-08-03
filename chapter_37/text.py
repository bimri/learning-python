"Source File Character Set Encoding Declarations"
'''
To interpret the content of strings you code and hence embed within
the text of your script files, Python uses the UTF-8 encoding by default, but it allows
you to change this to support arbitrary character sets by including a comment that
names your desired encoding. The comment must be of this form and must appear as
either the first or second line in your script in either Python 2.X or 3.X:
    # -*- coding: latin-1 -*-
'''
# -*- coding: latin-1 -*-
# Any of the following string literal forms work in latin-1.
# Changing the encoding above to either ascii or utf-8 fails,
# because the 0xc4 and 0xe8 in myStr1 are not valid in either.

myStr1 = 'aÄBèC'

myStr2 = 'A\u00c4B\U000000e8C'

myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')

    bytes1 = aStr.encode()                                          # Per default utf-8: 2 bytes for non-ASCII
    bytes2 = aStr.encode('latin-1')                                 # One byte per char
   #bytes3 = aStr.encode('ascii') # ASCII fails: outside 0..127 range

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))

