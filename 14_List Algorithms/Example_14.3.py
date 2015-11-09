from list_functions import *

bigger_vocab = load_words_from_file("vocab.txt")


print("There are {0} words in the vocab, starting with\n {1} ".format(len(bigger_vocab), bigger_vocab[:6]))

test(text_to_words("My name is Earl!"), ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.'), ["well", "i", "never", "said", "alice"])

book_words = get_words_in_book("alice_in_wonderland.txt")

print("There are {0} words in the book, the first 100 are\n{1}".format(len(book_words), book_words[:100]))


vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]

sbook_words = "the apple fell from the tree to the grass".split()

test(find_unknown_words(vocab, sbook_words), ["from", "to"])
test(find_unknown_words([], sbook_words), sbook_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]), [])

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
