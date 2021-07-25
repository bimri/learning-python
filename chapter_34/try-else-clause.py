"The try else Clause"
'''
The purpose of the else clause is not always immediately obvious to Python newcomers.
Without it, though, there is no direct way to tell (without setting and checking
Boolean flags) whether the flow of control has proceeded past a try statement because
no exception was raised, or because an exception occurred and was handled. Either
way, we wind up after the try:
'''
try:
    ... # run code ...
except IndexError:
    ... # handle exception ...
# Did we get here because the try failed or not?


""" 
Much like the way else clauses in loops make the exit cause more apparent, the else
clause provides syntax in a try that makes what has happened obvious and unambiguous: 
""" 
try:
    ... # run code ...
except IndexError:
    ... # handle exceptions ...
else:
    ... # no exceptions occured ...

'You can almost emulate an else clause by moving its code into the try block:'
try:
    ... # run code ...
    ... # no exception occured ... 
except IndexError:
    ... # handle exception ...

""" 
This can lead to incorrect exception classifications, though. If the “no exception occurred”
action triggers an IndexError, it will register as a failure of the try block and
erroneously trigger the exception handler below the try (subtle, but true!). By using an
explicit else clause instead, you make the logic more obvious and guarantee that
except handlers will run only for real failures in the code you’re wrapping in a try, not
for failures in the else no-exception case’s action.
"""
