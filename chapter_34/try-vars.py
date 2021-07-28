"Scopes and try except Variables"
try:
    1/0
except Exception as X:
    print(X)

# print(X)                                # NameError: name 'X' is not defined

'''
Unlike compression loop variables, though, this variable is removed after the except
block exits in 3.X. It does so because it would otherwise retain a reference to the runtime
call stack, which would defer garbage collection and thus retain excess memory space.
This removal occurs, though, even if you’re using the name elsewhere, and is more
extreme policy than that used for comprehensions:
'''
X = 89
try:
    1/0
except Exception as X:                  # 3.X localizes _and_ removes on exit
    print(X)

# print(X)                                # NameError: name 'X' is not defined


X = 99 
c = {X for X in 'spam'}                  # 2.X/3.X localizes only: not removed
print(c)
print(X)


'''
Because of this, you should generally use unique variable names in your try statement’s
except clauses, even if they are localized by scope. If you do need to reference the
exception instance after the try statement, simply assign it to another name that won’t
be automatically removed:
'''
try:
    1 / 0 
except Exception as X:                  # Python removes this reference 
    print(X) 
    Saveit = X                          # Assign exc to retain exc if needed 

# print(X)
print("Saveit = " + str(Saveit))
