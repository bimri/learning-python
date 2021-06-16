"Timing Script"
'Test the relative speed of iteration tool alternatives'

import sys, timer                                               # import timer functions
reps = 1000
repslist = list(range(reps))                                    # Hoist out, list in both 2.x/3.x

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res 

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))                             # Use list() here in 3.X only
    # return map(abs, repslist)

def genExpr():
    return list(abs(x) for x in repslist)                       # list() required to force results

def genFunc():
    def gen():
            for x in repslist:
                yield abs(x)
    return list(gen())                                          # list() required to force results


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))   


'''
On PyPy alone, list comprehensions beat map in this test, but the fact that all of PyPy’s
results are so much quicker today seems the larger point here. On CPython, map is still
quickest so far.
'''