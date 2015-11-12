class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()     # Instantiate an object of type Point
q = Point()     # Make a second point

p.x = 3
p.y = 4

print(p.x, p.y, q.x, q.y)   # Each point object has its own x and y

print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y
print("Distance Squared:", distance_squared_from_origin)
