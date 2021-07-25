"The try/except/else Statement"
'''
Syntactically, the try is a compound, multipart statement. It starts with a try header
line, followed by a block of (usually) indented statements; then one or more except
clauses that identify exceptions to be caught and blocks to process them; and an optional
else clause and block at the end. You associate the words try, except, and
else by indenting them to the same level (i.e., lining them up vertically). For reference,
here’s the general and most complete format in Python 3.X:
'''

try:
    statements                          # Run this main action first 
except name1:
    statements                          # Run if name1 is raised during try block 
except (name2, name3):          
    statements                          # Run if any of these exceptions occur 
except name4 as var:    
    statements                          # Run if name4 is raised, assign instance raised to var
except:
    statements                          # Run for all other exceptions raised 
else:
    statements                          # Run if no exception was raised during try block 


""" 
Semantically, the block under the try header in this statement represents the main
action of the statement—the code you’re trying to run and wrap in error processing
logic. The except clauses define handlers for exceptions raised during the try block,
and the else clause (if coded) provides a handler to be run if no exceptions occur.
""" 
