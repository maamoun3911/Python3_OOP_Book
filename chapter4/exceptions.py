# import random
# some_exceptions = [ValueError, TypeError, IndexError, None]
# try:
#     choice = random.choice(some_exceptions)
#     print(f"raising {choice}")
#     if choice:
#         raise choice("An error")
# except ValueError:
#     print("Caught a ValueError")
# except TypeError:
#     print("Caught a TypeError")
# except Exception as e:
#     print(f"Caught some other error: {e.__class__.__name__}")
# except BaseException:
#     print("Here al exceptions will raise")
# # else will work if there are not any exceptions
# else:
#     print("This code called if there is no exception")
# # finally will work whatever happens
# finally:
#     print("This cleanup code is always called")

# class InvalidWidthRawal(Exception):
#     def __init__(self, balance, amount) -> None:
#         super().__init__(f"account doesnot have {amount}")
#         self.balance, self.amount = balance, amount
    
#     def overage(self):
#         return self.amount - self.balance

# raise InvalidWidthRawal(250, 50)
