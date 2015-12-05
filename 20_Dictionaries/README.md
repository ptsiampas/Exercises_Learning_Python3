# 20. Dictionaries
Source: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3/dictionaries.html

## Notes
### Methods of dictionarys
```python
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

for k in eng2sp.keys():
    print("Got Key {} which maps to value {}".format(k, eng2sp[k]))

# create a list of keys
ks = list(eng2sp.keys())
print(ks)

# default method for dictionary is keys()
for k in eng2sp:
    print("Got Key: {}".format(k))

# Put key and value into a tuple for later processing
for (k,v) in eng2sp.items():
    print("Got {} that maps to {}".format(k,v))

# Check for key in dictionary
"one" in eng2sp
```

### Aliasing and copying
`.copy()` is required to work on a copy of the list not the original, if an assignment `(=)` is used then its an _alias_ to 
the original object.

## Glossary

**call graph** A graph consisting of nodes which represent function frames (or invocations), and directed edges 
(lines with arrows) showing which frames gave rise to other frames.
**dictionary** A collection of key:value pairs that maps from keys to values. The keys can be any immutable value,
 and the associated value can be of any type.
**immutable data value** A data value which cannot be modified. Assignments to elements or slices (sub-parts) of 
immutable values cause a runtime error.
**key** A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary. 
Each key must be unique across the dictionary.
**key:value pair** One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.
**mapping type** A mapping type is a data type comprised of a collection of keys and associated values. Python’s 
only built-in mapping type is the dictionary. Dictionaries implement the associative array abstract data type.
**memo** Temporary storage of precomputed values to avoid duplicating the same computation.
**mutable data value** A data value which can be modified. The types of all mutable values are compound types. Lists 
and dictionaries are mutable; strings and tuples are not.

## Exercises
1. **[Completed](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/20_Dictionaries/Exercise_20.8.1.py)** 
Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which 
occur in the string together with the number of times each letter occurs. Case should be ignored. A sample output of 
the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this this:

    ```
    a  2
    c  1
    d  1
    e  5
    g  1
    h  2
    i  4
    l  2
    n  2
    o  1
    p  2
    r  4
    s  5
    t  5
    u  1
    w  2
    ```
2. **[Completed](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/20_Dictionaries/Exercise_20.8.2.py)**
Give the Python interpreter’s response to each of the following from a continuous interpreter session:
a. Will print 35.

    ```python
    >>> d = {"apples": 15, "bananas": 35, "grapes": 12}
    >>> d["bananas"]
    ```
b. adds the key oranges with the value of 20, and then prints the length of the dictionary as 4.

    ```python
    >>> d["oranges"] = 20
    >>> len(d)
    ```
c. Searches the dictionary for the key grapes and returns _True_

    ```python
    >>> "grapes" in d
    ```
d. Produces an error, as the key **pears* don't exist in the dictionary

    ```python
    >>> d["pears"]
    ```
e. Tries to get the value for the key pears, if it doesn't find it will return 0. So this returns 0

    ```python
    >>> d.get("pears", 0)
    ```
f. Turns the dictionary **d** into a list of keys without the values, then sorts the list and finally prints the list.

    ```python
    >>> fruits = list(d.keys())
    >>> fruits.sort()
    >>> print(fruits)
    ```
g. removes the item apples from the list, then does a search for the key **apples** in **d**, which returns _False_

    ```python
    >>> del d["apples"]
    >>> "apples" in d
    ```
Be sure you understand why you get each result. Then apply what you have learned to fill in the body of the function 
below:

    ```python
    def add_fruit(inventory, fruit, quantity=0):
         return
    
    Make these tests work...
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    test("strawberries" in new_inventory, True)
    test(new_inventory["strawberries"], 10)
    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] , 35)
    ```
3. **[Completed](https://github.com/ptsiampas/Exercises_Learning_Python3/blob/master/20_Dictionaries/alice_words.py)**
Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical 
listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. 
(You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) 
The first 10 lines of your output file should look something like this:

    ```
    Word              Count
    =======================
    a                 631
    a-piece           1
    abide             1
    able              1
    about             94
    above             3
    absence           1
    absurd            2
    ```
    How many times does the word alice occur in the book? **385**
4. What is the longest word in Alice in Wonderland? How many characters does it have? **_multiplication_ with _14_ Char**