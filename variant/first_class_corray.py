# 1
# def square(x: int):
#     return x ** x

# first_class_func = square
# print(first_class_func)


# 2
# def square(x: int):
#     return x * x

# def my_map(func, nums_list: list[int]):
#     result = []
#     for num in nums_list:
#         result.append(func(num))
#     return result
# print(my_map(square, [1, 2, 3, 4, 5]))


# 3
# def hover(msg):
    
#     def say_hi():
#         return f"saying {msg}"
    
#     return say_hi

# hovering = hover("Hi")
# print(hovering)


# 4
# def html_tag(tag: str):
    
#     def html_content(content):
#         return f"<{tag}>{content}</{tag}>"
    
#     return html_content

# html_h1 = html_tag("h1")
# print(html_h1("header"))


# closure
# 1
# def outer_func():
#     message = "Hi"
    
#     def inner_func():
#         return message
    
#     return inner_func

# my_func = outer_func()
# print(my_func())

# 2
# def outer_func():
#     message = "Hi"
    
#     def inner_func():
#         return message
    
#     return inner_func

# my_func = outer_func()
# print(my_func())

# 3
# import logging
# logging.basicConfig(filename="example.log", level=logging.INFO)


# def logger(func):
    
#     def log_func(*args):
#         logging.info(f"Runing: {func.__name__} with {args}")
#         print(func(*args))
        
#     return log_func

# def add(x, y):
#     return x+y

# def subtract(x, y):
#     return x-y

# add_logger = logger(add)
# sub_logger = logger(subtract)

# add_logger(1, 2)
# add_logger(3, 2)

# sub_logger(5, 4)
# sub_logger(5, 6)

# Decoraters
# 1
# def decorater_function(func):
#     def wraper_function():
#         return f"message: from wraper func, displaying {func.__name__}"
    
#     return wraper_function

# @decorater_function
# def display():
#     return "display function ran"

# a]
# displaying = decorater_function(display)
# print(displaying())

# b]
# print(display())

# 2
# class ClassDecorater:
    
#     def __init__(self, origin_function) -> None:
#         self.origin_function = origin_function
    
#     def __call__(self, *args, **kwargs):
#         print("decorater text")
#         return self.origin_function(*args, **kwargs)

# @ClassDecorater
# def display(name, age):
#     return f"display function ran with {name}-{age}"

# print(display("Maamoun", 22))

# 3

# def decorater_func(origin_func):
    
#     def wraper_func(*args, **kwargs):
#         print(f"wraper func calling {origin_func.__name__}")
#         return origin_func(*args, **kwargs)
    
#     return wraper_func

# @decorater_func
# def display(*args, **kwargs):
#     return f"full info {args} {kwargs}"
# print(display("Maamoun", 22, tall=165))

# 4
# from typing import Any

# import time

# class TimeDecorater:
    
#     def __init__(self, origin_func) -> None:
#         self.origin_func = origin_func
    
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         t1 = time.time()
#         result = self.origin_func(*args, **kwds)
#         t = time.time() - t1
#         print(f"it takes {t} time to extract {self.origin_func.__name__} function")
#         return result

# @TimeDecorater
# def add_numbers(x, y):
#     time.sleep(2)
#     return x+y
# print(add_numbers(1, 5))

# 5
