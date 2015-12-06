# 21. Even More OOP
Source: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/even_more_oop.html


## 21.11. Exercises
1. **[complete](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/21_Even_more_OOP/Exercise_21.11.1.py)** Write a Boolean function between that takes two MyTime objects, `t1` and `t2`, as arguments, and returns True if the
invoking object falls between the two times. Assume `t1 <= t2`, and make the test closed at the lower bound and open 
at the upper bound, i.e. return True `if t1 <= obj < t2`.

2. **[complete](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/21_Even_more_OOP/Exercise_21.11.2.py)** Turn the above function into a method in the MyTime class.

3. **[complete](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/21_Even_more_OOP/Exercise_21.11.3.py)** Overload the necessary operator(s) so that instead of having to write
    
    ```
    if t1.after(t2): ...
    ```
    we can use the more convenient
    
    ```
    if t1 > t2: ...
    ```
4. **[complete](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/21_Even_more_OOP/Exercise_21.11.4.py)** Rewrite increment as a method that uses our “Aha” insight.
5. **[complete](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/21_Even_more_OOP/Exercise_21.11.5.py)** Create some test cases for the increment method. Consider specifically the case where the number of seconds to add 
to the time is negative. Fix up increment so that it handles this case if it does not do so already. (You may assume 
that you will never subtract more seconds than are in the time object.)


