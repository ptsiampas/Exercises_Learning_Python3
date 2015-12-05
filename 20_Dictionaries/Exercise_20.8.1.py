# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which
# occur in the string together with the number of times each letter occurs. Case should be ignored. A sample
# output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”

import string

letter_items = {}

sentence = "ThiS is String with Upper and lower case Letters"

for letter in sentence.lower():
    if letter in string.ascii_lowercase:
        letter_items[letter] = letter_items.get(letter, 0) + 1

letter_counts = list(letter_items.items())
letter_counts.sort()

for (let, co) in letter_counts:
    print(let, co)
