# Chapter 14 List Algorithms
http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/list_algorithms.html

## Notes

_Linear Search_ ([Example 14.2](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Example_14.2.py))

Searching all items of a sequence from first to last is called a *linear search*. Each time we check whether 
`item == target` we’ll call it a *probe*. We like to count probes as a measure of how efficient our algorithm is, 
and this will be a good enough indication of how long our algorithm will take to execute.

_Binary Search_ ([Example 14.4](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Example_14.4.py))

Binary search gets its name from the fact that each probe splits the list into two pieces 
and discards the one half from the region of interest.

Calculate the maximum number of search using a binary search algorithm: `ceil(log(NumberOfItems + 1, 2))`

_Remove adjacent duplicates_

Sort list then we simply have to remember the most recent item that was inserted into the result, and avoid 
inserting it again

_Merging Sorted Lists_

The algorithm works as follows: we create a result list, and keep two indexes, one into each list (lines 3-5). 
On each iteration of the loop, whichever list item is smaller is copied to the result list, and that list’s index is
advanced. As soon as either index reaches the end of its list, we copy all the remaining items from the other list 
into the result, which we return.

## Exercises Completed
#### 14.11. Exercises
1. The section in this chapter called Alice in Wonderland, again! started with the observation that the merge 
   algorithm uses a pattern that can be reused in other situations. Adapt the merge algorithm to write each of 
   these functions, as was suggested there:
   
     a. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.1a.py)* Return only those items that are present in both lists.
     
     b. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.1b.py)* Return only those items that are present in the first list, but not in the second.
     
     c. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.1c.py)* Return only those items that are present in the second list, but not in the first.
     
     d. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.1d.py)* Return items that are present in either the first or the second list.
     
     f. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.1e.py)* Return items from the first list that are not eliminated by a matching element in the second list. In this 
       case, an item in the second list “knocks out” just one matching item in the first list. This operation is 
       sometimes called `bagdiff`. For example `bagdiff([5,7,11,11,11,12,13], [7,8,11])` would return `[5,11,11,12,13]`

2. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.2.py)* Modify the queens program to solve some boards of size 4, 12, and 16. What is the maximum size puzzle you can 
usually solve in under a minute?

3. *[done](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.3.py)* Adapt the queens program so that we keep a list of solutions that have already printed, so that we don’t print 
the same solution more than once.

4. *[current](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/14_List%20Algorithms/Exercise_14.11.4.py)* Chess boards are symmetric: if we have a solution to the queens problem, its mirror solution — either flipping the 
board on the X or in the Y axis, is also a solution. And giving the board a 90 degree, 180 degree, or 270 degree 
rotation is also a solution. In some sense, solutions that are just mirror images or rotations of other 
solutions — in the same family — are less interesting than the unique “core cases”. Of the 92 solutions for
the 8 queens problem, there are only 12 unique families if you take rotations and mirror images into account. 
Wikipedia has some fascinating stuff about this.
    (a) Write a function to mirror a solution in the Y axis,
    
    (b) Write a function to mirror a solution in the X axis,
    
    (c) Write a function to rotate a solution by 90 degrees anti-clockwise, and use this to
        provide 180 and 270 degree rotations too.
        
    (d) Write a function which is given a solution, and it generates the family of symmetries
        for that solution. For example, the symmetries of `[0,4,7,5,2,6,1,3]` are
        ```
          [[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
          [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
          [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
          [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]]
        ```
    (e) Now adapt the queens program so it won’t list solutions that are in the same family.
   It only prints solutions from unique families.