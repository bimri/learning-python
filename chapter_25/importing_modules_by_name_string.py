'''
you can’t use import statements directly to load a module given
its name as a string—Python expects a variable name that’s taken literally and not
evaluated, not a string or expression.

To get around this, you need to use special tools to load a module dynamically from a
string that is generated at runtime. The most general approach is to construct an
import statement as a string of Python code and pass it to the exec built-in function to
run (exec is a statement in Python 2.X, but it can be used exactly as shown here—the
parentheses are simply ignored):

    >>> modname = 'string'
    >>> exec('import ' + modname) # Run a string of code
    >>> string # Imported in this namespace
    <module 'string' from 'C:\\Python33\\lib\\string.py'>


exec function (and its cousin for expressions, eval
    - It compiles a string of code and passes it to the Python interpreter to
      be executed. 
    - In Python, the byte code compiler is available at runtime, so you can write
      programs that construct and run other programs like this. 
    - By default, exec runs the code in the current scope, but you can get more specific by passing in optional namespace
      dictionaries if needed. 
    - It also has security issues noted earlier in the book, which
      may be minor in a code string you are building yourself.
'''


"Direct Calls: Two Options"
'''
The only real drawback to exec here is that it must compile the import statement each
time it runs, and compiling can be slow.

Precompiling to byte code with the compile
built-in may help for code strings run many times, but in most cases it’s probably
simpler and may run quicker to use the built-in __import__ function to load from a
name string instead

The effect is similar, but __import__ returns
the module object, so assign it to a name here to keep it:
    >>> modname = 'string'
    >>> string = __import__(modname)
    >>> string
    <module 'string' from 'C:\\Python33\\lib\\string.py'>


the newer call importlib.import_module does the same
work, and is generally preferred in more recent Pythons for direct calls to import by
name string—at least per the current “official” policy stated in Python’s manuals:
    >>> import importlib
    >>> modname = 'string'
    >>> string = importlib.import_module(modname)
    >>> string
    <module 'string' from 'C:\\Python33\\lib\\string.py'>

The import_module call takes a module name string, and an optional second argument
that gives the package used as the anchor point for resolving relative imports, which
defaults to None.
'''