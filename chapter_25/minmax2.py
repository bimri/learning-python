print('I am:', __name__)

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == '__main__':
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))               # Self-test code
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))



"printing the value of __name__ at the top here to trace its value."
'''
Python creates and assigns this usage-mode variable as soon as it starts loading a file. When we run
this file as a top-level script, its name is set to __main__, so its self-test code kicks in
automatically:

    c:\code> python minmax2.py
    I am: __main__
    16


If we import the file, though, its name is not __main__, so we must explicitly call the
function to make it run:

    c:\code> python
    >>> import minmax2
    I am: minmax2
    >>> minmax2.minmax(minmax2.lessthan, 's', 'p', 'a', 'a')
    'a'

Again, regardless of whether this is used for testing, the net effect is that we get to use
our code in two different roles—as a library module of tools, or as an executable program.
'''
