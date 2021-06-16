import sys, timer2

reps = 10000
repslist = range(reps) # Pull out range list time for 2.X
from math import sqrt # Not math.sqrt: adds attr fetch time

def mathMod():
    for i in repslist:
        res = sqrt(i)
    return res

def powCall():
    for i in repslist:
        res = pow(i, .5)
    return res

def powExpr():
    for i in repslist:
        res = i ** .5
    return res

print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1=3, _reps=1000)
    print ('%s: %.5f => %s' % (test.__name__, elapsed, result))



'''
C:\code> c:\python33\python
>>>
>>> def dictcomp(I):
return {i: i for i in range(I)}
>>> def dictloop(I):
        new = {}
        for i in range(I): new[i] = i
        return new
        
>>> dictcomp(10)
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>> dictloop(10)
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>>
>>> from timer2 import total, bestof
>>> bestof(dictcomp, 10000)[0] # 10,000-item dict
0.0017095345403959072
>>> bestof(dictloop, 10000)[0]
0.002097576400046819
>>>
>>> bestof(dictcomp, 100000)[0] # 100,000-items: 10X slower
0.012716923463358398
>>> bestof(dictloop, 100000)[0]
0.014129806355413166
>>>
>>> bestof(dictcomp, 1000000)[0] # 1 of 1M-items: 10X time
0.11614425187337929
>>> bestof(dictloop, 1000000)[0]
0.1331144855439561
>>>
>>> total(dictcomp, 1000000, _reps=50)[0] # Total to make 50 1M-item dicts
5.8162020671780965
>>> total(dictloop, 1000000, _reps=50)[0]
6.626680761285343
'''    