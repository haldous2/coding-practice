"""
Method to add two numbers without +, or any other operator

Initial thoughts - bit wise?
Will have to create manual addition of bits      

Assumptions: integers only - might modify version 2 for floats?
"""
def int_overflow(val):
    """
    Overflow handler
    Because python doesn't have internal types, this method will
    emulate strongly typed integer overflow
    e.g., if min is -6 and max is 5
       val: -3, -2, -1, 0, 1, 2, 3, 4, 5,  6,  7,  8
       ret: -3, -2, -1, 0, 1, 2, 3, 4, 5, -6, -5, -4 ... (repeats)
    """
    if not -sys.maxint-1 <= val <= sys.maxint:
        val = (val + (sys.maxint + 1)) % (2 * (sys.maxint + 1)) - (sys.maxint + 1)
    return val

def addbin(a, b):
    """
    Add binary a and b
    It looks like the carry grows exponentially 
       because there isn't anything to carry.
    Fix: because python doesn't have strong type, integers tend to 
         meander off into infinity. The fix is to implement a manual
         overflow method that cuts values off as though they were 32 bit ints
    """
    while b != 0:
        r = a ^ b               # add without carry
        c = (a & b) << 1        # carry
        a = int_overflow(r)
        b = int_overflow(c)
    return a

def add(a, b):
    print "result add", a, "and", b, "=", addbin(a, b)

add(2, 3)       # 5
add(15, 9)      # 24
add(2, -1)      # 1
add(2, -2)      # 0
add(2, -10)     # -8

# def subtract(a, b):
#     return add(a, b * -1)

def subtractbin(a, b):
    """
    Subtract binary b from a
    It looks like the borrow grows exponentially 
       because there isn't anything to borrow.
    Fix: because python doesn't have strong type, integers tend to 
         meander off into infinity. The fix is to implement a manual
         overflow method that cuts values off as though they were 32 bit ints
    """            
    while b != 0:
        r = a ^ b               # add without borrow
        c = ((~a) & b) << 1     # borrow
        a = int_overflow(r)
        b = int_overflow(c)
    return a

def subtract(a, b):
    print "result subtract", b, "from", a, "=", subtractbin(a, b)

subtract(2, 5)      # -3
subtract(5, 2)      # 3
subtract(2, 2)      # 0
