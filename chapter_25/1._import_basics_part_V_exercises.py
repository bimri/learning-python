def countLines(name):
    tot = 0 
    for line in open(name): tot += 1
    return tot 

def countChars(name):
    tot = 0
    for line in open(name): tot += len(line)
    return tot

def test(name):                                             # Or pass file object
    return countLines(name), countChars(name)               # Or return a dictionary


'''
% python
>>> import mymod
>>> mymod.test('mymod.py')
(10, 291)
'''

"""
A generator expression can have the same effect (though the instructor might take
off points for excessive magic!):

def countlines(name): return sum(+1 for line in open(name))
def countchars(name): return sum(len(line) for line in open(name))
"""

'''
The “ambitious” part of this exercise (passing in a file object so you only open the
file once), will require you to use the seek method of the built-in file object. It works
like C’s fseek call (and may call it behind the scenes): seek resets the current position
in the file to a passed-in offset. After a seek, future input/output operations
are relative to the new position. To rewind to the start of a file without closing and
reopening it, call file.seek(0); the file read methods all pick up at the current
position in the file, so you need to rewind to reread. Here’s what this tweak would
look like:
'''
def countLines(file):
    file.seek(0)                                                # Rewind to start of file
    return len(file.readlines())

def countChars(file):
    file.seek(0)                                                # Ditto (rewind if needed)
    return len(file.read())

def test(name):
    file = open(name)                                           # Pass file object
    return countLines(file), countChars(file)                   # Open file only once

"""
>>> import mymod2
>>> mymod2.test("mymod2.py")
(11, 392)
"""
