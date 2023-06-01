# # reversed
# normal_list=[1,2,3,4,5]

# class CustomSequence():
#     def __len__(self):
#         return 5
    
#     def __getitem__(self, index):
#         return f"x{index}"


# class FunkyBackwards():
#     def __reversed__(self):
#         return "Backwards!"

# for seq in normal_list, CustomSequence(), FunkyBackwards():
#     print(f"{seq.__class__.__name__}: ", end="")
#     for item in reversed(seq):
#         print(item, end=", ")
#     print()
    
    
# # enumerate
# friends = ["Ahmad", "Maamoun", "Ali"]

# for i, friend in enumerate(friends):
#     print(i, friend)
#     print(type((i, friend)))
#     print(type(i), type(friend))

# print()

# # zip

# import os

# contacts = []
# with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
#     header = file.readline().strip().split()
#     for line in file:
#         line = line.strip().split()
#         contact = zip(header, line)
#         contact = dict(contact)
#         contacts.append(contact)
# for contact in contacts:
#     print("{first} {last} {email}".format(**contact))


# print()


# # min, max, sum
# def min_max_indexes(seq):
#     minimum = min(enumerate(seq), key=lambda index: index[1])
#     maximum = max(enumerate(seq), key=lambda index: index[1])
#     return minimum[0], maximum[0]
# alist = [5, 0, 1, 4, 6, 3]
# print(min_max_indexes(alist))


# print()


# # list comperhensions
# a = list(range(10))
# a = [i for i in a if i % 2 == 0]
# print(a)


# print()


# # Dict Comperhensions

# with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
#     header = file.readline().strip().split()
#     contacts = [
#         dict(
#             zip(header, line.strip().split())
#             ) for line in file
#     ]
# print(contacts)


# print()

# # set comperhensions
# from collections import namedtuple
# Book = namedtuple("Book", "author title genre")
# books = [
#     Book("Pratchett", "Nightwatch", "fantasy"),
#     Book("Pratchett", "Thief Of Time", "fantasy"),
#     Book("Le Guin", "The Dispossessed", "scifi"),
#     Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
#     Book("Turner", "The Thief", "fantasy"),
#     Book("Phillips", "Preston Diamond", "western"),
#     Book("Phillips", "Twice Upon A Time", "scifi"),
# ]
# fantasy_authors = {
#     book.author for book in books if book.genre == "fantasy" 
# }
# print(fantasy_authors)


# print()


# fantasy_titles = {
#     book.title: book for book in books if book.genre == "fantasy"
# }
# print(fantasy_titles)


# print()


# Generators

import os

input_file = os.path.join(os.path.dirname(__file__), "log_file.txt")
output_file = os.path.join(os.path.dirname(__file__), "output_log_file.txt")

# 1
# with open(input_file, "r") as infile:
#     with open(output_file, "w") as outfile:
#         warnings = (line for line in infile if "WARNING" in line)
#         for line in warnings:
#             outfile.write(line)


# 2
# with open(input_file, ) as in_file:
#     with open(output_file, "w") as out_file:
#         warnings = (line.replace("\tWARNING", "") for line in in_file if "WARNING" in line)
#         for line in warnings:
#             out_file.write(line)

# 3
# "I really suggest to DeBug this code in your machine"
# class WarningFilter:
#     def __init__(self, insequence) -> None:
#         self.insequence = insequence
#     def __iter__(self):
#         return self
#     def __next__(self):
#         line = self.insequence.readline()
#         while line and "WARNING" not in line:
#             line = self.insequence.readline()
#         if not line:
#             raise StopIteration
#         return line.replace("\tWARNING", "")

# with open(input_file) as infile:
#     with open(output_file, "w") as outfile:
#         filtering = WarningFilter(infile)
#         for line in filtering:
#             outfile.write(line)
            

# # "another example to descripe the idea, and I also suggest to DeBug"
# class CustomList:
#     def __init__(self, lalista) -> None:
#         self.lalista = lalista
        
#     def __iter__(self):
#         self.pointer = 0
#         return self
    
#     def __next__(self):
#         element = self.lalista[self.pointer]
#         while self.pointer < len(self.lalista) and element % 2:
#             self.pointer += 1
#             if self.pointer >= len(self.lalista):
#                 raise StopIteration
#             element = self.lalista[self.pointer]
#         if not element % 2:
#             self.pointer += 1
#             return element

# customlist = CustomList(list(range(10)))
# for i in customlist:
#     print(i)

# 4
def warnings_filter(insequence):
    for line in insequence:
        if "WARNING" in line:
            yield line.replace("\tWARNING", "")

with open(input_file, "r") as infile:
    with open(output_file, "w") as outfile:
        filtering = warnings_filter(infile)
        for line in filtering:
            outfile.write(line)


# "another example to describe idea"

# def filtering(lalista: list[int]):
#     for i in lalista:
#         if not i % 2:
#             yield i

# lalista = list(range(10))
# for i in filtering(lalista):
#     print(i)