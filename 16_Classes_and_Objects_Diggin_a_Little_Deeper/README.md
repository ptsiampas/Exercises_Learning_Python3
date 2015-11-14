# Chapter 16


## Exercises 16.6
1. Add a method area to the Rectangle class that returns the area of any instance:
   ```python
   r = Rectangle(Point(0, 0), 10, 5)
   test(r.area(), 50)
   ```
2. Write a perimeter method in the Rectangle class so that we can find the perimeter of
any rectangle instance:
   ```python
   r = Rectangle(Point(0, 0), 10, 5)
   test(r.perimeter(), 30)
   ```
3. Write a flip method in the Rectangle class that swaps the width and the height of any
rectangle instance:
   ```python
   r = Rectangle(Point(100, 50), 10, 5)
   test(r.width, 10)
   test(r.height, 5)
   r.flip()
   test(r.width, 5)
   test(r.height, 10)
   ````
4. Write a new method in the Rectangle class to test if a Point falls within the rectangle. For
this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper
bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0
is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain
the point (10, 2). These tests should pass:
   ```python
   r = Rectangle(Point(0, 0), 10, 5)
   test(r.contains(Point(0, 0)), True)
   test(r.contains(Point(3, 3)), True)
   test(r.contains(Point(3, 7)), False)
   test(r.contains(Point(3, 5)), False)
   test(r.contains(Point(3, 4.99999)), True)
   test(r.contains(Point(-3, -3)), False)
   ```
5. In games, we often put a rectangular “bounding box” around our sprites. (A sprite is an
object that can move about in the game, as we will see shortly.) We can then do collision
detection between, say, bombs and spaceships, by comparing whether their rectangles
overlap anywhere.

   Write a function to determine whether two rectangles collide. _Hint: this might be quite a
tough exercise! Think carefully about all the cases before you code_.