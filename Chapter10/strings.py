# objects lookup
class Email:
    def __init__(self, from_addr, to_addr, subject, message) -> None:
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message
        

email = Email("a@example.com", "b@example.com", "You have Maik", "Here's a some mail for you")

template = f"From: {email.from_addr}, To: {email.to_addr}, Subject: {email.subject}, message: {email.message}"
print(template)

# making it look right
# 1
subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print(f"Sub: ${subtotal:.2f} Tax: ${tax:.2f} Total: ${total:.2f}")


# 2
orders = [('burger', 2, 5),
            ('fries', 3.5, 1),
            ('cola', 1.75, 3)]
print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(f"{product:7s}{quantity: ^9d} ${price:<8.2f}${subtotal:>5.2f}")


# 3
import datetime
print(f"{datetime.datetime.now():%Y-%m-%d %I:%M%p }")

# Strings as Unicode
# 1: Convert bytes to text
characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))
print(characters.decode("iso8859-5"))

# 2: Convert text to bytes
characters = "cliché"
print(characters.encode("UTF-8", "replace")) # UTF usually is the best solution
print(characters.encode("latin-1", "ignore"))
print(characters.encode("CP437", "xmlcharrefreplace"))
# print(characters.encode("ascii")) # Error

# 3: Mutable type strings
# a]
b = bytearray(b"abcdefgh")
b[4:6] = b"\x15\xa3"
print(b)

# b]
b = bytearray(b'abcdef')
b[3] = ord(b'g')
b[4] = 68
print(b)


# File IO
# Placing in context
class StringJoiner(list):
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.result = "".join(self)

import string, random

with StringJoiner() as joiner:
    for _ in range(15):
        joiner.append(random.choice(string.ascii_letters))
print(joiner.result)

# Faking files
from io import StringIO, BytesIO
source_file = StringIO("an oft-repeated cliché")
dest_file = BytesIO()

char = source_file.read(1)
while char:
    dest_file.write(char.encode("ascii", "replace"))
    char = source_file.read(1)

print(dest_file.getvalue())
print(source_file)

# Storing objects
import pickle

some_data = ["a list", "containing", 5, 
            "values including another list", 
            ["inner", "list"]]

with open("pickled_list", "wb") as file:
    pickle.dump(some_data, file)

with open("pickled_list", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data


# Serilizing web pages

import json

class Contact:
    def __init__(self, first, last) -> None:
        self.first, self.last = first, last
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
c = Contact("Maamoun", "Haj Najeeb")
print(json.dumps(c.__dict__))
print(c.__dict__)