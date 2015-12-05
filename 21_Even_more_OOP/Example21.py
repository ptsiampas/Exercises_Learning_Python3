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
        """Return True if I am strictly greather than time2"""
        return self.to_seconds() > time2.to_seconds()


# def add_time(t1, t2):
#     h = t1.hours + t2.hours
#     m = t1.minutes + t2.minutes
#     s = t1.seconds + t2.seconds
#
#     while s >= 60:
#         s -= 60
#         m += 1
#     while m>=60:
#         m -=60
#         h+=1
#
#     sum_t = MyTime(h, m, s)
#     return sum_t


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)


current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
print("Bread done in {}".format(done_time))

t1 = MyTime(10, 55, 12)
t2 = MyTime(10, 48, 22)
t3 = add_time(t1, t2)
print("Total time adding {} to {} equals {}".format(t1, t2, t3))
t3.increment(500)
print("Added 500 seconds: {}".format(t3))

print("is t1 after t2?", t1.after(t2))

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print("Added t1({}) and t2({}) together = t3({})".format(t1, t2, t3))
t3 = t2 - t1
print("Subtracted t1({}) from t2({}) now = t3({})".format(t1, t2, t3))
