########################################################################################
###                                    Exercice 1                                    ###
########################################################################################


import math


class Ship:
    def __init__(self, name, size, author):
        self.name = name
        self.size = size  # la size est un str qui vaut soit "small" soit "large"
        self.author = author

    def is_small(self):
        """ retourne True si le vaisseau est "small" """
        return self.size == 'small'

    def is_large(self):
        """ retourne True si le vaisseau est "large" """
        return not self.is_small()


class Spaceport:
    def __init__(self, docked=None):
        self.docked = docked or []  # list des Ship dans le spatioport
        self.max_small = 5  # nombre maximum de quais pour des Ship small
        self.max_large = 2  # nombre maximum de Ship large. Un emplacement large peut être occupé par un Ship small

    def contains(self, ship):
        """ exercice 1 question 2 """
        raise NotImplementedError()

    def dock(self, ship):
        """ exercice 1 question 3 """
        raise NotImplementedError()

    def undock(self, ship):
        """ exercice 1 question 4 """
        raise NotImplementedError()


def is_same_ship(ship1, ship2):
    """ exercice 1 question 1 """
    if ship1.size == ship2.size:
        if ship1.name == ship2.name:
            if ship1.author == ship2.author:
                return True
    else:
        return False
        
    raise NotImplementedError()



########################################################################################
###                                    Exercice 2                                    ###
########################################################################################


def filter_letters(string):
    odd_chars = []
    for i in range(len(string)):
        if i % 2 != 0:
            odd_chars.append(string[i])
            return odd_chars

    """ exercice 2 question 1 """
    raise NotImplementedError()


def count_letters(string):
    """ exercice 2 question 2 """
    char_counter_dict = {}

    for char in "string":
        num_of_occur = 0
        char_counter_dict[char] = num_of_occur
        string.count(char)
        # assign a counter of occurences for every character
        # and put this counter as a value instead of 0 in num_of_occur

    raise NotImplementedError()


def mask_letters(string, mask):
    """ exercice 2 question 3 """
    raise NotImplementedError()


def puissances(start, end):
    for i in range(start,end + 1):
        return math.isqrt(i)**2 == i
        
    """ exercice 2 question 4 """

    raise NotImplementedError()


def return_int():
    """ exercice 2 question 5 """
    return str(42)
