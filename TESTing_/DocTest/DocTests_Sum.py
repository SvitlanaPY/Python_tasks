# import doctest
# class Calc:
#     @staticmethod

def sum(a: (int, float), b: (int, float)):
    """
    Given two integers or floats, return the sum.
    :param a: (int, float)
    :param b: (int, float)
    :return: (int, float)
    >>> sum(2, 3)
    5
    >>> sum(2.0, 4.0)
    6.0
    >>> sum(0.0, 0)
    0.0
    >>> sum('a', 5)
    ValueError('It must be a nmber')
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return ValueError('It must be a nmber')

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# doctest.testmod()

# obj = Calc()


# class Calc:
#     @staticmethod
#     def sum(a, b):
#         # if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         #     return a + b
#         # else:
#         #     return("ValueError")
#
# obj = Calc()
# print(obj.sum("1", 3.0))