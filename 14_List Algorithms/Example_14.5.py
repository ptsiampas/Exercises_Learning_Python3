from unit_tester import test
from list_functions import *

# Test cases

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]), [1,2,3,5,6,9])
test(remove_adjacent_dups([]), [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]), ["a", "big", "bite", "dog"])

all_words = get_words_in_book("alice_in_wonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book. Only {1} are unique.".format(len(all_words), len(book_words)))
print("The first 100 words are\n{0}".format(book_words[:100]))