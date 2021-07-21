"Flexibility: Call ordering assumptions"
'''
Routing with super also assumes that you really mean to pass method calls throughout
all your classes per the MRO, which may or may not match your call ordering requirements.
'''
# What if method call ordering needs differ from the MRO?

class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()

class D(B, C):
    def __init__(self): print('D.__init__'); C.__init__(self); B.__init__(self)


if __name__ == '__main__':
    X = D()                     # It's the MRO xor explicit calls...

    """ 
    Similarly, if you want some methods to not run at all, the super automatic path won’t
    apply as directly as explicit calls may, and will make it difficult to take more explicit
    control of the dispatch process. In realistic programs with many methods, resources,
    and state variables, these seem entirely plausible scenarios. While you could reorder
    superclasses in D for this method, that may break other expectations.
    """
    