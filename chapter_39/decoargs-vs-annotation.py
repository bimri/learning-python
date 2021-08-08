"Decorator Arguments Versus Function Annotations"
# Using decorator arguments (3.X + 2.X)

def rangetest(**argchecks):
    def onDecorator(func):
        def onCall(*pargs, **kargs):
            print(argchecks)
            for check in argchecks:
                pass                                        # Add validation code here
            return func(*pargs, **kargs)
        return onCall
    return onDecorator

@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c):                                          # func = rangetest(...)(func)
    print(a + b + c)

func(1, 2, c=3)                                             # Runs onCall, argchecks in scope

# Using function annotations (3.X only)

def rangetest(func):
    def onCall(*pargs, **kargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks:
            pass                                            # Add validation code here
        return func(*pargs, **kargs)
    return onCall

@rangetest
def func(a:(1, 5), b, c:(0.0, 1.0)):                        # func = rangetest(func)
    print(a + b + c)

func(1, 2, c=3)                                             # Runs onCall, annotations on func


'Other Applications: Type Testing (If You Insist!)'
def typetest(**argchecks):
    def onDecorator(func):
        ...
        def onCall(*pargs, **kargs):
            positionals = list(allargs)[:len(pargs)]
            for (argname, type) in argchecks.items():
                if argname in kargs:
                    if not isinstance(kargs[argname], type):
                        ...
                        raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            ...
                            raise TypeError(errmsg)
                        else:
                            # Assume not passed: default
                            ...
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@typetest(a=int, c=float)
def func(a, b, c, d):   # func = typetest(...)(func)
    ...


func(1, 2, 3.0, 4)                                          # OK
func('spam', 2, 99, 4)                                      # Triggers exception correctly
