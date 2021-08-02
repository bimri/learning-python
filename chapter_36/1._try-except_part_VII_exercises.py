"""
1. try/except. Write a function called oops that explicitly raises an IndexError exception
when called. Then write another function that calls oops inside a try/except
statement to catch the error. What happens if you change oops to raise a
KeyError instead of an IndexError? Where do the names KeyError and IndexError
come from? (Hint: recall that all unqualified names generally come from one of
four scopes.)
"""

def oops():
    raise IndexError

def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!')
    else:
        print('no error caught...') 


if __name__ == '__main__': doomed()
