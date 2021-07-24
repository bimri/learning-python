"Exceptions: The Short Story"
'Default Exception Handler'

def fetcher(obj, index): 
    return obj[index]

print(fetcher([1,2,3], 1))

x = 'bimri'
print(fetcher(x, 1))
print(fetcher(x, 2))
print(fetcher(x, 3))


""" 
However, if we ask this function to index off the end of the string, an exception will be
triggered when the function tries to run obj[index]. Python detects out-of-bounds indexing
for sequences and reports it by raising (triggering) the built-in IndexError exception:

Because our code does not explicitly catch this exception, it filters back up to the top
level of the program and invokes the default exception handler, which simply prints the
standard error message.

stack trace—a list of all the lines and functions that were active when the exception occurred.
"""
# IndexError: string index out of range
# print(fetcher(x, 5))



""" 
In a more realistic program launched outside the interactive prompt, after printing an
error message the default handler at the top also terminates the program immediately.
That course of action makes sense for simple scripts; errors often should be fatal, and
the best you can do when they occur is inspect the standard error message.
""" 


"Catching Exceptions"
try:
    fetcher(x, 5)
except IndexError as err:                               # <== exception handler: Catch and recover
    print('got exception')
    print(err)


"The net effect is to wrap a nested block of code in an error handler that intercepts the block’s exceptions."
def catcher():
    try: 
        fetcher(x, 5)
    except IndexError as err:                               # <== exception handler: Catch and recover
        print('got exception')
    print('continuing')


print()
catcher()


""" 
This time, after the exception is caught and handled, the program resumes execution
after the entire try statement that caught it—which is why we get the “continuing”
message here. We don’t see the standard error message, and the program continues on
its way normally.

Notice that there’s no way in Python to go back to the code that triggered the exception
(short of rerunning the code that reached that point all over again, of course). Once
you’ve caught the exception, control continues after the entire try that caught the
exception, not after the statement that kicked it off. In fact, Python clears the memory
of any functions that were exited as a result of the exception, like fetcher in our example;
they’re not resumable. The try both catches exceptions, and is where the program
resumes.
"""
