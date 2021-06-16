"Name Resolution: The LEGB Rule"

'''
~ Name assignments create or change local names by default.
~ Name references search at most 4 scopes: local, then enclosing 
  functions(if any), then global, then built-in.
~ Names desclared in global and nonlocal statements map assigned 
  names to enclosing module and function scopes, respectively.
'''


'''there are technically three more scopes in
Python—temporary loop variables in some comprehensions, exception reference variables
in some try handlers, and local scopes in class statements. The first two of these
are special cases that rarely impact real code, and the third falls under the LEGB umbrella
rule'''


"Comprehension variables"
'''such variables are local to the expression itself in all comprehension forms:
    generator, list, set, and dictionary
'''

'''for loop statements never localize their variables
to the statement block in any Python'''


"Exception variables"
'''
such variables are local to that block, and in fact are removed when the block is exited
except
'''


"statement class"
'''
creates a new local scope too for the names assigned inside the top level of its block

As for def, names assigned inside a class don’t clash with names elsewhere, and follow 
the LEGB lookup rule, where the class block is the “L” level. Like modules and imports, 
these names also morph into class object attributes after the class statements ends.

Unlike functions: names are not created per call class. class object calls generate 
instances which inherit names assigned in the class and record per-object state
as attributes.
'''

"classes themselves are skipped by scope lookups"
"their names must be fetched as object attributes"
