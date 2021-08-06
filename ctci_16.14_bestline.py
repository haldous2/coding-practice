"""
a.k.a. LeetCode (max points on a line #149)
Given two dimensional points, find a line which passes the most number of points

Initial thoughts: 
The question is confusing as to what to look for. If you look at the solution 
in the Cracking the Coding Interview book, you'll see that "passes" means to
pass through each point. You create a line from a point to another point, 
then figure out which line was repeated for other points.

Initially, I thought passes meant "passed by, got as close to every point possible".
If doing the latter, a linear regression is the way to go.
  formula summation((x - x mid)(y - y mid)) / summation((x - x mid)^2)
  to find mid x, mid y - add all x values, take avg, add all y values, take avg

I think the point of this problem is to undestand errors that can occur
with floating point numbers.

Assumptions: 
graph has no duplicates
cannot assume that points are all integers (cannot use gcd in this case)
No line exists unless there are at least two points
"""
## Testing round to 8 places - epsilon 00000001
#  reason to use epsilon to check .00000001 forward and backward
#  Note: could also create floor with epsilon, rounding does the same thing
# print round(1.999999999, 8)  # output: 2.0
# print round(1.999999990, 8)  # output: 1.99999999

# moral of the story - floating point numbers are not predictable or precise.
# ways to mitigate the issue:
# 1. Floor a value with epsilon or rounding
# 2. Check an epsilon value +/- away to see if same(ish) value

epsilon = .00000001  # since we are rounding by 8 decimal places

def getLines(graph):

   lines = {}
   maxhops = 0
   maxline = None

   if len(graph) <= 1:
       ## per assumptions - cannot return line unless at least two lines
       #  return -1 because adding one to hops for display
       return -1

   for i in range(len(graph)):
       for j in range(i + 1, len(graph)):

           # one point to every other point - O(n^2) time
           slope = getSlope(graph[i], graph[j], lines)
           yintercept = getYIntercept(graph[i], slope, lines)
           # print graph[i], graph[j], "slope:", slope, "yintercept:", yintercept

           # store hash - lines[(my, mx)] = {yintercept:count}
           if slope in lines:
               if yintercept in lines[slope]:
                   # Count point only once from current point
                   if lines[slope][yintercept][0] != graph[i]:
                       lines[slope][yintercept][1] += 1
                       lines[slope][yintercept][0] = graph[i]
               else:
                   # Count calling point
                   lines[slope][yintercept] = [graph[i], 1]
           else:
               # Count calling point
               lines[slope] = {yintercept:[graph[i], 1]}

           if maxhops < lines[slope][yintercept]:
               maxhops = lines[slope][yintercept][1]
               maxline = getLine(slope, yintercept)

   # debug
   # printLines(lines)
   # print "maxhops:", maxhops
   return maxline

def getLine(slope, yintercept):
   """
   Build string representation of line using slope and yintercept
   """
   if slope == 0:
       return "y = " + str(yintercept)
   elif slope == "inf":
       # yintercept is actually xintercept
       return "x = " + str(yintercept)
   else:
       return "y = " + str(slope) + "x + " + str(yintercept)

def getSlope(p1, p2, lines):
   slope = calculateSlope(p1, p2)
   # need to check an epsilon away in each direction
   # e.g., rounding to 8 decimals
   #   1.999999990 = 1.99999999
   #   1.999999999 = 2.0
   # most likely the same number, so look +/- epsilon away
   if slope != "inf" and slope != 0:
       next_slope = slope + epsilon
       prev_slope = slope - epsilon
       if next_slope in lines:
           return next_slope
       elif prev_slope in lines:
           return prev_slope
   return slope

def calculateSlope(p1, p2):
   """
   With two point, calculate
     return slope as (my, mx)
   """
   x1 = p1[0]
   y1 = p1[1]
   x2 = p2[0]
   y2 = p2[1]
   my = y2 - y1
   mx = x2 - x1

   # Calculated slope my / mx
   if my == 0:
       return 0
   elif mx == 0:
       return "inf"
   else:
       return round((float(my) / float(mx)), 8)

def getYIntercept(point, slope, lines):
   """
   With slope and lines, return yintercept
   """
   yintercept = calculateYIntercept(point, slope)
   # need to check an epsilon away in each direction
   # e.g., rounding to 8 decimals
   #   1.999999990 = 1.99999999
   #   1.999999999 = 2.0
   # most likely the same number, so look +/- epsilon away
   next_yintercept = yintercept + epsilon
   prev_yintercept = yintercept - epsilon
   if slope in lines:
       if next_yintercept in lines[slope]:
           return next_yintercept
       elif prev_yintercept in lines[slope]:
           return prev_yintercept
   return yintercept

def calculateYIntercept(point, slope):
   """
   With a point(x, y) and a slope(my, mx)
     return y intercept as float
   """
   x1 = point[0]
   y1 = point[1]

   ## Using calculated slope my/mx
   if slope == 0:
       # horizontal line
       return y1
   elif slope == "inf":
       # vertical line
       return x1
   else:
       # regular line with y intercept
       # y - y1 = m(x - x1)
       # y = m(x - x1) + y1
       # for y intercept, set x to zero
       # y = -mx1 + y1
       y = ((slope * float(x1)) * -1) + float(y1)
       return round(y, 8)

def printLines(lines):
   for slope, intercepts in lines.items():
       print "slope:", slope
       for intercept, linedata in intercepts.items():
           if slope == "inf":
               print "   x-int:", intercept, "count:", linedata[1]
           else:
               print "   y-int:", intercept, "count:", linedata[1]

## Test Graphs
graph = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# graph = [[3,2],[4,1],[2,3],[1,4]]
# graph = [[3,2]]

## Initalize counter
maxline = getLines(graph)

## Max Line
print "max line:", maxline
