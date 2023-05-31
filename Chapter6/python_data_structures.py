# tuples

from collections import namedtuple

# Stock = namedtuple("Stock", "symbol current high low")
# dollar = Stock("$", 613.30, 625.86, 610.50)
# at = Stock("@", 613.30, 625.86, 610.50)
# print(type(dollar))
# print(dollar)
# symbol, current, high, low = dollar
# print(symbol)
# froma = namedtuple("English", "word expression")
# print(froma("hello", "just saying hi"))

#############################################################

# Dictionaries

# stocks = {"GOOG": (613.30, 625.86, 610.50),
#             "MSFT": (30.25, 30.70, 30.19)
#             }
# # setdefault means if the key is there don't do anything, 
# # if it isn't there make a key and value as we implement
# stocks.setdefault("GOOG", (613.30, 625.86, 610)) # no effect
# stocks.setdefault("RIM", (67.38, 68.48, 67.28))
# print(stocks['GOOG'])
# print(stocks['RIM'])

#############################################################

# def letter_frequency(sentence):
#     frequencies = {}
#     for letter in sentence:
#         frequencies.setdefault(letter, 0)
#         frequencies[letter] += 1
#     return frequencies
# print(letter_frequency("maamoun"))

#############################################################

# from collections import defaultdict

# def letter_frequency(sentence):
#     frequencies = defaultdict(int)
#     for letter in sentence:
#         frequencies[letter] += 1
#     return frequencies
# print(letter_frequency("maamoun"))

#############################################################

# from collections import defaultdict
# Stock = namedtuple("Stock", "symbol current high low")
# dollar = Stock("$", 613.30, 625.86, 610.50)
# at = Stock("@", 613.30, 625.86, 610.50)

# def stock_frequency(*group):
#     Stock = defaultdict(tuple)
#     for stock in group:
#         Stock[stock[0]] = stock[1:]
#     return Stock
# print(stock_frequency(dollar, at))

#############################################################

# from collections import defaultdict

# num_items = 0
# def tuple_counter():
#     global num_items
#     num_items += 1
#     return (num_items, [])

# d = defaultdict(tuple_counter)
# d['a'][1].append("hello")
# d['b'][1].append('world')
# d['b'][1].append("you")
# print(d)


#########################
# I leave global variables because of it's problems and turn into classes, much easier

# from collections import defaultdict


# class Counting:
#     def __init__(self) -> None:
#         self.counter = 0
    
#     def tuple_counter(self) -> tuple[int, list]:
#         self.counter += 1
#         return self.counter, []


# tuple_counter = Counting().tuple_counter
# defdict = defaultdict(tuple_counter)
# # defdict = defaultdict(counter.tuple_counter())
# # if we do this it will give error
# # TypeError: first argument must be callable or None
# defdict["a"][1].append("hello")
# defdict['b'][1].append('world')
# defdict['b'][1].append("you")
# print(defdict)

#######################################################
# Lists
#######
# import string

# CHARACTERS = list(string.ascii_letters)

# def letter_frequencies(sentence):
#     frequencies: list[tuple[str, int]] = [(c, 0) for c in CHARACTERS]
#     for letter in sentence:
#         index = CHARACTERS.index(letter)
#         frequencies[index] = letter, frequencies[index][1]+1
#     return frequencies
# print(letter_frequencies("maamoun"))

# class WeirdSortee:
#     def __init__(self, string: str, number: int, sort_num: bool):
#         self.string = string
#         self.number = number
#         self.sort_num = sort_num
    
#     def __lt__(self, object):
#         if self.sort_num:
#             return self.number < object.number
#         return self.string < object.string
    
#     def __repr__(self):
#         return f"{self.string}:{self.number}"


# a = WeirdSortee('a', 4, True)
# c = WeirdSortee('c', 3, True)
# b = WeirdSortee('b', 2, True)
# d = WeirdSortee('d', 1, True)
# l = [a,b,c,d]

# l.sort()
# print(l)

# x = [(1,'c'), (2,'a'), (3, 'b')]
# x.sort()
# print(x)
# x.sort(key=lambda x: x[1])
# print(x)

###########################

# class TooLong(Exception):
#     pass

# class ExtendedList(list):
#     def append(self, __object: str) -> None:
#         if len(__object) > 5:
#             raise TooLong("Word must be less than 5 letters")
#         return super().append(__object)
    
# lalista = ExtendedList()
# lalista.append("Ahmad")
# # lalista.append("Maamoun")
# help(list.__setitem__)

#############################

# from collections import OrderedDict
# help(OrderedDict)