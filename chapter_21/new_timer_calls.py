'''
• time.perf_counter() returns the value in fractional seconds of a performance
counter, defined as a clock with the highest available resolution to measure a short
duration. It includes time elapsed during sleep states and is system-wide.
• time.process_time() returns the value in fractional seconds of the sum of the system
and user CPU time of the current process. It does not include time elapsed
during sleep, and is process-wide by definition.
'''


'''
The time.clock call is still usable on Windows today, as shown in this book. It is documented
as being deprecated in 3.3’s manuals, but issues no warning when used there
—meaning it may or may not become officially deprecated in later releases. If needed,
you can detect a Python 3.3 or later with code like this, which I opted to not use for
the sake of brevity and timer comparability:
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
        timer = time.perf_counter # or process_time
    else:
        timer = time.clock if sys.platform[:3] == 'win' else time.time


    try:
        timer = time.perf_counter                       # or process_time
    except AttributeError:
        timer = time.clock if sys.platform[:3] == 'win' else time.time
'''
