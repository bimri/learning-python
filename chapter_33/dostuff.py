"""
In fact, realistic C programs often have as much code devoted to error detection as to
doing actual work. But in Python, you don’t have to be so methodical (and neurotic!).
You can instead wrap arbitrarily vast pieces of a program in exception handlers and
simply write the parts that do the actual work, assuming all is normally well: 
""" 
def doStuff():                      # Python code 
    doFirstThing()                  # We don't care about exceptions here 
    doNextThing()                   # so we don't need to detect them 
    ...
    doLastThing()                   


if __name__ == "__main__":
    try:
        doStuff()               # This is where we care about results, 
    except:                     # so it's the only place we must check for them
        badEnding() 
    else: 
        goodEnding() 


'''
Because control jumps immediately to a handler when an exception occurs, there’s no
need to instrument all your code to guard for errors, and there’s no extra performance
overhead to run all the tests. Moreover, because Python detects errors automatically,
your code often doesn’t need to check for errors in the first place. The upshot is that
exceptions let you largely ignore the unusual cases and avoid error-checking code that
can distract from your program’s goals.
'''
