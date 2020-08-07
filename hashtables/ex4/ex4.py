def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Locate the pairs of positives

    cache = dict()
    result = []

    for each in a:
        if each not in cache:

            # returns a positive of the value if negative
            cache[each] = each*-1

            if cache[each] in cache and each != 0:
                result.append(abs(cache[each]))

    return result


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
