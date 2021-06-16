'''
Syntax                                  Location                                                            Interpretation

func(value)                             Caller                                                      Normal argument: matched by position
func(name=value)                        Caller                                                      Keyword argument: matched by name
func(*iterable)                         Caller                                                      Pass all objects in iterable as individual positional arguments
func(**dict)                            Caller                                                      Pass all key/value pairs in dict as individual keyword arguments
def func(name)                          Function                                                    Normal argument: matches any passed value by position or name
def func(name=value)                    Function                                                    Default argument value, if not passed in the call
def func(*name)                         Function                                                    Matches and collects remaining positional arguments in a tuple
def func(**name)                        Function                                                    Matches and collects remaining keyword arguments in a dictionary
def func(*other, name)                  Function                                                    Arguments that must be passed by keyword only in calls (3.X)
def func(*, name=value)                 Function                                                    Arguments that must be passed by keyword only in calls (3.X)
'''