'''
Although the __getitem__ technique of the prior section works, it’s really just a fallback
for iteration. Today, all iteration contexts in Python will try the __iter__ method first,
before trying __getitem__. That is, they prefer the iteration protocol we learned about
in Chapter 14 to repeatedly indexing an object; only if the object does not support the
iteration protocol is indexing attempted instead. Generally speaking, you should prefer
__iter__ too—it supports general iteration contexts better than __getitem__ can.
'''


"""
This iterable object interface is given priority and attempted first. Only if no such
__iter__ method is found, Python falls back on the __getitem__ scheme and repeatedly
indexes by offsets as before, until an IndexError exception is raised.
"""
