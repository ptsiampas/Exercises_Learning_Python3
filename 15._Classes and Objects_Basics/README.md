# 15. Classes and Objects — the Basics

http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/classes_and_objects_I.html

## Notes
It may be helpful to think of a class as a factory for making objects. The class itself isn’t an instance of a point, 
but it contains the machinery to make point instances. Every time we call the constructor, we’re asking the factory 
to make us a new object. As the object comes off the production line, its initialization method is executed to get 
the object properly set up with its factory default settings.
### Parameters and classes note
Be aware that our variable only holds a reference to an object, so passing tess into a function creates an alias: 
both the caller and the called function now have a reference, but there is only one turtle!

### Thinking about OOP
The most important advantage of the object-oriented style is that it fits our mental chunking and real-life experience
more accurately. In real life our cook method is part of our microwave oven — we don’t have a cook function sitting 
in the corner of the kitchen, into which we pass the microwave! Similarly, we use the cellphone’s own methods to 
send an sms, or to change its state to silent. The functionality of real-world objects tends to be tightly bound 
up inside the objects themselves. OOP allows us to accurately mirror this when we organize our programs.

## 15.12 Exercises
1. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.1.py)** Rewrite the distance function from the chapter titled fruitful functions so that it takes
two Points as parameters instead of four numbers.
2. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.2.py)**Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about 
the x-axis. For example, Point(3, 5).reflect_x() is (3,-5)
3. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.3.py)**Add a method slope_from_origin which returns the slope of the line joining the
origin to the point. For example,
    ```python
    >>> Point(4, 10).slope_from_origin()
    2.5
    ```
  What cases will cause your method to fail? _When a zero is given for any of the points._
4. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.4.py)** The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients
a and b completely describe the line. Write a method in the Point class so that if a point
instance is given another point, it will compute the equation of the straight line joining
the two points. It must return the two coefficients as a tuple of two values. For example,
    ```python
    >>> print(Point(4, 11).get_line_to(Point(6, 15)))
    >>> (2, 3)
    ```
    This tells us that the equation of the line joining the two points is “y = 2x + 3”. When
    will your method fail? _When it isn't given a target point to calculate_

5. **[Un-finished](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.5.py)** Given four points that fall on the circumference of a circle, find the midpoint of the circle.
    When will you function fail?
    **Hint:** You must know how to solve the geometry problem before you think of going
    anywhere near programming. You cannot program a solution to a problem if you don’t
    understand what you want the computer to do!

6. **[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/15._Classes%20and%20Objects_Basics/Exercise_15.12.6.py)** Create a new class, SMS_store. The class will instantiate SMS_store objects, like your
inbox or your outbox on your cellphone:
`my_inbox = SMS_store()`
This store can hold multiple SMS messages (i.e. its internal state will just be a list of
messages). Each message will be represented as a tuple:
`(has_been_viewed, from_number, time_arrived, text_of_SMS)`
Your inbox object should provide these methods:
```python
my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# Makes new SMS tuple, inserts it after other messages
# in the store. When creating this message, its
# has_been_viewed status is set False.
my_inbox.message_count()
# returns the number of sms messages in my_inbox
my_inbox.get_unread_indexes()
# returns list of indexes of all not-yet-viewed SMS messages
my_inbox.get_message(i)
# return (from_number, time_arrived, text_of_sms) for message[i]
# Also change its state to "has been viewed".
# If there is no message at position i, return None
my_inbox.delete(i)
my_inbox.clear()
# delete the message at index i
# delete all messages from inbox
```
Write the class, create a message store object, write tests for these methods, and implement the methods.
