'''
Technically speaking, there are 3 (not 2) formatting tools
built into Python, if we include the obscure string module’s Template
tool
'''

import string

t = string.Template('$num= $title')
print(t.substitute({'num': 7, 'title': 'Strings'}))
print(t.substitute(num=7, title='Strings'))
print(t.substitute(dict(num=7, title='Strings')))
