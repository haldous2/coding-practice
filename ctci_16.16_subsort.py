"""
Given an array of integers, write a method to find indices m and n such that 
if you sorted elements m through n ,the entire array would be sorted. 
Minimize n - m (that is, find the smallest such sequence).

Assume: integers
"""

def subsort(arr):

    def find_unsorted_edges():
        """
         Discover edges where sorted array is out of sequence
         Returns left and right edge where out of order
                 or -1, -1 if no edges found
        """
        i = 0
        j = len(arr) - 1
        left_edge = -1
        right_edge = -1
        # looking 1 forward and 1 back
        # so while loop needs to stop 1 before ends of array
        while (i < len(arr) - 1 or j > 0) and i <= j:
            if arr[i] > arr[i + 1]:
                left_edge = i + 1
            else:
                i += 1
            if arr[j] < arr[j - 1]:
                right_edge = j - 1
            else:
                j -= 1
            if left_edge > -1 and right_edge > -1:
                break
        return (left_edge, right_edge)

    def find_middle_min_max(left_edge, right_edge):
        """
        Find min and max of unsorted section of array
        Note: left_edge, right_edge must be > -1
        """
        minval = -1
        maxval = -1
        if left_edge > -1 and right_edge > -1:
            minval = arr[left_edge]
            maxval = arr[right_edge]
            for i in range(left_edge, right_edge + 1):
                minval = min(minval, arr[i])
                maxval = max(maxval, arr[i])
        return (minval, maxval)

    def find_insert_min_max(left_edge, right_edge, minval, maxval):
        """
        From left and right edges, 
        find min and max edges going towards middle
        """
        left_edge_min = -1
        right_edge_max = -1
        if left_edge > -1 and right_edge > -1 and minval > -1 and maxval > -1:
            i = 0
            j = len(arr) - 1
            while (i <= left_edge):
                if arr[i] >= minval:
                    left_edge_min = i
                    break
                i += 1
            while (j >= right_edge):
                if arr[j] <= maxval:
                    right_edge_max = j
                    break
                j -= 1
        return (left_edge_min, right_edge_max)

    if len(arr) <= 1:
        return (-1, -1)  # not possible to sort

    left_edge, right_edge = find_unsorted_edges()
    minval, maxval = find_middle_min_max(left_edge, right_edge)
    left_edge_min, right_edge_max = find_insert_min_max(left_edge, right_edge, minval, maxval)
    print "edges:", left_edge, right_edge, "min/max:", minval, maxval, "min/max edges:", left_edge_min, right_edge_max
    if left_edge_min > -1 and right_edge_max > -1:
        return (left_edge_min, right_edge_max)
    else:
        return (-1, -1)

## Tests
# arr = []                                      ## lo,hi -> -1,-1
# arr = [1]                                     ## lo,hi -> -1,-1
# arr = [1,2,3,4,5,6,7,8,9]                     ## lo,hi -> -1,-1

arr = [1,2,4, 7,10,11,7,12,6,7, 16,18,19]     ## lo,hi -> 3,9
# arr = [1,2,3, 5,6,4, 7,8,9]                   ## lo,hi -> 3,5
# arr = [1,2,3,4,5,6,7, 9,8]                    ## lo,hi -> 7,8
# arr = [2,1 ,3,4,5,6,7,8,9]                    ## lo,hi -> 0,1
# arr = [1,3,2,4,5,6,7,8,9]                     ## lo,hi -> 1,2
# arr = [2, 1]                                  ## lo,hi -> 0,1
# arr = [1,2, 7,6,3,5, 7,8]                     ## lo,hi -> 2,5
print subsort(arr)
