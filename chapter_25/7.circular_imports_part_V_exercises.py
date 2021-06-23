'''
Circular imports. The short story is that importing recur2 first works because the
recursive import then happens at the import in recur1, not at a from in recur2.
The long story goes like this: importing recur2 first works because the recursive
import from recur1 to recur2 fetches recur2 as a whole, instead of getting specific
names. recur2 is incomplete when it’s imported from recur1, but because it uses
import instead of from, you’re safe: Python finds and returns the already created
recur2 module object and continues to run the rest of recur1 without a glitch.
When the recur2 import resumes, the second from finds the name Y in recur1 (it’s
been run completely), so no error is reported.

Running a file as a script is not the same as importing it as a module; these cases
are the same as running the first import or from in the script interactively. For
instance, running recur1 as a script works, because it is the same as importing
recur2 interactively, as recur2 is the first module imported in recur1. Running
recur2 as a script fails for the same reason—it’s the same as running its first import
interactively.
'''