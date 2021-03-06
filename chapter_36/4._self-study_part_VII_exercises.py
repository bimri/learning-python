"""
4. Self-study examples. At the end of Appendix D, I’ve included a handful of example
scripts developed as group exercises in live Python classes for you to study and run
on your own in conjunction with Python’s standard manual set. These are not
described, and they use tools in the Python standard library that you’ll have to
research on your own. Still, for many readers, it helps to see how the concepts
we’ve discussed in this book come together in real programs. If these whet your
appetite for more, you can find a wealth of larger and more realistic applicationlevel
Python program examples in follow-up books like Programming Python and
on the Web.
"""
# Find the largest Python source file in a single directory

import os, glob 
dirname = r'C:\Python38\Lib'

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py') 
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename)) 

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2]) 
print()


# Find the largest Python source file in an entire directory tree

import sys, os, pprint 
if sys.platform[:3] == 'win':
    dirname = r'C:\Python38\Lib'
else:
    dirname = '/usr/lib/python'

allsizes = []
for (thisDir, subHere, filesHere) in os.walk(dirname):
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2])
print()


# Find the largest Python source file on the module import search path

import sys, os, pprint
visited  = {} 
allsizes = []
for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        thisDir = os.path.normpath(thisDir) 
        if thisDir.upper() in visited:
            continue
        else:
            visited[thisDir.upper()] = True 
        for filename in filesHere:
            if filename.endswith('.py'):
                pypath = os.path.join(thisDir, filename) 
                try:
                    pysize = os.path.getsize(pypath) 
                except:
                    print('skipping', pypath)
                allsizes.append((pysize, pypath)) 

allsizes.sort() 
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3])
print()


# Sum columns in a text file separated by commas

filename = 'data.txt'
sums = {}

for line in open(filename):
    cols = line.split(',')
    nums = [int(col) for col in cols]
    for (ix, num) in enumerate(nums):
        sums[ix] = sums.get(ix, 0) + num 

for key in sorted(sums):
    print(key, '=', sums[key]) 

print()


# Similar to prior, but using lists instead of dictionaries for sums

import sys
filename = sys.argv[1]
numcols  = int(sys.argv[2])
totals   = [0] * numcols

for line in open(filename):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]

print(totals)


# Test for regressions in the output of a set of scripts

import os
testscripts = [dict(script='test1.py', args=''),                        # Or glob script/args dir
               dict(script='test2.py', args='spam')]

for testcase in testscripts:
    commandline = '%(script)s %(args)s' % testcase
    output = os.popen(commandline).read()
    result = testcase['script'] + 'result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult = open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
            print(output) 
        else:
            print('Passed:', testcase['script'])


# Build GUI with tkinter (Tkinter in 2.X) with buttons that change color and grow

from tkinter import * 
import random 
fontsize = 25
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

def reply(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack()
    L.config(fg=color)

def timer():
    L.config(fg=random.choice(colors))
    win.after(250, timer)

def grow():
    global fontsize
    fontsize += 5
    L.config(font=('arial', fontsize, 'italic'))
    win.after(100, grow)

win = Tk()
L = Label(win, text='Spam',
          font=('arial', fontsize, 'italic'), fg='yellow', bg='navy',
          relief=RAISED)
L.pack(size=TOP, expand=YES, fill=BOTH)
Button(win, text='press', command=(lambda: reply('red'))).pack(side=BOTTOM, fill=X)
Button(win, text='timer', command=timer).pack(side=BOTTOM, fill=X)
Button(win, text='grow', command=grow).pack(side=BOTTOM, fill=X)


# Similar to prior, but use classes so each window has own state information

from tkinter import *
import random

class MyGui:
    """
    A GUI with buttons that change color and make the label grow
    """
    colors = ['blue', 'green', 'orange', 'red', 'brown', 'yellow']

    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Gui1', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)
    
    def reply(self):
        "change the button's color at random on Spam presses"
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color,
                font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        "start making the label grow on Grow presses"
        self.growing = True
        self.grower()
    
    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower) 
        
    def stop(self):
        "stop the button growing on Stop presses"
        self.growing = False
    

class MySubGui(MyGui):
    colors = ['black', 'purple']                                            # Customize to change color choices


MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()


# Email inbox scanning and maintenance utility

"""
scan pop email box, fetching just headers, allowing
deletions without downloading the complete message
"""

import poplib, getpass, sys

mailserver = 'your pop email server name here'                              # pop.server.net
mailuser   = 'your pop user name here'
mailpasswd = getpass.getpass('Password for %s' % mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, mboxSize = server.stat()
    print('There are', msgCount, 'mail messages, size ', mboxSize)
    msginfo = server.list()
    print(msginfo)
    for i in range(msgCount):
        msgnum = i+1
        msgsize = msginfo[1][i].split()[1]
        resp, hrdlines, octets = server.top(msgnum, 0)                      # Get hdrs only
        print('-'*80)
        print('[%d: octets=%d, size=%s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)

        if input('Print?') in ['y', 'Y']:
            for line in server.retr(msgnum)[1]: print(line)                 # Get whole msg
        if input('Delete?') in ['y', 'Y']:
            print('deleting')
            server.dele(msgnum)                                             # Delete on srvr
        else:
            print('skipping')
finally:
    server.quit()                           # Make sure we unlock mbox
input('Bye.')                               # Keep window up on Windows   


# CGI server-side script to interact with a web browser

#!/usr/bin/python
import cgi
form = cgi.FieldStorage()                   # Parse form data
print("Content-type: text/html\n")          # hdr plus blank line
print("<HTML>")
print("<title>Reply Page</title>")          # HTML reply page
print("<BODY>")
if not 'user' in form:
    print("<h1>Who are you?</h1>")
else:
    print("<h1>Hello <i>%s</i>!</h1>" % cgi.escape(form['user'].value))
    print("</BODY></HTML>")


# Database script to populate a shelve with Python objects
rec1 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}

rec2 = {'name': {'first': 'Sue', 'last': 'Jones'},
        'job': ['mgr'],
        'age': 35.0}

import shelve
db = shelve.open('dbfile')
db['bob'] = rec1
db['sue'] = rec2
db.close()


# Database script to print and update shelve created in prior script

import shelve
db = shelve.open('dbfile')
for key in db:
    print(key, '=>', db[key])

bob = db['bob']
bob['age'] += 1
db['bob'] = bob
db.close()


# Database script to populate and query a MySql database

from MySQLdb import Connect
conn = Connect(host='localhost', user='root', passwd='XXXXXXX')
curs = conn.cursor()
try:
    curs.execute('drop database testpeopledb')
except:
    pass                                                            # Did not exist

curs.execute('create database testpeopledb')
curs.execute('use testpeopledb')
curs.execute('create table people (name char(30), job char(10), pay int(4))')

curs.execute('insert people values (%s, %s, %s)', ('Bob', 'dev', 50000))
curs.execute('insert people values (%s, %s, %s)', ('Sue', 'dev', 60000))
curs.execute('insert people values (%s, %s, %s)', ('Ann', 'mgr', 40000))

curs.execute('select * from people')
for row in curs.fetchall():
    print(row)

curs.execute('select * from people where name = %s', ('Bob',))
print(curs.description)
colnames = [desc[0] for desc in curs.description]
while True:
    print('-' * 30)
    row = curs.fetchone()
    if not row: break
    for (name, value) in zip(colnames, row):
        print('%s => %s' % (name, value))

conn.commit()                                                           # Save inserted records


# Fetch and open/play a file by FTP

import webbrowser, sys
from ftplib import FTP                                                  # Socket-based FTP tools
from getpass import getpass                                             # Hidden password input
if sys.version[0] == '2': input = raw_input                             # 2.X compatibility

nonpassive = False                                                      # Force active mode FTP for server?
filename = input('File?')                                               # File to be downloaded
dirname = input('Dir? ') or '.'                                         # Remote directory to fetch from
sitename = input('Site?')                                               # FTP site to contact
user = input('User?')                                                   # Use () for anonymous
if not user:
    userinofo = ()
else:
    from getpass import getpass                                         # Hidden password input
    userinfo = (user, getpass('Pswd?'))

print('Connecting...')
connection = FTP(sitename)                                              # Connect to FTP site
connection.login(*userinfo)                                             # Default is anonymous login
connection.cwd(dirname)                                                 # Xfer 1k at a time to localfile
if nonpassive:                                                          # Force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')                                        # Local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

print('Playing...')
webbrowser.open(filename)
