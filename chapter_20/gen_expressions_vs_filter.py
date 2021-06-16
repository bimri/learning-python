'''
filter is an iterable
in 3.X that generates its results on request, a generator expression with an if clause is
operationally equivalent
'''
# generator seems marginally simpler than the filter here
line = 'aa bbb c'
print(
    ''.join(x for x in line.split() if len(x) > 1)          # Generator with 'if
)

print(
''.join(filter(lambda x: len(x) > 1, line.split()))         # Similar to filter
)


"there is always a statement-based equivalent to a generator expression"
print(
    ''.join(x.upper() for x in line.split() if len(x) > 1)
)

# Statement equivalent?
"the statement form isn’t quite the same"
"cannot produce items one at a time"
res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()                                    # this is also a join

print(res)


'''
The true equivalent to a generator expression would be a generator
function with a yield
'''