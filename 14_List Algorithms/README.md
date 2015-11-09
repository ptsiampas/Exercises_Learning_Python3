# Chapter 14 List Algorithms
http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/list_algorithms.html

## Notes

_Linear Search_(example 14.2)

Searching all items of a sequence from first to last is called a *linear search*. Each time we check whether 
`item == target` we’ll call it a *probe*. We like to count probes as a measure of how efficient our algorithm is, 
and this will be a good enough indication of how long our algorithm will take to execute.

_Binary Search_(Example 14.4)

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
