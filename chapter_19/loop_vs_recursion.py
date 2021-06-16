L = [1, 2, 3, 4, 5]

sum = 0
while L:
    sum += L[0]
    L = L[1:]

print(sum)


"For loops itertae automatically, making recursion extraneous"
"and less efficient in terms of memory space & execution time"
L = [1,2,3,4,5]
sum = 0

for x in L: 
    sum +=x

print(sum)
