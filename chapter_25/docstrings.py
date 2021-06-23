"Docstrings: Module Documentation at Work"
'''
>>> import formats
>>> help(formats)
Help on module formats:

    NAME
        formats
    DESCRIPTION
        File: formats.py (2.X and 3.X)
        Various specialized string display formatting utilities.
        Test me with canned self-test or command-line arguments.
        To do: add parens for negative money, add more features.
    FUNCTIONS
        commas(N)
            Format positive integer-like N for display with
            commas between digit groupings: "xxx,yyy,zzz".
        money(N, numwidth=0, currency='$')
            Format number N for display with commas, 2 decimal digits,
            leading $ and sign, and optional padding: "$ -xxx,yyy.zz".
            numwidth=0 for no space padding, currency='' to omit symbol,
            and non-ASCII for others (e.g., pound=u'£' or u'£').
    FILE
    c:\code\formats.py
'''
