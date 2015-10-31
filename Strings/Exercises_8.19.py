__author__ = 'petert'
import sys
import string

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)



def ack_everything():
    """
    2. Modify:
        prefixes = "JKLMNOPQ"
        suffix = "ack"

        for letter in prefixes:
            print(letter + suffix)
    so that Ouack and Quack are spelled correctly.
    """
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "Q":
            letter += "u"
        print(letter + suffix)


def count_letters(word, letter):
    """
    3. Encapsulate
        fruit = "banana"
        count = 0
        for char in fruit:
            if char == "a":
                count += 1
        print(count)
    in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments.
    Make the function return the number of characters, rather than print the answer. The caller
    should do the printing.
    """
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def count_letters2(word, letter):
    """
    4. Now rewrite the count_letters function so that instead of traversing the string, it repeatedly calls the
    find method, with the optional third parameter to locate new occurrences of the letter being counted.
    """
    count = 0
    c = word.find(letter)
    while c != -1:
        if c > count:
            count += 1
        c = word.find(letter, c + 1)
    return count


def remove_punct(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def count_words_and_e(paragraph):
    """ 5b. Write a function which removes all punctuation from the string, breaks the string into a list of words,
    and counts the number of words in your text that contain the letter “e”. Your program should print an
    analysis of the text like this:

    Your text contains 243 words, of which 109 (44.8%) contain an "e".
    """
    e_words = 0
    total_words = 0

    no_punct_para = remove_punct(paragraph).split()

    for word in no_punct_para:
        if count_letters2(word, "e") > 0:
            e_words += 1
        total_words += 1

    percentage_e = (total_words - e_words) / total_words * 100

    msg="Your text contains {0} words, of which {1} ({2:.1f}%) contain an \"e\""\
        .format(total_words, e_words, percentage_e)
    return msg


def print_times_table():
    """ 6. Print out a neatly formatted multiplication table, up to 12 x 12."""
    for i in range(1,12):
        for x in range(1,13):
            print("{0:>3}".format(i*x), end="\t")
        print()
    return


def reverse(word):
    """
    7. Write a function that reverses its string argument, and satisfies these tests:

        test(reverse("happy"), "yppah")
        test(reverse("Python"), "nohtyP")
        test(reverse(""), "")
        test(reverse("a"), "a")
    """
    rev_word = ""
    c = len(word)

    while c > 0:
        rev_word += word[c-1]
        c -= 1
    return rev_word


def mirror(word):
    """
    Write a function that mirrors its argument:

    test(mirror("good"), "gooddoog")
    test(mirror("Python"), "PythonnohtyP")
    test(mirror(""), "")
    test(mirror("a"), "aa")
    """
    return word + reverse(word)


def remove_letter(letter, word):
    """
    9. Write a function that removes all occurrences of a given letter from a string:

    test(remove_letter("a", "apple"), "pple")
    test(remove_letter("a", "banana"), "bnn")
    test(remove_letter("z", "banana"), "banana")
    test(remove_letter("i", "Mississippi"), "Msssspp")
    test(remove_letter("b", ""), "")
    test(remove_letter("b", "c"), "c")
    """
    final = ""
    for char in word:
        if char != letter:
            final += char
    return final


def is_palindrome(word):
    """ 10. Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

    test(is_palindrome("abba"), True)
    test(is_palindrome("abab"), False)
    test(is_palindrome("tenet"), True)
    test(is_palindrome("banana"), False)
    test(is_palindrome("straw warts"), True)
    test(is_palindrome("a"), True)
    # test(is_palindrome(""), ??)    # Is an empty string a palindrome?
    """
    if word == reverse(word):
        return True
    return False


def count_sub(pattern, nStr):
    """
    Write a function that counts how many times a substring occurs in a string:

    test(count_sub("is", "Mississippi"), 2)
    test(count_sub("an", "banana"), 2)
    test(count_sub("ana", "banana"), 2)
    test(count_sub("nana", "banana"), 1)
    test(count_sub("nanan", "banana"), 0)
    test(count_sub("aaa", "aaaaaa"), 4)
    """
    count = 0
    position = nStr.find(pattern)
    while position != -1:
        if position > count:
            count += 1
        position = nStr.find(pattern, position + 1)
    return count


def occurrences(string, sub):
    """http://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences"""
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count


def remove(pattern, n_string):
    # Write a function that removes the first occurrence of a string from another string:
    #
    # test(remove("an", "banana"), "bana")
    # test(remove("cyc", "bicycle"), "bile")
    # test(remove("iss", "Mississippi"), "Missippi")
    # test(remove("eggs", "bicycle"), "bicycle")

    f_pos = n_string.find(pattern)  # Find the first position of the occurrence
    if f_pos == -1:                 # Didn't find the pattern, return with the word
        return n_string
    new_str = ""


    return new_str


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("\nTests for Exercise 1")
    test(count_letters("banana", "a"), 3)
    test(count_letters2("banana","a"),3)
    test(count_letters2("banana","x"),0)

    # 7. Tests
    print("\nTests for Exercise 7")
    test(reverse("happy"), "yppah")
    test(reverse("Python"), "nohtyP")
    test(reverse(""), "")
    test(reverse("a"), "a")

    # 8. Tests
    print("\nTests for Exercise 8")
    test(mirror("good"), "gooddoog")
    test(mirror("Python"), "PythonnohtyP")
    test(mirror(""), "")
    test(mirror("a"), "aa")

    # 9. Tests
    print("\nTests for Exercise 9")
    test(remove_letter("a", "apple"), "pple")
    test(remove_letter("a", "banana"), "bnn")
    test(remove_letter("z", "banana"), "banana")
    test(remove_letter("i", "Mississippi"), "Msssspp")
    test(remove_letter("b", ""), "")
    test(remove_letter("b", "c"), "c")

    # 10. Tests
    print("\nTests for Exercise 10")
    test(is_palindrome("abba"), True)
    test(is_palindrome("abab"), False)
    test(is_palindrome("tenet"), True)
    test(is_palindrome("banana"), False)
    test(is_palindrome("straw warts"), True)
    test(is_palindrome("a"), True)


    # 11. Tests
    print("\nTests for Exercise 11")
    test(count_sub("is", "Mississippi"), 2)
    test(count_sub("an", "banana"), 2)
    test(count_sub("ana", "banana"), 2)
    test(count_sub("nana", "banana"), 1)
    test(count_sub("nanan", "banana"), 0)
    test(count_sub("aaa", "aaaaaa"), 4)
    test(occurrences("aaaaaa", "aaa"), 4)

    # 12. Tests
    print("\nTests for Exercise 12")
    test(remove("an", "banana"), "bana")
    test(remove("cyc", "bicycle"), "bile")
    test(remove("iss", "Mississippi"), "Missippi")
    test(remove("eggs", "bicycle"), "bicycle")

### # ------------------- MAIN ------------------- ###

ack_everything()

# 5a. Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text
# perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
ma_Quote = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """
print(count_words_and_e(ma_Quote))

print_times_table()

test_suite()