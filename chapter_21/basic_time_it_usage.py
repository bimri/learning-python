'''
With timeit, tests are specified by either callable objects or statement strings; the latter
can hold multiple statements if they use ; separators or \n characters for line breaks,
and spaces or tabs to indent statements in nested blocks (e.g., \n\t). Tests may also
give setup actions, and can be launched from both command lines and API calls, and
from both scripts and the interactive prompt.
'''

"Interactive usage and API calls"
'''
the timeit module’s repeat call returns a list giving the total time taken
to run a test a number of times, for each of repeat runs—the min of this list yields the
best time among the runs, and helps filter out system load fluctuations that can otherwise
skew timing results artificially high.
'''
import timeit

print(
    min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5))
)


'''
timeit builds, compiles, and executes a function
def statement string that embeds the test string, thereby avoiding a function call per
inner loop.
'''



"Command-line usage"
'''
The timeit module has reasonable defaults and can be also run as a script, either by
explicit filename or automatically located on the module search path with Python’s
–m flag
'''

'''

            c:\code> C:\python33\Lib\timeit.py -n 1000 "[x ** 2 for x in range(1000)]"
            1000 loops, best of 3: 506 usec per loop
            c:\code> python -m timeit -n 1000 "[x ** 2 for x in range(1000)]"
            1000 loops, best of 3: 504 usec per loop
            c:\code> py −3 -m timeit -n 1000 -r 5 "[x ** 2 for x in range(1000)]"
            1000 loops, best of 5: 505 usec per loop

'''



"Timing multiline statements"
'''
To time larger multiline sections of code in API call mode, use line breaks and tabs or
spaces to satisfy Python’s syntax; code read from a source file already will.
'''
print(
    min(timeit.repeat(number=10000, repeat=3,
        stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1"))
)

print(
    min(timeit.repeat(number=10000, repeat=3,
        stmt="L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"))
)

print(
    min(timeit.repeat(number=10000, repeat=3,
        stmt="L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]"))
)

'''
To run multiline statements like these in command-line mode, appease your shell by
passing each statement line as a separate argument, with whitespace for indentation—
timeit concatenates all the lines together with a newline character between them, and
later reindents for its own statement nesting purposes.
'''

'''
                c:\code> py −3 -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "i=0" "while i < len(L):"
                " L[i] += 1" " i += 1"
                1000 loops, best of 3: 1.54 usec per loop
                
                c:\code> py −3 -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
                1000 loops, best of 3: 0.959 usec per loop
'''



"Other usage modes: Setup, totals, and objects"
'''
The timeit module also allows you to provide setup code that is run in the main statement’s
scope, but whose time is not charged to the main statement’s total—potentially
useful for initialization code you wish to exclude from total time, such as imports of
required modules, test function definition, and test data creation.

To specify setup code, use a –s in command-line mode

As a rule of thumb, though, the more code you include in a test statement,
the more applicable its results will generally be to realistic code:
'''

'''
            c:\code> python -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
            1000 loops, best of 3: 0.956 usec per loop

            c:\code> python -m timeit -n 1000 -r 3 -s "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
            1000 loops, best of 3: 0.775 usec per loop 


            >>> from timeit import repeat

            >>> min(repeat(number=1000, repeat=3,
            setup='from mins import min1, min2, min3\n'
                    'vals=list(range(1000))',
            stmt= 'min3(*vals)'))
            0.0387865921275079

            >>> min(repeat(number=1000, repeat=3,
            setup='from mins import min1, min2, min3\n'
                    'import random\nvals=[random.random() for i in range(1000)]',
            stmt= 'min3(*vals)'))
            0.275656482278373  

'''


'''
With timeit, you can also ask for just total time, use the module’s class API, time
callable objects instead of strings, accept automatic loop counts, and use class-based
techniques and additional command-line switches and API argument options


            c:\code> py −3
            >>> import timeit
            >>> timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=1000) # Total time
            0.5238125259325834
            
            >>> timeit.Timer(stmt='[x ** 2 for x in range(1000)]').timeit(1000) # Class API
            0.5282652329644009
            
            >>> timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=3)
            [0.5299034147194845, 0.5082454007998365, 0.5095136232504416]
            
            >>> def testcase():
            y = [x ** 2 for x in range(1000)] # Callable objects or code strings
            
            >>> min(timeit.repeat(stmt=testcase, number=1000, repeat=3))
            0.5073828140463377
'''
