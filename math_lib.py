
def list_mean(L):
    
    """
    Compute the arithmetic mean of an array
    Parameters
    ----------
    L : list of int or float
        Non-empty array containing values of which to compute mean

    Returns
    --------
    mn
        The arithmetic mean of array L
    """

    if len(L) < 1:
        raise ValueError("Can't give the mean of zero values!")
    elif L is None:
        raise ValueError("Can't give the mean of None!")

    good_vals = []
    bad_vals = []

    for i in L:
        try:
            k = int(i) # a temp variable, checks if i is float or int
            good_vals.append(i)
        except ValueError:
            bad_vals.append(i)
            continue

    if len(bad_vals) > 0:
        print("These values are non-numerical and excluded from mean")
        print(bad_vals)

    mn = sum(good_vals)/len(good_vals)
    return mn

def list_stdev(L):
    """
    The standard deviation of a list of values
    Parameters
    -----------
    L : list of int or float
        Non-empty array containing values of which to compute stdev

    Returns
    --------
    st
        Standard deviation of the values in L

    """

    if len(L) < 1:
        raise ValueError("Can't give the stdev of zero values!")
    elif len(L) < 2:
        raise ValueError("Need more than two data for stdev!")
    elif L is None:
        raise ValueError("Can't give the mean of None!")

    good_vals = []
    bad_vals = []

    for i in L:
        try:
            k = int(i) # a temp variable, checks if i is float or int
            good_vals.append(i)
        except ValueError:
            bad_vals.append(i)
            continue

    if len(bad_vals) > 0:
        print("These values are non-numerical and excluded from stdev")
        print(bad_vals)

    st = math.sqrt(sum([(mean(good_vals)-x)**2 for x in good_vals]) /
                    len(good_vals))
    return st

