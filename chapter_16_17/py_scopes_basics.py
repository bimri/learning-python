X = 87                      # Global(module) scope X

def func():
    X = 809                 # Local(function) scope X: a different variable
    print(X)

print(X)                    # global scope variable X fetched
func()                      # local scope variable X printed
