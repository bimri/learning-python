'''
Just like generator functions, generator expressions are a memory-space optimization
—they do not require the entire result list to be constructed all at once, as the squarebracketed
list comprehension does.

Also like generator functions, they divide the work
of results production into smaller time slices—they yield results in piecemeal fashion,
instead of making the caller wait for the full set to be created in a single call.
'''

'''
On the other hand, generator expressions may also run slightly slower than list comprehensions
in practice, so they are probably best used only for very large result sets,
or applications that cannot wait for full results generation.
'''