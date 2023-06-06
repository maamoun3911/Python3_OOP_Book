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
#         warnings = (line.replace("WARNING", "") for line in in_file if "WARNING" in line)
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


# "another example to descripe the idea, and I also suggest to DeBug"
# class CustomOddList:
#     def __init__(self, lalist: list[int]) -> None:
#         self.lalist: list[int] = list(lalist)
#         self.pointer = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.pointer < len(self.lalist):
#             num = self.lalist[self.pointer]
#             self.pointer += 1
#             if num % 2:
#                 return num
#         if self.pointer >= len(self.lalist):
#             raise StopIteration

# lalista = CustomOddList(range(10))
# for i in lalista:
#     print(i)


# 4
# def warnings_filter(insequence):
#     for line in insequence:
#         if "WARNING" in line:
#             yield line.replace("WARNING", "")

# with open(input_file, "r") as infile:
#     with open(output_file, "w") as outfile:
#         filtering = warnings_filter(infile)
#         for line in filtering:
#             outfile.write(line)


# "another example to describe idea"

# def filtering(lalista: list[int]):
#     for i in lalista:
#         if not i % 2:
#             yield i

# lalista = list(range(10))
# for i in filtering(lalista):
#     print(i)

# default arguments
# def hello(b=[]):
#     b.append('a')
#     return b

# print(hello())
# print(hello())


# def hello(b=None):
#     if b is None:
#         b = []
#     b.append('a')
    # return b

# print(hello())
# print(hello())


# class Options:
#     default_options = {
#     'port': 21,
#     'host': 'localhost',
#     'username': None,
#     'password': None,
#     'debug': False,
#     }
    
#     def __init__(self, **kwargs):
#         self.options: dict[str] = dict(Options.default_options)
#         self.options.update(kwargs)
    
#     def __getitem__(self, key):
#         return self.options[key]

# option = Options(port=2)
# print(option['port'])
# options = Options()
# print(options.options)


# import shutil
# import os.path

# def augmented_move(target_folder, *filenames, verbose=False, **specific):
#     '''Move all filenames into the target_folder, allowing
#     specific treatment of certain files.'''
#     def print_verbose(message, filename):
#         '''print the message only if verbose is enabled'''
#         if verbose:
#             print(message.format(filename))
    
#     for filename in filenames:
#         target_path = os.path.join(target_folder, filename)
#         if filename in specific:
#             if specific[filename] == 'ignore':
#                 print_verbose(f"Ignoring {filename}")
#             elif specific[filename] == 'copy':
#                 print_verbose(f"Copying {filename}")
#                 shutil.copyfile(filename, target_path)
#         else:
#             print_verbose("Moving {0}", filename)
#             shutil.move(filename, target_path)


# def show_args(arg1, arg2, arg3="THREE"):
#     print(arg1, arg2, arg3)

# show_args(*range(3))

# ladict = {"arg1": "one", "arg2": "two", "arg3": "three"}
# show_args(**ladict)

# Functions are obects two
# functions are top level objects
# def my_function():
#     print("The Function Was Called")
# my_function.description = "A silly function"

# def second_function():
#     print("The second was called")
# second_function.description = "A sillier function."

# def another_function(function):
#     print("The description:", end=" ")
#     print(function.description)
#     print("The name:", end=" ")
#     print(function.__name__)
#     print("The class:", end=" ")
#     print(function.__class__)
#     print("Now I'll call the function passed in")
#     function()

# another_function(my_function)
# another_function(second_function)


# import datetime
# import time


# class TimedEvent:
#     def __init__(self, endtime, callback) -> None:
#         self.endtime = endtime
#         self.callback = callback
        
#     def ready(self) -> bool:
#         return self.endtime <= datetime.datetime.now()


# class Timer:
#     def __init__(self) -> None:
#         self.events = []
        
#     def call_after(self, delay, callback):
#         end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        
#         self.events.append(TimedEvent(end_time, callback))
    
#     def run(self):
#         while True:
#             ready_events = (e for e in self.events if e.ready())
#             for event in ready_events:
#                 event.callback(self)
#                 self.events.remove(event)
#             time.sleep(0.5)


# def format_time(message, *args):
#     now = datetime.datetime.now().strftime("%I:%M:%S")
#     print(message.format(*args, now=now))

# def one(timer):
#     format_time("{now}: Called One")
# def two(timer):
#     format_time("{now}: Called Two")
# def three(timer):
#     format_time("{now}: Called Three")

# class Repeater:
#     def __init__(self):
#         self.count = 0
    
#     def repeater(self, timer):
#         format_time("{now}: repeat {0}", self.count)
#         self.count += 1
#         timer.call_after(5, self.repeater)


# timer = Timer()
# timer.call_after(1, one)
# timer.call_after(2, one)
# timer.call_after(2, two)
# timer.call_after(4, two)
# timer.call_after(3, three)
# timer.call_after(6, three)
# repeater = Repeater()
# timer.call_after(5, repeater.repeater)
# format_time("{now}: Starting")
# timer.run()


# class Repeater:
#     def __init__(self):
#         self.count = 0
        
#     def __call__(self, timer):
#         format_time("{now}: repeat {0}", self.count)
#         self.count += 1
#         timer.call_after(5, self)
        
# timer = Timer()
# timer.call_after(5, Repeater())
# format_time("{now}: Starting")
# timer.run()

# class A:
#     def hello(self):
#         return "Hello"
# def hello():
#     return "hi"

# a = A()
# a.hello = hello
# print(a.hello())

