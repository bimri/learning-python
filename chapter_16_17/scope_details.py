'''the interactive prompt is a module named __main__
that prints results and doesn’t save its code
it’s like the top level of a module file'''

'''Functions - provide nested namespaces(scopes) that 
localize the names they use, such that names inside a 
function won't clash with those outside it(in a module 
or another function)'''

"Functions define a local scope and modules define a global scope"


'''
The enclosing module is a global scope: - 
    Global variables become attributes of a module object to the outside world
    after imports
The global scope spans a single file only: -
    names at the top level of a file are global to code within that single file 
    only
Assigned names are local unless declared global or nonlocal: -
    names assigned inside a function definition are put in the local scope
    
    need to assign a name that lives at the top level of the module enclosing the function, you can do so by declaring
    it in a global statement inside the function    

    need to assign a namet that lives in an enclosing def as of Python 3.X you can do so by declaring it in a
    nonlocal statement

Names not assigned a value in the function definition are assumed to be enclosing scope
locals 

Each call to a function creates a new local scope: - 
    Every time you call a function, you create a new local scope

When you hear “global” in Python, think “module.”
'''
