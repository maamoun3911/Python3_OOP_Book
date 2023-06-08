from typing import Any
import functools

# class DecoraterClass:
#     def __init__(self, origin_func) -> None:
#         functools.update_wrapper(self, origin_func)
#         self.origin_func = origin_func
    
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         print("already decorated")
#         return self.origin_func(*args, **kwds)

# @DecoraterClass
# def decorated_func(*args, **kwds):
#     return "decorated func"
# print(decorated_func())


# def decorater_func(func):
#     @functools.wraps(func)
#     def wraper_func(*args, **kwargs):
#         print("from wrapper")
#         return func(*args, **kwargs)
#     return wraper_func


# @decorater_func
# def display(name):
#     return f"{name} from display function"
# print(display("Maamoun"))
# print(display.__name__)


# class Square:
#     def __init__(self, width) -> None:
#         self._width = width
    
#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self, value):
#         self._width = value

#     @classmethod
#     def create(cls):
#         return cls(1)

#     @staticmethod
#     def PI():
#         return 3.14
# print(Square.PI())
# a = Square.create()
# print(a.width)


# class Reapeating:
#     def __init__(self, origin_func) -> None:
#         functools.update_wrapper(self, origin_func)
#         self.origin_func = origin_func
    
#     def __call__(self, times, *args: Any, **kwds: Any) -> Any:
#         for _ in range(times):
#             print("From repeating class")
#             print(self.origin_func(*args, **kwds))

# @Reapeating
# def repeated_func(*args, **kwds):
#     return "repeated func returned"

# print(repeated_func(5))

# print("***************")

# def repeat(num_times):
    
#     def decorater_repeat(func):
        
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 print(func(*args, **kwargs))
            
#         return wrapper_repeat
    
#     return decorater_repeat

# @repeat(num_times=4)
# def greet(name):
#     return f"Hello {name}"
# print(greet("Maamoun"))

# print("***************")

# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
        
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
        
#         return wrapper_repeat

#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)

# @repeat
# def say_whee():
#     print("Whee!")

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# print(say_whee())
# print(greet("Maamoun"))

# print("******************")

# import time

# class RepeatingDeco:
#     def __init__(self, func=None) -> None:
#         functools.update_wrapper(self, func)
#         self.func = func
    
#     def __call__(self, times, *args: Any, **kwds: Any) -> Any:
#         if self.func:
#             if times > 0:
#                 time.sleep(times)
#                 print(f"slept for {times} seconds")
#                 return self.__call__(times-1)
#             return f"Done {self.__name__}"

# @RepeatingDeco
# def display(*args, **kwargs):
#     return "Hola"

# print(display(2))

# class count_calls:
#     def __init__(self, origin_func) -> None:
#         functools.update_wrapper(self, origin_func)
#         self.origin_func = origin_func
#         self.counter = 0
    
#     def __call__(self, num, *args, **kwargs):
#         self.counter += 1
#         if num < 2:
#             print(self.counter)
#         return self.origin_func(num, *args, **kwargs)

# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)

# print(fibonacci(10))

###################################################

class Properties:
    def __init__(self, food) -> None:
        self._food = food
    
    @property
    def food(self):
        return self._food
    
    @food.setter
    def food(self, value):
        self._food = value

obj = Properties("Beans")
obj.food = "soya"
print(obj.food)