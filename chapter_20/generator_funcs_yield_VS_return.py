'''
`Generator functions`
    - are like normal functions in most respects(def statement)
    - when created, they compiled specially into an object that 
        supports the the iteration protocol
    - when called, they don't return a result: they return a result
        generator that can appear in any iteration context.
'''


'''
`State suspension`
    - they are often a useful alternative to both computing an entire series
        of values up front and manually saving and restoring state in classes
    - The state that generator functions retain when they are suspended includes 
        both their code location, and their entire local scope.
    - their local variables retain information between results and make it 
        available when the functions are resumed

functions containing a yield statement are compiled specially
as generators—they are not normal functions, but rather are built to return an object
with the expected iteration protocol methods. When later called, they return a generator
object that supports the iteration interface with an automatically created method
named __next__ to start or resume execution


Generator functions may also have a return statement that, along with falling off the
end of the def block, simply terminates the generation of values—technically, by raising
a StopIteration exception after any normal function exit actions. From the caller’s
perspective, the generator’s __next__ method resumes the function and runs until either
the next yield result is returned or a StopIteration is raised.
'''