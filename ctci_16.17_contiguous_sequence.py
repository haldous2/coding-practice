"""
You are given an array of integers (both positive and negative). 
Find the contiguous sequence with the largest sum. Return the sum.

The book version doesn't address returning contiguous sequence, and 
only returns the sum. It also doesn't address how to handle arrays
that are one or smaller. 
I think the point of this problem is to talk with the interviewer
about: what to do if the sum is less than zero, or is zero. What
       exactly is the largest sum? In this case, if negative, return
       zero as no sum, otherwise the max sum
"""
## Version 1
#  issues with this version
#    if there are duplicate numbers (3 & 3 for example) on the ends
#    an issue will arise where the sum may not be maximized as
#    values that are lesser or equal are removed from the left side first
def sum_all(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def max_range(arr, sum_max):
    sum_new = sum_max
    left_index = 0
    right_index = len(arr) - 1
    left_index_max = left_index
    right_index_max = right_index
    while left_index <= right_index:
        # Recalculate sums
        if arr[left_index] <= arr[right_index]:
            sum_new -= arr[left_index]
            left_index += 1
        else:
            sum_new -= arr[right_index]
            right_index -= 1
        # Reset max sum if applicale
        if sum_max < sum_new:
            sum_max = sum_new
            left_index_max = left_index
            right_index_max = right_index
    return (sum_max, left_index_max, right_index_max)

def max_sequence(arr):
    if len(arr) == 0:
        return (0, -1, -1)
    if len(arr) == 1:
        return (0, 0, 0)
    sum_max = sum_all(arr)
    return max_range(arr, sum_max)

# arr = []                        ## 0 (-1, -1)
# arr = [3]                       ## 0 (-1, -1)
arr = [-2, -8, 3, -2, 4, -10]   ## 5 (2, 4)
# arr = [-1, -2, -3]              ## 0 (-1, -1)
# sum_max, lo_index_max, hi_index_max = max_sequence_v2(arr)
# print "sum:", sum_max, "@", (lo_index_max, hi_index_max)

## Version 2
#  Book - add to sum until negative, track indexes, when next element is
#         positive start adding to sum again
#  Note: is no sum return 0 - even if negative. Confirm with interviewer
#  Note: this version returns the indexes since the question asks for the
#        sequence with the largest sum
def sum_all_v2(arr):

    sum = 0
    sum_max = 0
    lo_index = -1
    lo_index_max = -1
    hi_index_max = -1

    for i in range(len(arr)):

        sum += arr[i]

        # Track sum and indexes
        if sum >= 0:
            # Indexes
            if lo_index < 0:
                lo_index = i
            # Max sum, indexes
            if sum_max < sum:
                sum_max = sum
                lo_index_max = lo_index
                hi_index_max = i
        else:
            # Reset sum and lo index
            sum = 0
            lo_index = -1

    return (sum_max, lo_index_max, hi_index_max)

def max_sequence_v2(arr):
    if len(arr) == 0:
        return (0, -1, -1)
    if len(arr) == 1:
        return (0, 0, 0)
    return sum_all_v2(arr)

# arr = []                        ## 0 (-1, -1)
# arr = [3]                       ## 0 (-1, -1)
arr = [-2, -8, 3, -2, 4, -10]   ## 5 (2, 4)
# arr = [-1, -2, -3]              ## 0 (-1, -1)
sum_max, lo_index_max, hi_index_max = max_sequence_v2(arr)
print "sum:", sum_max, "@", (lo_index_max, hi_index_max)
