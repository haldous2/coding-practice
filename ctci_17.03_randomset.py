"""
Randomly generate a set of m integers from an array of size n.
Each element must have equal probability of being chosen.

Given an array of values, randomly choose n values
Not sure about duplciates
"""
def generatesetV1build(arr, sub):
    """
    naive version
       select random from input array
       swap random select to end
       shrink size of the random selection

    Running tests appears to show this is an unbiased approach
       similar to shuffle; however, not running through all of array elements. 
    Honestly, I'm not sure how to tell if this is biased or not.
       Because it is not able to randomly choose those already selected, 
       there should not be any bias - which is exactly how shuffle works
    """
    ret = sub[:]    # copy of sub / fresh start
    for i in range(len(sub)):
        rndidx = random.randint(0, len(arr) - 1 - i)
        ret[i] = arr[rndidx]
        # swap value to end
        # print "swap indexes", rndidx, "and", (len(arr) - 1 - i), "rndrange: 0 to", (len(arr) - 1 - i)
        arr[len(arr) - 1 - i], arr[rndidx] = arr[rndidx], arr[len(arr) - 1 - i]
    return ret
    print "lo:", lo, "hi:", hi, "diff:", hi - lo

def generatesetV1():
    arr = [1,2,3,4,5,6,7,8,9,0]
    sub = [None, None, None]      # select 3 in 10
    trk = {}
    # print sub
    for i in range(1000000):
        newsub = sorted(generatesetV1build(arr, sub))
        if tuple(newsub) in trk:
            trk[(tuple(newsub))] += 1
        else:
            trk[(tuple(newsub))] = 1
    lo = sys.maxint
    hi = 0
    for item, count in trk.items():
        lo = min(lo, count)
        hi = max(hi, count)
        print item, count
    print "lo:", lo, "hi:", hi, "diff:", hi - lo

generatesetV1()

def generatesetV2build(arr, sub):
    """
    book version - unbiased and fair
    """
    n = len(arr)
    m = len(sub)
    ret = arr[0:m]
    # prefill ret
    # random indexes
    for i in range(m, n):   # from m to (n - 1)
        k = random.randint(0, i)
        if k < m:   # e.g. length of sub is 3, m=3 need index 0,1,2 - k < m
            ret[k] = arr[i]
    return ret

def generatesetV2():
    arr = [1,2,3,4,5,6,7,8,9,0]
    sub = [None, None, None]      # select 3 in 10
    trk = {}
    # print sub
    for i in range(1000000):
        newsub = sorted(generatesetV2build(arr, sub))
        if tuple(newsub) in trk:
            trk[(tuple(newsub))] += 1
        else:
            trk[(tuple(newsub))] = 1
    lo = sys.maxint
    hi = 0
    for item, count in trk.items():
        lo = min(lo, count)
        hi = max(hi, count)
        print item, count
    print "lo:", lo, "hi:", hi, "diff:", hi - lo

generatesetV2()
