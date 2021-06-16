"Timing Module: Homegrown"
# to get the total time taken to run multiple calls to a function 
# with arbitrary positional arguments
import time 

# some classic mistakes in both function design and benchmarking
def timer(func, *args):                             # Simplistic timing function
    start = time.time()
    for i in range(1000):
        func(*args)
    return time.time() - start                     # Total elapsed time is seconds


'Run on Interactive Prompt'
# >>> from timer0 import timer                      
# >>> timer(pow, 2, 1000)                           # Time to call pow(2, 1000) 1000 times
# timer(str.upper, 'spam')                          # Time to call 'spam'.upper() 1000 times
