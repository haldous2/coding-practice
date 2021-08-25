"""
Given two arrays of integers, 
  find a pair of values (one value from each array) that you
  can swap to give the two arrays the same sum.
"""
def sum_swap_v1(arra, arrb):
    """
    Version 1:
        Using min values from heap 
    Note: heapify -> heapq.heapify .. depending on how imported
    Overall time with heap - O(nlogn); could also just be sorted
    """
    if not arra or not arrb:
        return None

    # Sum of array
    arra_sum = sum(arra)
    arrb_sum = sum(arrb)

    # Create min heaps, find min values
    # O(nlogn) time, O(n) space
    arra_heap = [val for val in arra]  # copy
    heapify(arra_heap)
    arrb_heap = [val for val in arrb]  # copy
    heapify(arrb_heap)

    # Min values
    # O(1) time
    arra_min = heappop(arra_heap)
    arrb_min = heappop(arrb_heap)

    # Test values
    arra_test = arra_sum - arra_min + arrb_min
    arrb_test = arrb_sum - arrb_min + arra_min

    # print arra_test, arrb_test

    # O(A+B) where A, B are lengths of corresponding arrays
    while arra_heap and arrb_heap:

        if arra_test == arrb_test:
            return (arra_min, arrb_min)

        # Balance out sums by taking next min from larger sum. 
        #   The next min should be larger than previous min
        #   which will make smaller sum larger, and larger sum smaller
        if arra_test > arrb_test:
            arra_min = heappop(arra_heap)
        else:
            arrb_min = heappop(arrb_heap)

        arra_test = arra_sum - arra_min + arrb_min
        arrb_test = arrb_sum - arrb_min + arra_min

        # print arra_test, arrb_test

    if arra_test == arrb_test:
        return (arra_min, arrb_min)
    return None

def sum_swap_v2(arra, arrb):
    """
    Version 2:
      Using a hash table and target
      Using formula suma - vala + valb = sumb - valb + vala
        suma - sumb / 2 = target - must be integer, otherwise return None
        and: vala - valb = target -> target + valb = vala
        Hash vala(s), find target + valb to match
    O(A+B) where A, B are lengths of arrays A, B
    """
    arra_sum = sum(arra)
    arrb_sum = sum(arrb)
    arra_set = set()

    def load_arra_set(arra):
        for val in arra:
            arra_set.add(val)

    def get_target(arra_sum, arrb_sum):
        if (arra_sum - arrb_sum) % 2 != 0:
            return None
        return (arra_sum - arrb_sum) / 2

    def find_swap_values(arrb, target):
        for val in arrb:
            if (target + val) in arra_set:
                return (target + val, val)
        return None

    def sum_swap(arra, arrb):
        load_arra_set(arra)
        target = get_target(arra_sum, arrb_sum)
        if target is not None:
            result = find_swap_values(arrb, target)
            return result
        else:
            return None

    return sum_swap(arra, arrb)

arra = [4, 1, 2, 1, 1, 2]   # (1,3)
arrb = [3, 6, 3, 3]

arra = [1,2,3,4]            # (1,3)
arrb = [1,3,4,6]

# arra = [1,2,3,4]            # None
# arrb = [5,5,5,5]

arra = []                   # None
arrb = []

arra = [1]                  # (1,1)
arrb = [1]

print "v1:", sum_swap_v1(arra, arrb)
print "v2:", sum_swap_v2(arra, arrb)
