"Mixed Usage Modes: __name__ and __main__"
'''
lets you both import a file as a module and run it as a
standalone program

each module has a built-in attribute called __name__, which
Python creates and assigns automatically as follows:
    • If the file is being run as a top-level program file, __name__ is set to the string
    "__main__" when it starts.

    • If the file is being imported instead, __name__ is set to the module’s name as known
    by its clients.

The upshot is that a module can test its own __name__ to determine whether it’s being
run or imported.
'''
