from unit_tester import test
from string import punctuation

def cleanword(word):
    clean_word = ""

    for letter in word:
        if letter not in punctuation:
            clean_word += letter
    return clean_word


def has_dashdash(str):
    if "--" in str:
        return True
    return False


def extract_words(sentence):
    if has_dashdash(sentence):
        sentence = " ".join(sentence.split("--"))

    words = sentence.split()

    for (x, word) in enumerate(words):
        words[x] = cleanword(word.lower())

    return words


def wordcount(word, sentence):
    count = 0
    for w in sentence:
        if word == w:
            count += 1
    return count


def wordset(sentence):
    """ Removes duplicates and sorts final result alphabetic"""
    result = []
    for word in sentence:
        if word not in result:
            result.append(word)
    result.sort()
    return result


def longestword(sentence):
    lword = 0

    for word in sentence:
        if len(word) > lword:
            lword = len(word)

    return lword

test(cleanword("what?"),  "what")
test(cleanword("'now!'"), "now")
test(cleanword("?+='w-o-r-d!,@$()'"),  "word")

test(has_dashdash("distance--but"), True)
test(has_dashdash("several"), False)
test(has_dashdash("spoke--"), True)
test(has_dashdash("distance--but"), True)
test(has_dashdash("-yo-yo-"), False)

test(extract_words("Now is the time!  'Now', is the time? Yes, now."),
     ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsy as she spoke--fancy"),
     ['she','tried','to','curtsy','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]), 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]), 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]), 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]), 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]), ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]), ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]), ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]), 5)
test(longestword(["a", "am", "I", "be"]), 2)
test(longestword(["this","supercalifragilisticexpialidocious"]), 34)
test(longestword([ ]), 0)