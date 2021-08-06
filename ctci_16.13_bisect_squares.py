"""
Bisect Squares - return line segment to edges of squares that divides squares evenly
Note: squares are paralell with x axis

This problem isn't that difficult. If you are only dividing the squares, a simple calculation 
to find the centers of each square will lead to a slope and the point slope form y = mx + b

The most difficult part of this problem has to do with finding the equation of the line segment
where the line through the centers touches the outer edge of the squares.
I had to do a little digging into my geometry brain, and realize that parametric equations were
a good way to show line segments with regard to a range t. 

I think the Cracking the Coding solution skips over what the actual line segment is supposed
to look like, so your equations might end up looking different.
"""
class square:
    ## Define a square object that returns its center point
    #  Note: squares are paralell to x axis
    def __init__(self, bottom_left_x, bottom_left_y, width, height):
        self.x = bottom_left_x
        self.y = bottom_left_y
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_center(self):
        return (self.x + (self.width / 2.0), self.y + (self.height / 2.0))

    def get_cross_points(self, my, mx):
        """
        Get x or y intercepts using slope from center

        slope m = my/mx

        if my = 0 then line is horizontal - y = number
           return (x, center.y), (x + width, center.y)
        if mx = 0 then line is vertical   - x = number
           return (center.x, y), (center.x, y + height)
        if my/mx == 1
           return corners
        if my/mx < 1
           return None - there aren't any x intercepts
        if my/mx > 1
           return x intercepts using equation of line
        """
        if my == 0:
            # return y intercepts - line is horizontal
            c = self.get_center()
            cx = c[0]
            cy = c[1]
            return [(self.x, cy), (self.x + self.width, cy)]
        if mx == 0:
            # return x intercepts - line is vertical
            c = self.get_center()
            cx = c[0]
            cy = c[1]
            return [(cx, self.y), (cx, self.y + self.height)]
        m = my / mx
        if m == 1:
            # return corners
            return [(self.x, self.y),(self.x + self.width, self.y + self.height)]
        if m == -1:
            # return corners
            return [(self.x, self.y + self.height),(self.x + self.width, self.y)]
        if abs(m) < 1:
            # get y intercepts
            # calculate y intercept from center using slope
            c = self.get_center()
            cx = c[0]
            cy = c[1]
            xb1 = self.x
            xb2 = self.x + self.width
            # print "y intercept - cx:", cx, "cy:", cy, "xb1:", xb1, "xb2:", xb2, "m:", m
            # using point slope form
            # y - y1 = m(x - x1)
            # y = y1 + m(x - x1)
            #    where x are xb1, xb2 (boundaries)
            #    and   x1, y1 are center points cx, cy
            #    y = cy + m(xb1 - cx)
            y1 = cy + m * (xb1 - cx)
            y2 = cy + m * (xb2 - cx)
            return [(xb1, y1), (xb2, y2)]
        if abs(m) > 1:
            # get x intercepts
            # calculate x intercept from center using slope
            c = self.get_center()
            cx = c[0]
            cy = c[1]
            yb1 = self.y
            yb2 = self.y + self.height
            # print "x intercept - cx:", cx, "cy:", cy, "yb1:", yb1, "yb2:", yb2, "m:", m
            # using point slope form
            # y - y1 = m(x - x1)
            # x = ((y - y1) / m) + x1 
            #    where y are yb1, yb2 (boundaries)
            #    and   x1, y1 are center points cx, cy
            #    x = ((yb1 - cy) / m) + cx
            x1 = ((yb1 - cy) / m) + cx
            x2 = ((yb2 - cy) / m) + cx
            return [(x1, yb1), (x2, yb2)]

def get_edges(s1, s2):
    ## find edges of square after line goes through center of each square
    #  will return to points, edge of s1, edge of s2
    #  as list of tuples [(x1, y1), (x2, y2)]
    #  new points will be passed to parametric equestion method

    # check if same point
    c1 = s1.get_center()
    c2 = s2.get_center()
    if c1 == c2:
        # center points are the same coordinate
        # cannot find a single line to separate the squares
        return None
    else:
        # find edge points for s1 and s2
        # passes in slope m = (my / mx)
        x1 = c1[0]
        y1 = c1[1]
        x2 = c2[0]
        y2 = c2[1]
        my = (y2 - y1)
        mx = (x2 - x1)
        e1 = s1.get_cross_points(my, mx)
        e2 = s2.get_cross_points(my, mx)

    # print "e1:", e1, "e2:", e2
    max_d = 0
    max_p1 = None
    max_p2 = None
    for i in range(len(e1)):
        for j in range(len(e2)):
            d = getdistance(e1[i], e2[j])
            if max_d < d:
                max_d = d
                max_p1 = e1[i]
                max_p2 = e2[j]

    # print "e1, e2:", max_p1, max_p2
    return [max_p1, max_p2]

def getdistance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    d = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    return d

def parametric_equation(point1, point2):
    ## generate parametric equations of line segment
    #  points are tuple (x, y)

    # points
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    # slope
    a = x2 - x1  # slope x portion
    b = y2 - y1  # slope y portion
    # print "a:", str(a), "b:", str(b)

    # parametric equations
    # y = y1 + bt
    # x = x1 + at
    eq = "y = " + str(y1) + " + " + str(b) + "t"
    eq += " "
    eq += "x = " + str(x1) + " + " + str(a) + "t"

    # segment range t - solve parametric for t
    # from y = y1 + bt, x = x1 + at
    # t = (y2 - y1) / b or t = (x2 - x1) / a
    if b != 0:
        # if b is 0, line is horizontal and cannot solve for t
        t = (y2 - y1) / b
    elif a != 0:
        # if a is 0, line is vertical and cannot solve for t
        t = (x2 - x1) / a
    else:
        # should not make it here - line cannot be horizontal and vertical
        t = "NA"
    # print "t:", t

    eq += " "
    eq += "range: {0 to " + str(t) + "}"

    return eq

s1 = square(0, 0, 4, 4)
s2 = square(4, 4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

s1 = square(0, 0, 4, 4)
s2 = square(4, -4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

s1 = square(0, 0, 4, 4)
s2 = square(-4, -4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

s1 = square(0, 0, 4, 4)
s2 = square(-4, 4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

s1 = square(0, 0, 4, 4)
s2 = square(4, 4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

## Horizontal test
s1 = square(0, 0, 4, 4)
s2 = square(4, 0, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

## Vertical test
s1 = square(0, 0, 4, 4)
s2 = square(0, 4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"

## Off axis test
s1 = square(0, 0, 4, 4)
s2 = square(2.2, 4, 4, 4)
points = get_edges(s1, s2)
if points is not None:
    # print "points:", points
    print parametric_equation(points[0], points[1])
else:
    print "boxes have the same center"
