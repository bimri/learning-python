"Exception Design Tips and Gotchas"
'Catching Too Much: Avoid Empty except and Exception'
'''
Exception handler generality is a key design choice. Python lets you pick
and choose which exceptions to catch, but you sometimes have to be careful to not be
too inclusive.

Perhaps worse, such code might also catch unrelated system exceptions. Even things
like memory errors, genuine programming mistakes, iteration stops, keyboard interrupts,
and system exits raise exceptions in Python. Unless you’re writing a debugger or
similar tool, such exceptions should not usually be intercepted in your code.
'''
def func():
    try:
        ...                             # IndexError is raised in here 
    except:
        ...                             # But everything comes here and dies! 
    
try:
    func() 
except IndexError:                      # Exception should be processed here
    ...


'''
scripts normally exit when control falls off the end of the top-level file.
However, Python also provides a built-in sys.exit(statuscode) call to allow early terminations.
This actually works by raising a built-in SystemExit exception to end the
program, so that try/finally handlers run on the way out and special types of programs
can intercept the event. Because of this, a try with an empty except might unknowingly
prevent a crucial exit, as in the following file (exiter.py):
'''
import sys 

def bye():
    sys.exit(40)                        # Crucial error: abort now!

try:
    bye()
except:
    print('got it')                     # Oops--we ignored the exit
print('continuing...') 


'''
You simply might not expect all the kinds of exceptions that could occur during an
operation. Using the built-in exception classes of the prior chapter can help in this
particular case, because the Exception superclass is not a superclass of SystemExit:

In other cases, though, this scheme is no better than an empty except clause—because
Exception is a superclass above all built-in exceptions except system-exit events, it still
has the potential to catch exceptions meant for elsewhere in the program.
'''
try: 
    bye()
except Exception:                       # Won't catch exits, but _will_catch many others
    ...


'''
Probably worst of all, both using an empty except and catching the Exception superclass
will also catch genuine programming errors, which should be allowed to pass most of
the time. In fact, these two techniques can effectively turn off Python’s error-reporting
machinery

The coder here assumes that the only sort of error that can happen when indexing a
dictionary is a missing key error. But because the name myditctionary is misspelled (it
should say mydictionary), Python raises a NameError instead for the undefined name
reference, which the handler will silently catch and ignore. The event handler will incorrectly
fill in a None default for the dictionary access, masking the program error.

Moreover, catching Exception here will not help—it would have the exact same effect
as an empty except, happily and silently filling in a default and masking a genuine
program error you will probably want to know about.
'''
# mydictionary = {...}
# ...

# try:
#     x = myditctionary['spam']           # Oops: misspelled
# except:
#     x = None                            # Assume we got KeyError
# ...continue here with x...

'''
As a rule of thumb, be as specific in your handlers as you can be—empty except clauses
and Exception catchers are handy, but potentially error-prone. In the last example, for
instance, you would be better off saying except KeyError: to make your intentions
explicit and avoid intercepting unrelated events. In simpler scripts, the potential for
problems might not be significant enough to outweigh the convenience of a catchall,
but in general, general handlers are generally trouble.
'''
