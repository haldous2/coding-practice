"""
Book version - reading only able to read jth bit
Reading from 0 to n
Also, I think the assumption that the order is ascending
   e.g. 0,1,2,3 etc.
Method: read first bit (jth) start from least sig bit
           if no more bits - done. stored number will be answer
           if less zeros than ones - drop ones - add zero to number
           if less ones than zeros - drop zeros - add one to number
           if resulting number is larger than n, return None - none missing

Note: this code amazes me: prety cool, pretty, pretty cool stuff.
"""

def readjth(bnum, jth):
    """
    Read jth bit - return True if set, False if not
    """
    return ((bnum >> jth) & 1) > 0

def findmissingint():

    # bits 0 to 8 - n = 8 - test missing 3
    bits = [0b0000, 0b0001, 0b0010, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000]
    n = 8
    col = 0
    num = 0

    while bits:

        zeros = []
        ones = []

        for bnum in bits:
            if readjth(bnum, col):
                ones.append(bnum)
            else:
                zeros.append(bnum)

        if len(zeros) <= len(ones):
            bits = zeros
            num |= 0 << col
        else:
            bits = ones
            num |= 1 << col

        # print bits, num

        col += 1

    if num > n:
        return None
    else:
        return num

print "missing:", findmissingint()

findmissingV1()

def findmissingV2():
"""
Bit version - if we could read the bits
Using pseudo bits - each int is 8 bits long with max 256
Also, for the formula n(n+1)/2 - number should start at 1, not at 0
   otherwise n will be off by one
O(n) time
"""
def insertint(val, idx, bits, n):
    # mask - 0000 1111 0000 where 1111 is the part to clear
    mask = ((2**(8 * n)) - 1)
    mask ^= (255 << (8 * idx))
    # clear bits for insertion
    #     bits 1010 1010 1010
    #   ^ mask 0000 1111 0000
    bits &= mask # clear bits for insertion (for reuse)
    bits |= val << (8 * idx)
    return bits

def readint(idx, bits):
    bits = bits >> (8 * idx)
    mask = 255
    return bits & mask

def findmissingint():

    n = 10
    sum = 0

    bits = 0
    bits = insertint(1,0,bits,n)
    bits = insertint(2,1,bits,n)
    bits = insertint(3,2,bits,n)
    bits = insertint(4,3,bits,n)
    bits = insertint(5,4,bits,n)
    bits = insertint(6,5,bits,n)
    # bits = insertint(7,6,bits,n)
    bits = insertint(8,7,bits,n)
    bits = insertint(9,8,bits,n)
    bits = insertint(10,9,bits,n)
    # print "bits:", bits, bin(bits)

    for i in range(n):
        nxtint = readint(i, bits)
        # print "nxtint:", nxtint
        sum += nxtint
    # sum of sequence (n(n+1))/2
    return ((n * (n + 1)) / 2) - sum

print "missing:", findmissingint()

# findmissingV2()
