# 3. Overload the >operator so that instead of having to write
#    if t1.after(t2): ...
#    to use
#    if t1 > t2: ...
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

    def __gt__(self, other):
        """Return True if I am strictly greater than time2"""
        return self.to_seconds() > other.to_seconds()

    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()


test(MyTime(2, 34, 14) > MyTime(14, 32, 12), False)
test(MyTime(14, 32, 12) > MyTime(2, 34, 14), True)
