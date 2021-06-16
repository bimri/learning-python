f = open('script2.py')                                      # Read a four-line script file in this directory

print(f.readline())
print(f.readline())                                         # readline loads one line on each call
print(f.readline())
print(f.readline())                                         # Last lines may have a \n or not
print(f.readline())                                         # Returns empty string at end-of-file


#%%
'''raises a built-in exception at __next__ StopIteration
end-of-file instead of returning an empty string'''
f = open('script2.py')                                      # __next__ loads one line on each call too

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
# print(f.__next__())                                         # StopIteration Exception


# %%
'''NEW WAY TO READ FILES'''
for line in open('script2.py'):                               # Use file iterators to read by lines                            
    print(line.upper(), end='')                               # Calls __next__, catches StopIteration

print()

#%%
'''OLDER WAY'''
for line in open('script2.py').readlines():
    print(line.upper(), end='')

print()


''' With While loop'''
f = open('script2.py')

while True:                                                     # may run slower than the iterator-based for loop version
    line = f.readline()
    if not line: break
    print(line.upper(), end='')
