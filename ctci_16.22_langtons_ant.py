"""
An ant is sitting on an infinite grid of white and black squares. 
It initially faces right.
At each step, it does the following:
  (1) At a white square, 
      flip the color of the square, 
      turn 90 degrees right (clockwise), and move forward one unit.
  (2) At a black square, 
      flip the color of the square, 
      turn 90 degrees left (counter-clockwise), and move forward one unit.

Question: which square does the ant start on? 
          Only input is k moves, therefore - programmers selection of
          the start square?
Answer:   For this program, ant starts on white square
          first move will flip a black square.
Queston: Is this board a checker board, or all white board? The instructions
         say board with white and black squares - so I'm assuming a checker board
Answer:  I've implemented both, commenting out code in get_point_original_color
         will switch the boards

For fun, run the program k = 10,500 with an all white board 
"""
def print_k_moves(k):

    # points[(x, y)] = BL, WH <- current color
    points = {}
    minmax = [None, None, None, None]  # min_x, max_x, min_y, max_y

    def ant_moves(ant, k):
        # test_get_point_original_color()
        for move in range(k):
            # Track
            track_point(ant.location)
            # prev_location = ant.location
            # Move
            ant.direction, ant.location = ant_move_next(ant.direction, ant.location)
            # print "moving from:", prev_location, "to:", ant.location, ant.direction
            # print "-----"
        print_board()

    def ant_move_next(direction, point):
        """
        1. Flip current color (save current color for next step)
        2. From current color & direction, find new point
             WHITE: new point -> 90 degree turn clockwise
             BLACK: new point -> 90 degree turn counter-clockwise
        """
        point_x = point[0]
        point_y = point[1]
        new_point = None
        new_direction = None
        current_color = get_point_current_color(point)
        # print "current color", current_color, "for", point
        # Flip color
        switch_point_current_color(point)
        # Direction and Point
        if direction == "N":
            if current_color == "WH":
                # turn clockwise
                # from north, go east
                point_x += 1
                new_direction = "E"
            else:
                # turn counter-clockwise
                # from north, go west
                point_x -= 1
                new_direction = "W"
        elif direction == "E":
            if current_color == "WH":
                # turn clockwise
                # from east, go south
                # Note: y + when going down
                point_y += 1
                new_direction = "S"
            else:
                # turn counter-clockwise
                # from east, go north
                # Note: y - when going up
                point_y -= 1
                new_direction = "N"
        elif direction == "S":
            if current_color == "WH":
                # turn clockwise
                # from south, go west
                point_x -= 1
                new_direction = "W"
            else:
                # turn counter-clockwise
                # from south, go east
                point_x += 1
                new_direction = "E"
        elif direction == "W":
            if current_color == "WH":
                # turn clockwise
                # from west, go north
                point_y -= 1
                new_direction = "N"
            else:
                # turn counter-clockwise
                # from west, go south
                point_y += 1
                new_direction = "S"
        return (new_direction, (point_x, point_y))

    def get_point_original_color(point):
        """
        Every point from (0,0) has a predetermined base color
        (0,0) is WHite, calculate out from center to determine
           the color of the point in question
        """
        point_x = point[0]
        point_y = point[1]

        # All white board
        return "WH"

        # B&W checker board
        # if point_x % 2 == point_y % 2:
        #     return "WH"
        # else:
        #     return "BL"

    def test_get_point_original_color():
        print "test get point original color"
        print get_point_original_color((0,0))  # WH
        print get_point_original_color((0,1))  # BL
        print get_point_original_color((0,2))  # WH
        print get_point_original_color((0,3))  # BL
        print

        print get_point_original_color((1,0))  # BL
        print get_point_original_color((1,1))  # WH
        print get_point_original_color((1,2))  # BL
        print get_point_original_color((1,3))  # WH - error BL
        print

        print get_point_original_color((2,0))  # WH
        print get_point_original_color((2,1))  # BL
        print get_point_original_color((2,2))  # WH
        print get_point_original_color((2,3))  # BL

    def get_point_current_color(point):
        """
        Returns the current color of a point
        Note: point should already be in points hash table
        """
        return points[point]

    def switch_point_current_color(point):
        """
        Switch point color from WHite to BLack and vice versa
        Note: point should already be in points hash table
        """
        # print "switching color for point", point
        if points[point] == "WH":
            points[point] = "BL"
        else:
            points[point] = "WH"

    def track_point(point):
        """
        Track each visited point color
        """
        if point not in points:

            points[point] = get_point_original_color(point)

            point_x = point[0]
            point_y = point[1]

            # Min and max x, y for printing
            if minmax[0] is None or minmax[0] > point_x:  # min_x
                minmax[0] = point_x
            if minmax[1] is None or minmax[1] < point_x:  # max_x
                minmax[1] = point_x
            if minmax[2] is None or minmax[2] > point_y:  # min_y
                minmax[2] = point_y
            if minmax[3] is None or minmax[3] < point_y:  # max_y
                minmax[3] = point_y

    def print_board():
        min_x = minmax[0]
        max_x = minmax[1]
        min_y = minmax[2]
        max_y = minmax[3]
        for y in range(min_y, max_y - min_y): # row
            for x in range(min_x, max_x - min_x): # col
                if x == 0 and y == 0:
                    print "0",
                elif (x, y) in points:
                    if get_point_current_color((x,y)) == "BL":
                        print unichr(0x2588),
                        # print "X",
                    else:
                        # print "_",
                        print " ",
                else:
                    if get_point_original_color((x,y)) == "BL":
                        print unichr(0x2588),
                        # print "X",
                    else:
                        # print "_",
                        print " ",
            print ""

    class Ant(object):
        # Note, point (0,0) is a white square
        # Note, starting out facing right -> "E"
        location = (0,0)
        direction = "E"

    ant = Ant()
    ant_moves(ant, k)

print_k_moves(10500)
