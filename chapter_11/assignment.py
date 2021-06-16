spam = 'Spam'                                               # Basic form
spam, ham = 'yum', 'YUM'                                    # Tuple assignment (positional)
[spam, ham] = ['yum', 'YUM']                                # List assignment (positional)
a, b, c, d = 'spam'                                         # Sequence assignment, generalized
a, *b = 'spam'                                              # Extended sequence unpacking (Python 3.X)
spam = ham = 'lunch'                                        # Multiple-target assignment
spam += 42                                                  # Augmented assignment (equivalent to spams = spams + 42)
