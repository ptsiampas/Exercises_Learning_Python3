# 5. Create some test cases for the increment method. Consider specifically the case where the number of seconds to
# add to the time is negative. Fix up increment so that it handles this case if it does not do so already. (You may
# assume that you will never subtract more seconds than are in the time object.)
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
        t2 = MyTime(0, 0, self.to_seconds() + seconds)
        if t2.to_seconds() < 0:
            t2 = MyTime(0, 0, 0)

        self.hours = t2.hours
        self.minutes = t2.minutes
        self.seconds = t2.seconds

    def to_seconds(self):
        """
        :return: the number of seconds represented by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __gt__(self, other):
        """Return True if I am strictly greater than time2"""
        return self.to_seconds() > other.to_seconds()

    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()


# Couldn't get the unit test function to work with the output.

t1 = MyTime(1, 32, 12)
t1.increment(500)
print(t1)
t1.increment(-50000)
print(t1)
