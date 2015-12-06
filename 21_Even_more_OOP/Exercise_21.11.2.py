# 2. Turn the Exercise 21.11.1 function into a method in the MyTime class.
from unit_tester import test


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """
        Createa MyTime object initialisation of hours, min, secs
        :param hrs:
        :param mins:
        :param secs:
        :return:
        """
        # self.hours = hrs
        # self.minutes = mins
        # self.seconds = secs
        # Calculate total seconds to represent
        totalseconds = hrs * 3600 + mins * 60 + secs
        self.hours = totalseconds // 3600
        leftoversecs = totalseconds % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """
        :return: the number of seconds represented by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """Return True if I am strictly greater than time2"""
        return self.to_seconds() > time2.to_seconds()

    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()


t1 = MyTime(2, 34, 14)
t2 = MyTime(14, 32, 12)

test(MyTime(5, 34, 23).between(t1, t2), True)
test(MyTime(2, 34, 13).between(t1, t2), False)
test(MyTime(2, 34, 15).between(t1, t2), True)
test(MyTime(14, 32, 12).between(t1, t2), False)
test(MyTime(14, 32, 11).between(t1, t2), True)
