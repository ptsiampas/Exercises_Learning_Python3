import string


def remove_punct(s):
    s_without_punct = ""
    s = s.replace("--", " ")
    s = s.replace("-", " ")
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def print_result(word_count):
    final_word_count = list(word_count.items())
    final_word_count.sort()
    count = 0
    layout = "{:<15}{}"
    print(layout.format("Word", "Count"))
    print("======================")
    for (w, c) in final_word_count:
        if count > 10:
            break
        print(layout.format(w, c))
        count += 1


def longest_word(words):
    old_word = ""
    for word in list(words.keys()):
        if len(word) > len(old_word):
            old_word = word
            old_word_length = len(old_word)
    return old_word, old_word_length


file = open("../14_List Algorithms/alice_in_wonderland.txt", "r")

word_counts = {}

while True:
    line = file.readline()
    if len(line) == 0:
        break

    for word in remove_punct(line.lower()).split():
        # Stuff
        # print(word)
        word_counts[word] = word_counts.get(word, 0) + 1

file.close()
print_result(word_counts)
print("The word Alice occurs {} times in the book.".format(word_counts.get("alice")))
w, c = longest_word(word_counts)
print("The longest word in Alice in wonderland is {} with a length of {}".format(w, c))
