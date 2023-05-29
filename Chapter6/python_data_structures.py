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

from collections import defaultdict

def tuple_counter(dictionary, key, list_value) -> tuple[int, list]:
    dictionary[key] = len(dictionary)+1, []
    dictionary[key][1].append(list_value)
    # return (num_items, [])

d = defaultdict(tuple[int, list])
tup_con = tuple_counter(d, "a", "hello")
tup_con = tuple_counter(d, "b", ", world")
tup_con = tuple_counter(d, "c", "!")
tup_con = tuple_counter(d, "c", "?")

print(d)


num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])
d = defaultdict(tuple_counter)

d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append('world')
d['b'][1].append("you")
print(d)
