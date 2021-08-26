"""
Implement a method rand7() given rand5().
That is, 
given a method that generates a random number between O and 4 (inclusive), 
write a method that generates a random number between O and 6 (inclusive).
"""
def rand5():
    return random.randint(0,4)

## Version 1
def rand7V1():
    """
    Brute force, 
    Call (Rand5() x 2) until value between 0 & 6
    Note: appears to favor higher numbers
          zero doesn't get called as often
    """
    result = -1
    while result < 0 or result > 6:
        resulta = rand5()
        resultb = rand5()
        result = resulta + resultb
    return result

# Version 2
def rand7V2():
    """
    Calling Rand5() exactly twice
    Using a formula to calculate rand7 value
    where x is rand5 val
       (x * 2) - (x / 2); this works for vals 6,5,3,2,0
    for values 4 and 1, when a is odd, will need to check
       second rand5 value. if even, add one to subtractor
       e.g.
       odd a:  (x * 2) - (x / 2)
       even a: (x * 2) - (x / 2 + 1)
    Note: results are more evenly spread, though 6 seems to
          be hit a lot more often
          This version should be faster as second rand5 called
          only when first rand5 is odd (which is twice in 0 to 4)
    """
    result = -1
    resulta = rand5()
    if resulta % 2 == 0:        # a is even
        resultb = 0
    else:                       # a is odd
        if rand5() % 2 == 0:    # b is even
            resultb = 0
        else:
            resultb = 1
    return (resulta * 2) - ((resulta / 2) + resultb)

# Version 3 (No bias - best version)
def rand7V3():
    """
    Using a multidimensional array
    Generate two variables, x & y - that will sync up with grid
       where x & y = 0, 1, 2, 3, 4

    Note: Although there are duplicates, they are evenly distributed
          so this works. Similar to V4 (below)
    """
    g = [[0,1,2,3,4],
         [5,6,0,1,2],
         [3,4,5,6,0],
         [1,2,3,4,5],
         [6,-1,-1,-1,-1]]
    result = -1
    while result == -1:
        result = g[rand5()][rand5()]
    return result

# Version 4 (No bias - best version)
def rand7V4():
    """
    Adding 5 * rand5() + rand5()
      Produces an even distribution of numbers without duplicates
      Similar to V3 (above)
      0  + (0 to 4);  0 to 4   % 7: 0,1,2,3,4
      5  + (0 to 4);  5 to 9   % 7: 5,6,0,1,2
      10 + (0 to 4); 10 to 14  % 7: 3,4,5,6,0
      15 + (0 to 4); 15 to 19  % 7: 1,2,3,4,5
      20 + (0 to 4); 20 to 24  % 7: 6,X,X,X,X

    Note: this is different than adding rand5() + rand5()
      because there will not be duplicate (biased) results
      e.g. 1 + 1 = 2, and also 0 + 2 = 2 etc. more 2's than 
      zeros and other numbers.
    """
    while True:
        result = 5 * rand5() + rand5()  # note pemdas - 5 * rand5 calculated first
        if result < 21:
            return result % 7 

## Test Rand5
ints5 = {}
n = 1
for i in range(n):
    int5 = rand5()
    if int5 in ints5:
        ints5[int5] += 1
    else:
        ints5[int5] = 1
print "=== rand5() ==="
print "frequency should be around", 1.0 / 5
for number, frequency in ints5.items():
    print number, "frequency:", (frequency * 1.0) / n

## Test Rand7
ints7 = {}
n = 10000
for i in range(n):
    int7 = rand7V4()
    if int7 in ints7:
        ints7[int7] += 1
    else:
        ints7[int7] = 1
print "=== rand7() ==="
print "frequency should be around", 1.0 / 7
for number, frequency in ints7.items():
    print number, "frequency:", (frequency * 1.0) / n
