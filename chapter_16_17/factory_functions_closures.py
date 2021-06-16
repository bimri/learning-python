def maker(N):
    def action(X):                  # Make and return action
        return X ** N               # action retains N from enclosing scope
    return action

f = maker(2)
print(f)

print(f(3))                         # Pass 3 to X, N remembers 2: 3 ** 2
print(f(4))                         # 4 ** 2


g = maker(3)                        # g remembers 3, f remembers 2
print(g(4))                         
print(f(4))                         # 4 ** 2


# lambda functions retain state too
def maker(N):
    return lambda X: X ** N

h = maker(3)
print(h(4))                         # 4 ** 3 again
