#!/usr/bin/python 
"""
File certificate.py: a Python 2.X and 3.X script.
Generate a bare-bones class completion certificate: printed,
and saved
"""

from __future__ import print_function                                           # 2.X compatibility
import time, sys, webbrowser

if sys.version_info[0] == 2:                                                    # 2.X compatibility
    input = raw_input
    import cgi
    htmlescape = cgi.escape
else:
    import html
    htmlescape = html.escape

maxline  = 60                                    # For seperator lines
browser  = True                                  # Display in a browser
saveto   = 'bimri_cert.txt'                      # Save filenames
template = """ 
%s

===> OFFICIAL CERTIFICATE <===

Date: %s

This certifies that:

\t%s

has survived the massive tome:

\t%s

and is now entitled to all privileges thereof, including
the right to called a Python Programmer a.k.a. "Pythonista".
--Mark Lutz, Instructor


%s
""" 

# Interact, setup
for c in 'Congratulations!'.upper():
    print(c, end=' ')
    sys.stdout.flush()                              # Else some shells wait for \n
    time.sleep(0.25)
print()

date = time.ctime()
# date = time.strftime('%b %d, %Y', date)             # monthdate, year
name = input('Your name: ').strip()
sept = '*' * maxline
book = 'Learning Python 5th Edition'

# Make text file version
file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file=file)
file.close()

# Make html file version
htmlto = saveto.replace('.txt', '.html')
file = open(htmlto, 'w')

tags = text.replace(sept, '<hr>')                   # Insert a few tags
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('<===', '</h1>')

tags = tags.split('\n') # Line-by-line mods
tags = ['<p>' if line == ''
             else line for line in tags]
tags = ['<i>%s</i>' % htmlescape(line) if line[:1] == '\t'
             else line for line in tags]
tags = '\n'.join(tags)

link = '<i><a href="http://www.rmi.net/~lutz">Book support site</a></i>\n'
foot = '<table>\n<td><img src="ora-lp.jpg" hspace=5>\n<td>%s</table>\n' % link
tags = '<html><body bgcolor=beige>' + tags + foot + '</body></html>'

print(tags, file=file)
file.close()

# Display results
print('[File: %s]' % saveto, end='')
print('\n' * 2, open(saveto).read())

if browser:
    webbrowser.open(saveto, new=True)
    webbrowser.open(htmlto, new=False)

if sys.platform.startswith('win'):
    input('[Press Enter]')                              # Keep window open if clicked on Windows
