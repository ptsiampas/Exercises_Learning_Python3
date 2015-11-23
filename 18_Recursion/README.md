# Chapter 18 Recursion
Source: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/recursion.html

## Notes
```python
def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of ’order’ and ’size’.
    Leave the turtle facing the same direction.
    """
    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3) # go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
```
**Recursion, the high-level view**
One way to think about this is to convince yourself that the function works correctly when you
call it for an order 0 fractal. Then do a mental leap of faith, saying “the fairy godmother (or
Python, if you can think of Python as your fairy godmother) knows how to handle the recursive
level 0 calls for me on lines 11, 13, 15, and 17, so I don’t need to think about that detail!” All
I need to focus on is how to draw an order 1 fractal if I can assume the order 0 one is already
working.
You’re practicing mental abstraction—ignoring the sub-problem while you solve the big problem.
If this mode of thinking works (and you should practice it!), then take it to the next level. Aha!
now can I see that it will work when called for order 2 under the assumption that it is already
working for level 1.
And, in general, if I can assume the order n-1 case works, can I just solve the level n problem?
Students of mathematics
_**He just tightens up the code - Use it as a reference for the rest**_

```python
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
```

**Recursion, the low-level operational view**
Another way of trying to understand recursion is to get rid of it. If we had separate functions to
draw a level 3 fractal, a level 2 fractal, a level 1 fractal and a level 0 fractal, we could simplify
the above code, quite mechanically, to a situation where there was no longer any recursion, like
this:

```python
def koch_0(t, size):
    t.forward(size)
    
def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
        koch_0(t, size/3)
        t.left(angle)
def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
        koch_1(t, size/3)
        t.left(angle)
def koch_3(t, size):
    for angle in [60, -120, 60, 0]:
        koch_2(t, size/3)
        t.left(angle)
```


## Exercises
1. Modify the Koch fractal program so that it draws a Koch snowflake.
2. Draw a Cesaro torn line fractal, of the order given by the user. 
   a. We show four different lines of orders 0,1,2,3. In this example, the angle of the tear is 10 degrees.
   b. Four lines make a square. Use the code in part (a) to draw cesaro squares. Varying the angle gives interesting effects — experiment a bit, or perhaps let the user input the angle of the tear.
3. A Sierpinski triangle of order 0 is an equilateral triangle. An order 1 triangle can be
drawn by drawing 3 smaller triangles (shown slightly disconnected here, just to help our
understanding). Higher order 2 and 3 triangles are also shown. Draw Sierpinski triangles
of any order input by the user.
4. Adapt the above program to change the color of its three sub-triangles at some depth
of recursion. The illustration below shows two cases: on the left, the color is changed
at depth 0 (the outmost level of recursion), on the right, at depth 2. If the user supplies
a negative depth, the color never changes. (**Hint:** add a new optional parameter
colorChangeDepth (which defaults to -1), and make this one smaller on each recursive
subcall. Then, in the section of code before you recurse, test whether the parameter is zero, and change color.)