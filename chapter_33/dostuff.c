doStuff() 
{                                           # C Program
    if (doFirstThing() == ERROR)            # Detect errors everywhere
        return ERROR;                       # even if not handled here 
    if (doNextThing() == ERROR)
        return ERROR;
    ...
    return doLastThing();
}

main() 
{
    if (doStuff() == ERROR)
        badEnding();
    else 
        goodEnding();
}


// In fact, realistic C programs often have as much code devoted to error detection as to
// doing actual work. But in Python, you don’t have to be so methodical (and neurotic!).
