"""
Method to add two numbers without +, or any other operator

Initial thoughts - bit wise?
Will have to create manual addition of bits      

Assumptions: integers only - might modify version 2 for floats?
"""
def add(a, b):
    """
    Addition breaks when adding and subracting same value 
       e.g. (2 + -2)
       It looks like the carry grows exponentially 
       because there isn't anything to carry. 
       same issue with subtraction below
       The only fix I can think of is to check if numbers are 
       equal and opposite before adding them
    """
    i = 0
    while b != 0:
        if i == 5:
            break
        i += 1
        r = a ^ b           # result
        c = (a & b) << 1    # carry
        print a, b, r, c
        a = r
        b = c
    print "=== result", a
    return a

add(2, 3)
add(12, 5)
add(3, -3)    # crash

# def subtract(a, b):
#     return add(a, b * -1)

def subtract(a, b):
    """
    Subtraction breaks if denom is larger than numerator
    Way to solve: 
       1. swap denominator and numerator, flip sign
       2. add to negative number - add(a, -b)
    """            
    i = 0
    while b != 0:
        if i == 10:
            break
        i += 1
        c = ((~a) & b) << 1     # borrow
        a = a ^ b               # add without borrow
        b = c
        print a, b, c
    print "=== result", a

subtract(2, 5)
subtract(5, 2)  # crash
subtract(2, 2)
