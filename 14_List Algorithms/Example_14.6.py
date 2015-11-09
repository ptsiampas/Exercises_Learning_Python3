from unit_tester import test
from list_functions import *
import time

xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

test(merge(xs, []), xs)
test(merge([], ys), ys)
test(merge([], []), [])
test(merge(xs, ys), zs)
test(merge([1,2,3], [3,4,5]), [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]), ["a", "big", "big", "bite", "cat", "dog"])

bigger_vocab = load_words_from_file("vocab.txt")
book_words = get_words_in_book("alice_in_wonderland.txt")

t0 = time.clock()
combine = bigger_vocab + book_words
combine.sort()
t1 = time.clock()
print("combine.sort took {0:.5f} seconds. Size of list=".format(t1-t0), len(combine))

t0 = time.clock()
zx = merge(bigger_vocab,book_words)
t1 = time.clock()
print("Merge function took {0:.5f} seconds. Size of List=".format(t1-t0),len(zx))
