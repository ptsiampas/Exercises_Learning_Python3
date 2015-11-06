from unit_tester import test

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    if old == " ":
        return new.join(s.split())

    return new.join(s.split(old))

test(myreplace(",", ";", "this, that, and some other thing"),
                         "this; that; and some other thing")
test(myreplace(" ", "**","Words will now      be  separated by stars."),
                 "Words**will**now**be**separated**by**stars.")