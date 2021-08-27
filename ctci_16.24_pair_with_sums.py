"""
Design an algorithm to find ALL pairs of integers within an array 
which sum to a specified value.

Assumptions:
array of integers
input array, predefined sum
numbers can be positive or negative
might have to deal with values larger than int (e.g. max + max = larger than max)
  however, python doesn't have these limitations
  Should I assume that predefined sum is less or equal to max int?
there might be duplicates
"""            
def find_pair_with_sumV1(arr, sum):
   """
   Brute Force
   iterate through all combinations in array
   Keep track of pairs available to avoid duplicates
   O(n^2) time, O(n) space
   """
   pairs = []
   pairs_avail = {}
   # Load pairs_avail duplicate tracker
   for num in arr:
       if num in pairs_avail:
           pairs_avail[num] += 1
       else:
           pairs_avail[num] = 1
   # Find matching pairs
   for i in range(len(arr)):
       if pairs_avail[arr[i]] > 0:
           for j in range(len(arr)):
               if pairs_avail[arr[j]] > 0 and arr[i] + arr[j] == sum:
                   pairs.append((arr[i], arr[j]))
                   pairs_avail[arr[i]] -= 1
                   pairs_avail[arr[j]] -= 1
   return pairs

def find_pair_with_sumV2(arr, sum):
   """
   Track seen in set - look for (sum - current) in set
   pairs need to be unique; track pairs in hash
   O(n) time, O(n) extra space
   """
   pairs = []
   pairs_available = {}  # pairs_available[num] = number of pairs available
   for num in arr:
       # Look for available complement
       # if (sum - num) in pairs_available and pairs_available[(sum - num)] > 0:
       if pairs_available.get((sum - num), 0) > 0:
           # complement is available
           pairs_available[(sum - num)] -= 1
           pairs.append((sum - num, num))
           if num not in pairs_available:
               # just used this num, start at zero
               pairs_available[num] = 0
       else:
           # Track unused nums
           if num in pairs_available:
               pairs_available[num] += 1
           else:
               pairs_available[num] = 1
   return pairs

def find_pair_with_sumV3(arr, sum):
   """
   Same as V2, with preloading of pairs_available
   still O(n) time
   """
   pairs = []
   pairs_available = {}  # pairs_available[num] = number of pairs available
   # Load pairs_avail duplicate tracker
   for num in arr:
       if num in pairs_available:
           pairs_available[num] += 1
       else:
           pairs_available[num] = 1
   # Find matching pairs
   for num in arr:
       # Look for available complement
       if (sum - num) in pairs_available and pairs_available[(sum - num)] > 0:
           # complement is available
           pairs_available[(sum - num)] -= 1
           pairs_available[num] -= 1
           pairs.append((sum - num, num))
   return pairs

def find_pair_with_sumV4(arr, sum):
   """
   Sort array, track inwards - should handle duplicates automatically
   O(nlogn) time, O(1) space
   """
   arr = sorted(arr)
   pairs = []
   i = 0
   j = len(arr) - 1
   while i < j:
       result = arr[i] + arr[j]
       if result == sum:
           pairs.append((arr[i], arr[j]))
           i += 1
           j -= 1
       elif result < sum:
           i += 1
       else:
           j -= 1
   return pairs

arr = [1,3,5,2,4,6,9,7]
sum = 9
print "v1:",find_pair_with_sumV1(arr, sum)
print "v2:",find_pair_with_sumV2(arr, sum)
print "v3:",find_pair_with_sumV3(arr, sum)
print "v4:",find_pair_with_sumV4(arr, sum)
