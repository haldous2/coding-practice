"""
You have an integer matrix representing a plot of land, 
  where the value at that location represents the height above sea level. 
A value of zero indicates water. 
A pond is a region of water connected vertically, horizontally, or diagonally. 
The size of the pond is the total number of connected water cells.
Write a method to compute the sizes of all ponds in the matrix
"""
def find_ponds(g = []):
    """
    Find the number of connected ponds and their sizes
    Runtime O(w*h) where w is width, h is height
    """
    if len(g) == 0:
        return []
    if len(g[0]) == 0:
        return []
    def traverse_ponds():
        """
        Traverse ponds, track each in queue and count number connected
        """
        visited = {}
        queue = deque()

        for row in range(len(g)):
            for col in range(len(g[row])):
                if (col, row) not in visited and g[row][col] == 0:
                    visited[(col, row)] = 1
                    # print "===== NEW exploring from:", (col, row)
                    queue.extend(explore_ponds((col, row)))
                    while queue:
                        water = queue.pop()
                        if water not in visited:
                            visited[water] = (col, row)
                            visited[(col, row)] += 1
                            # print "===== STILL exploring from:", water
                            queue.extend(explore_ponds(water))

        ponds = []
        for key, val in visited.items():
            if type(val) is int:
                ponds.append(val)
        return ponds

    def explore_ponds(point):
        """
        Explore out one square from point
        Note: square if flipped - direction of y up goes to zero
        Note: pass back list of tuples -> [(0,0), (1,2), (col, row)] etc...
        Note: could also write this as a loop
        Overall runtime for this method is constant O(1)
        """
        water_found = []
        col = point[0]
        row = point[1] 
        # print "col(x):", col, "row(y):", row, "value:", g[row][col]

        def explore_connect_pond(dir_col, dir_row):
            # check bounds of square
            if dir_col >= 0 and dir_row >= 0 and dir_col < len(g[0]) and dir_row < len(g):
                # check if pond
                if g[dir_row][dir_col] == 0:
                    # add pond to queue
                    water_found.append((dir_col, dir_row))
        # up
        dir_col = col
        dir_row = row - 1  # up is down
        explore_connect_pond(dir_col, dir_row)
        # print "up:", dir_col, dir_row
        # down
        dir_col = col
        dir_row = row + 1  # down is up
        explore_connect_pond(dir_col, dir_row)
        # print "down:", dir_col, dir_row

        # left
        dir_col = col - 1
        dir_row = row
        explore_connect_pond(dir_col, dir_row)
        # print "left:", dir_col, dir_row
        # right
        dir_col = col + 1
        dir_row = row
        explore_connect_pond(dir_col, dir_row)
        # print "right:", dir_col, dir_row

        # left up diag
        dir_col = col - 1
        dir_row = row - 1
        explore_connect_pond(dir_col, dir_row)
        # print "up left:", dir_col, dir_row
        # right up diag
        dir_col = col + 1
        dir_row = row - 1
        explore_connect_pond(dir_col, dir_row)
        # print "up right:", dir_col, dir_row

        # left down diag
        dir_col = col - 1
        dir_row = row + 1
        explore_connect_pond(dir_col, dir_row)
        # print "down left:", dir_col, dir_row
        # right down diag
        dir_col = col + 1
        dir_row = row + 1
        explore_connect_pond(dir_col, dir_row)
        # print "down right:", dir_col, dir_row

        # print "water found:", water_found
        return [p for p in water_found]

    return traverse_ponds()

g = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]  ## 2,4,1     passed
g = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]]  ## 1,1,1,1   passed
g = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]  ## None      passed
g = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  ## 16        passed
print find_ponds(g)
