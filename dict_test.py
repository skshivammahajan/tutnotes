"""
class dict(object)

clear() Remove all items form the dictionary.
copy()  Return a shallow copy of the dictionary.
fromkeys(seq[, v])  Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])    Return the value of key. If key doesnot exit, return d (defaults to None).
items() Return a new view of the dictionary's items (key, value).
keys()  Return a new view of the dictionary's keys.
pop(key[,d])    Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()   Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d]) If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other]) Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()    Return a new view of the dictionary's values

"""


"""
What is dictionary in Python?
Python dictionary is an unordered collection of items.
A dictionary has a key: value pair.
"""


"""
How to create a dictionary?
keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

dict() -> new empty dictionary

dict(mapping) -> new dictionary initialized from a mapping object's
  (key, value) pairs

dict(iterable) -> new dictionary initialized as if via:
  d = {}
for k, v in iterable:
    d[k] = v

dict(**kwargs) -> new dictionary initialized with the name = value pairs
in the keyword argument list.  For example: dict(one=1, two=2)
"""

# Empty Dictionary
d1 = {}
# using the built-in function dict().
d11 = dict()

# dictionary with integer keys
d2 = {1: "one", 2: "two"}

# dictionary with mixed keys
d3 = {'name': "SHIVAM", 8: [1, 2, 3]}


# from sequence having each item as a pair
d4 = dict([(1, 'apple'), (2, 'ball')])
print(d4)


# initialized with the name = value pairs
d5 = dict(one=1, two=2)


"""
How to access elements from a dictionary?
Key can be used either inside square brackets or with the get() method.

The difference while using get() is that it returns None instead of KeyError, if the key is not found.

get(...)
  D.get(k[, d]) -> D[k] if k in D, else d.  d defaults to None.

  The get() method returns:

the value for the specified key if key is in dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.

"""


my_dict = {"name": "SHIVAM", "age": 27}

print(my_dict["name"])
print(my_dict.get("age"))

# Trying to access keys which doesn't exist throws error
# KeyError: 'salary'
# print(my_dict["salary"])

# Print None
print(my_dict.get("salary"))
#  Provided Default value
print('Salary: ', my_dict.get('salary', 0.0))

"""
Python get() method Vs dict[key] to Access Elements
The get() method returns a default value if the key is missing.

However, if the key is not found when you use dict[key], KeyError exception is raised.
"""


"""
How to change or add elements in a dictionary?
Dictionary are mutable.
We can add new items or change the value of existing items using assignment operator.
"""


# If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
my_dict = {"name": "AKKI", "age": 24}

# Since the key is already present, value gets updated
my_dict["age"] = 25

# Add item
my_dict["salary"] = 25000

print(my_dict)


"""
How to delete or remove elements from a dictionary?

pop(...) remove a particular item(provided key) in a dictionar
  D.pop(k[, d]) -> v, remove specified key and return the corresponding value.
  If key is not found, d (default value) is returned if given, otherwise KeyError is raised


popitem(...)  remove and return an arbitrary item (key, value)
  D.popitem() -> (k, v), remove and return some(key, value) pair as a 2 - tuple
but raise KeyError if D is empty.

clear(...) All the items can be removed at once using the clear() method.
  D.clear() -> None.  Remove all items from D.

del  -->  keyword to remove individual items or the entire dictionary itself.

"""
# create a dictionary
squares = {1: "one", 3: "nine", 4: "sixteen", 5: "twentyfive", 2: "four"}

# remove a particular item
print(squares.pop(4))

print(squares)

# KeyError is raised if default value is not specified
print(squares.pop(6, "Don't Exist"))


# (2, 'four')
print(squares.popitem())
# (5, 'twentyfive')
print(squares.popitem())
# (3, 'nine')
print(squares.popitem())
# (1, 'one')
print(squares.popitem())
# KeyError: 'popitem(): dictionary is empty'
# print(squares.popitem())


squares = {1: "one", 3: "nine", 4: "sixteen", 5: "twentyfive", 2: "four"}

# remove all items
squares.clear()

# Output: {}
print(squares)


squares = {1: "one", 3: "nine", 4: "sixteen", 5: "twentyfive", 2: "four"}
# delete a particular item
del squares[5]
# Raises KeyError if key is not present
# del squares[6]


# delete the dictionary itself
del squares
# Throws Error NameError: name 'squares' is not defined
# print(squares)


"""
copy(...)
  D.copy() ->  Returns a shallow copy of D
  It doesn't modify the original dictionary.


Difference in Using copy() method, and = Operator to Copy Dictionaries?
When copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.

When = operator is used, a new reference to the original dictionary is created.

"""

original = {1: 'one', 2: 'two'}
new = original.copy()

new.clear()

# when the new dictionary is cleared, the original dictionary remains unchanged.
print("original", original)
print("new", new)

original = {1: 'one', 2: 'two'}
new = original

new.clear()
# when the new dictionary is cleared, the original dictionary is also cleared.
print("original", original)
print("new", new)


"""
fromkeys(iterable, value=None)
  Returns a new dict with keys from iterable and values equal to value.


The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.

iterable - sequence of elements which is to be used as keys for the new dictionary
value (Optional) - value which is set to each each element of the dictionary
"""

sequence = ['a', 'e', 'i', 'o', 'u']

my_dict = dict.fromkeys(sequence)
# {'a': None, 'e': None, 'i': None, 'o': None, 'u': None}
print(my_dict)

# {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}
my_dict = dict.fromkeys(sequence, 2)
print(my_dict)


# Create a dictionary from mutable object list

# Set
keys = {"a", "e", "i", "o", "u", "e"}
value = [1]


vowels = dict.fromkeys(keys, value)
print(vowels)
value.append(2)
print(vowels)

"""
If the provided value is a mutable object (whose value can be modified) like list, dictionary, etc., when the mutable object is modified, each element of the sequence also gets updated.

This is because, each element is assigned a reference to the same object (points to the same object in the memory).

To avoid this issue, we use dictionary comprehension.
"""

# Set
keys = {"a", "e", "i", "o", "u", "e"}
value = [1]

dict_comp = {k: list(value) for k in keys}
# # you can also use { key : value[:] for key in keys }
"""
Here, for each key in keys, a new list from value is created and assigned to it.

In essence, value isn't assigned to the element but a new list is created from it, which is then assigned to each element in the dictionary.
"""
print(dict_comp)


"""
items(...) returns a view object that displays a list of dictionary's (key, value) tuple pairs.
  D.items() -> a set - like object providing a view on D's items

keys(...) returns a view object that displays a list of all the keys in the dictionary
  D.keys() -> a set - like object providing a view on D's keys

values(...) returns a view object that displays a list of all the values in the dictionary.
  D.values() -> an object providing a view on D's values


Note: When the dictionary is changed, the view object also reflect these changes.
"""


# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

# dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
print(sales.items())


# How items() works when a dictionary is modified?
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)
"""
The view object items doesn't itself return a list of sales items but it returns a view of sales's (key, value) pair.

If the list is updated at any time, the changes are reflected on to the view object itself, as shown in the above program.
"""


person = {'name': 'Phill', 'age': 22}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

# How keys() works when dictionary is updated?

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)
# Here, when the dictionary is updated, keys is also automatically updated to reflect changes.

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

values = sales.values()
print('Original items:', values)


"""
setdefault(...)
  D.setdefault(k[, d]) -> D.get(k, d), also set D[k] = d if k not in D

  The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.


  If not provided, the default_value will be None.

  The setdefault() returns:

value of the key if it is in the dictionary
None if key is not in the dictionary and default_value is not specified
default_value if key is not in the dictionary and default_value is specified

"""

# when key is in the dictionary?
person = {'name': 'Phill', 'age': 22}
print(person.setdefault("age"))

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ', person)
print('salary = ', salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('id', 22)
print('person = ', person)
print('age = ', age)

"""
update(...)

  D.update([E, ]**F) -> None.  Update D from dict / iterable E and F.



The update() method adds element(s) to the dictionary if the key is not in the dictionary.
If the key is in the dictionary, it updates the key with the new value.

The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

It doesn't return any value (returns None).
"""

d = {1: "one", 2: "three"}
# # updates the value of key 2
d.update({2: "Four"})

print(d)
# adds element with key 3
d.update({3: "Three"})
d.update(y=3, z=0)
d.update([("S", "MA")])
print(d)


"""
Python Dictionary Comprehension
Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.

Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.

"""
squares = {x: x**x for x in range(1, 11)}
print(squares)


squares = {}
for x in range(1, 11):
    squares[x] = x ** x
print(squares)


even_squares = {x: x**x for x in range(1, 11) if x % 2 == 0}
print(even_squares)


# Dictionary Membership Test

"""
We can test if a key is in a dictionary or not using the keyword in. Notice that membership test is for keys only, not for values.
"""
print(2 in even_squares)

print(4 not in squares)


# Iterating Through a Dictionary
# Using a for loop we can iterate though each key in a dictionary.
for i in even_squares:
    print(i)


"""
Built-in Functions with Dictionary

all()   Return True if all keys of the dictionary are true (or if the dictionary is empty).
any()   Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()   Return the length (the number of items) in the dictionary.
sorted()    Return a new sorted list of keys in the dictionary.


cmp()   Compares items of two dictionaries.  (Not available in Python 3)
"""

k = even_squares.keys()
even_squares.update({0: "Zero"})
print(k)
print(all(even_squares))


d = {}
# True
print(all(d))
# False
print(any(d))


print(len(even_squares))
print(sorted(even_squares))
