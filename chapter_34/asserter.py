"Example: Trapping Constraints (but Not Errors!)"
'''
Assertions are typically used to verufy program conditions during development.
When displayed, their error message test automatically includes source code line
information and the value listed in the assert statement.
'''
def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2 


if __name__ == "__main__":
    f(20)


""" 
It’s important to keep in mind that assert is mostly intended for trapping user-defined
constraints, not for catching genuine programming errors. Because Python traps programming
errors itself, there is usually no need to code assert to catch things like outof-
bounds indexes, type mismatches, and zero divides:
""" 
def reciprocal(x):
    '''
    Such assert use cases are usually superfluous—because Python raises exceptions on
    errors automatically, you might as well let it do the job for you. As a rule, you don’t
    need to do error checking explicitly in your own code.
    '''
    assert x != 0               # A generally useless assert!
    return 1 / x                # Python checks for zero automatically 


""" 
Of course, there are exceptions for most rules, if a function has to perform long-running 
or unrecoverable actions before it reaches the place where an exception will be triggered, 
you still might want to test for errors. Even in this case, though, be careful not to make 
your tests overly specific or restrictive, or you will limit your code’s utility.
""" 
