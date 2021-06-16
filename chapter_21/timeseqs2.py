import sys, timer                                               # import timer functions
reps = 1000
repslist = list(range(reps))                                    # Hoist out, list in both 2.x/3.x


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res
    
def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist))              # list() in 3.X only

def genExpr():
    return list(x + 10 for x in repslist)                       # list() in 2.X + 3.X

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())                                          # list in 2.X + 3.X


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
        


'''
For deeper truth, change this code to apply a simple user-defined function
in all five iteration techniques timed. For instance (from timeseqs2B.
py of the book’s examples):

    def F(x): return x
    def listComp():
        return [F(x) for x in repslist]
    def mapCall():
        return list(map(F, repslist))

The results, in file timeseqs-results.txt, are then relatively similar to using
a built-in function like abs—at least in CPython, map is quickest. More
generally, among the five iteration techniques, map is fastest today if all
five call any function, built in or not, but slowest when the others do not.
'''