class SMS_store:
    def __init__(self):
        self.messages = []
        self.has_been_viewed = False
        self.from_number = ""
        self.time_arrived = ""
        self.text_of_SMS = ""

    def __str__(self):
        counter = 0
        for message in self.messages:
            (viewed, number, time, sms) = message
            print('({0}): {1}, {2}, {3}, {4}'
                  .format(counter, viewed, number, time, sms))
            counter += 1
        return 'Done'

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """
        Makes new SMS tuple, inserts it after other messages
        in the store. When creating this message, its
        as_been_viewed status is set False.
        :return:
        """
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        self.messages.append((self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS))
        return self.message_count()

    def message_count(self):
        """
        returns the number of sms messages in my_inbox
        :return:
        """
        return len(self.messages)

    def get_unread_indexes(self):
        """
        returns list of indexes of all not-yet-viewed SMS messages
        :return:
        """
        c = 0
        indexes = []
        while c < self.message_count():
            if not self.messages[c][0]:
                indexes.append(c)
            c += 1
        return indexes

    def get_message(self, i):
        """
        return (from_number, time_arrived, text_of_sms) for message[i]
        Also change its state to "has been viewed".
        If there is no message at position i, return None
        """
        (viewed, number, time, sms) = self.messages[1]
        self.messages[1] = (True, number, time, sms)
        return '({0}, {1}, {2})'.format(number, time, sms)

    def delete(self, i):
        return self.messages.pop(i)

    def clear(self):
        self.messages = []
        return 'Messages Cleared'


my_inbox = SMS_store()

# Setup data

print(my_inbox.add_new_arrival("0433-322-100", "Monday 11. March 2002", "Message 0"))
my_inbox.add_new_arrival("0433-322-100", "Tuesday 12. March 2002", "Message 1")
my_inbox.add_new_arrival("0433-322-100", "Wednesday 13. March 2002", "Message 2")
my_inbox.add_new_arrival("0433-322-100", "Thursday 14. March 2002", "Message 3")
my_inbox.add_new_arrival("0433-322-100", "Friday 15. March 2002", "Message 4")
my_inbox.add_new_arrival("0433-322-100", "Saturday 16. March 2002", "Message 5")
my_inbox.add_new_arrival("0433-322-100", "Sunday 17. March 2002", "Message 6")
my_inbox.add_new_arrival("0433-322-100", "Monday 18. March 2002", "Message 7")
my_inbox.add_new_arrival("0433-322-100", "Tuesday 19. March 2002", "Message 8")
print(my_inbox.add_new_arrival("0433-322-100", "Wednesday 20. March 2002", "Message 9"))

print(my_inbox)
print("Get Message:", my_inbox.get_message(3))
print(my_inbox)
print("Unread Messages:", my_inbox.get_unread_indexes())
print("Deleted Message: ", my_inbox.delete(4))
print(my_inbox)
print(my_inbox.clear())
print(my_inbox)
