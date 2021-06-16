" [ expression for target in iterable ] "

# you can code any number of nested loops in a list comprehension for
# each may have an optional associated test to act as a filter if

'''
[ 
    expression for target1 in iterable if condition1
               for target2 in iterable if condition2 ...
               for targetN in iterable if conditionN ]
'''
res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

# verbose equivalent
res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)


# traverses strings
ts = [x + y for x in 'ALL' for y in 'all']
print(ts)

multi = [x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]
print("multi", multi)

cmplx = [ x + y + z for x in 'spam' if x in 'sm'
                    for y in 'SPAM' if y in ('P', 'A')
                    for z in '123' if z > '1']
print("complex", cmplx)


# nested for clauses applied to numeric objects
"combines even numbers from 0 through 4 with odd numbers from 0 through 4"
nmo = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(nmo)

'state-based code'
res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

print(res)


'''
Recall that if you’re confused about what a complex list comprehension does, you can
always nest the list comprehension’s for and if clauses inside each other like this—
indenting each clause successively further to the right—to derive the equivalent statements.
'''
