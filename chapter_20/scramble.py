def scramble(seq):
    for i in range(len(seq)):                                   # Generator function
        yield seq[i:] + seq[:i]