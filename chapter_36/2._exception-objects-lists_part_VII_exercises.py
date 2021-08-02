""" 
2. Exception objects and lists. Change the oops function you just wrote to raise an
exception you define yourself, called MyError. Identify your exception with a class
(unless you’re using Python 2.5 or earlier, you must). Then, extend the try statement
in the catcher function to catch this exception and its instance in addition to
IndexError, and print the instance you catch.
""" 
class MyError(Exception): pass 

def oops():
    raise MyError('Spam!')

def doomed():
    try:
        oops() 
    except IndexError:
        print('caught an index error!')
    except MyError as err:
        print('caught error:', MyError, err)
    else:
        print('no error caught...') 
    

if __name__ == '__main__': doomed() 
