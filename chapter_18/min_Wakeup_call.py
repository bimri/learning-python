def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res 

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)                    # Or, in Python 2.4+: return sorted(args)[0]
    tmp.sort()    
    return tmp[0]

print(min1(3, 4, 2, 1))
print(min2('bb', 'aa'))
print(min3([2,2], [1,1], [3,3]))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res 

def lessthan(x, y): return x < y
def grtthan(x, y): return x > y 

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))       # self-test code
print(minmax(grtthan, 4, 2, 1, 5, 6, 3))
