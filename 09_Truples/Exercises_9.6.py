__author__ = 'petert'

def tuple_function(a):
    """
    :param a: Tuple of something with 3 elements
    :return: none
    """
    (item1, item2, item3) = a
    print("{0}, {1}, {2}".format(item1, item2, item3))


var_tuple = ("string", 12, "blond")
tuple_function(var_tuple)
