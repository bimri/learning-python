"Why You Will Care: Inspecting Files, and Much More"
'''
After
saving a formerly ASCII HTML file in Notepad as “UTF8,” I found that it had grown
a mystery non-ASCII character along the way due to an apparent keyboard operator
error, and would no longer work as ASCII in text tools. To find the bad character, I
simply started Python, decoded the file’s content from its UTF-8 format via a text
mode file, and scanned character by character looking for the first byte that was not a
valid ASCII character too:
    >>> f = open('py33-windows-launcher.html', encoding='utf8')
    >>> t = f.read()
    >>> for (i, c) in enumerate(t):
        try:
            x = c.encode(encoding='ascii')
        except:
            print(i, sys.exc_info()[0])
        9886 <class 'UnicodeEncodeError'>

With the bad character’s index in hand, it’s easy to slice the Unicode string for more
details:
    >>> len(t)
    31021
    >>> t[9880:9890]
    'ugh. \u206cThi'
    >>> t[9870:9890]
    'trace through. \u206cThi'

After fixing, I could also open in binary mode to verify and explore actual undecoded
file content further:
    >>> f = open('py33-windows-launcher.html', 'rb')
    >>> b = f.read()
    >>> b[0]
    60
    >>> b[:10]
    b'<HTML>\r\n<T'
    
'''
