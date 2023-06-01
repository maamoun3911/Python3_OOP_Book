# passing no argument
zipped = zip()
print(list(zipped))
# print(next(zipped))
# StopIteration

print()

a = ["a", "b", "c"]
zipped = zip(a)
for z in zipped:
    print(z)

print()

a = ["a", "b", "c"]
b = 1, 2, 3
for z in zip(a, b):
    print(z)

print()

print(list(zip(range(5), range(100))))

print()

from itertools import zip_longest

a = ["a", "b", "c"]
b = ("d", "e", "f")
c = 1, 2, 3, 4, 5
zipped = zip_longest(a, b, c, fillvalue="!")
print(tuple(zipped))

print()

letters = ["a", "b", "c"]
numbers = 1, 2, 3
for l, n in zip(letters, numbers):
    print(f"letter: {l}, number: {numbers}")


print()


first_dict = {"first name": "Maamoun", "Last name": "Haj Najeeb", "Job": "Django Developer"}
second_dict = {"first name": "Ahmad", "Last name": "Haj Najeeb", "Job": "Node.JS Developer"}
for (k1, v1), (k2, v2) in zip(first_dict.items(), second_dict.items()):
    print(f"First Dict: {k1, v1}, Second Dict: {k2, v2}")


print()


# unzip
pairs = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
numbers, letters = zip(*pairs)
print(letters)
print(numbers)


print()


letters = ["c", "b", "a", "d"]
numbers = [1, 4, 3, 2]
zipped = zip(letters, numbers)
zipped = list(zipped)
zipped.sort(key = lambda x: x[0])
print(zipped)
zipped.sort(key = lambda x: x[1])
print(zipped)


print()


zipped = sorted(zip(letters, numbers), key=lambda x: x[1])
print(zipped)
zipped = sorted(zip(letters, numbers), key=lambda x: x[0])
print(zipped)


print()


fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
zip_dict = dict(zip(fields, values))
print(zip_dict)

field, value = ["job"], ["Python Consultant"]
zip_dict.update(zip(field, value))
print(zip_dict)


print()