X = 11

import moda                         # Gain access to names in moda
moda.f()                            # Sets moda.X, not this file's X
print(X, moda.X)


'''
import operations never give upward visibility to code in imported files
—an imported file cannot see names in the importing file.

    • Functions can never see names in other functions, unless they are physically enclosing.
    • Module code can never see names in other modules, unless they are explicitly imported.

'''
