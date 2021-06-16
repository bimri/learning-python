def runner(stmts, pythons=None, tracecmd=False):
    for (number, repeat, setup, stmt) in stmts:
        if not pythons:
            ...
            best = min(timeit.repeat(
            setup=setup, stmt=stmt, number=number, repeat=repeat))
        else:
            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))
            ...
            for (ispy3, python) in pythons:
                ...
                cmd = '%s -m timeit -n %s -r %s %s %s' % (python, number, repeat, setup, args)
                