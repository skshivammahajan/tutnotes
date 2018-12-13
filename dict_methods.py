dict1 = {1: "one", 2: "two", 3: "three"}
print(dict1)

# The clear() method removes all items from the dictionary.
dict1.clear()
print("dict1 = ", dict1)

# also remove all elements from the dictionary by assigning empty dictionary {}
d = {1: "one", 2: "two"}
d = {}
print("d = ", d)
# difference between calling clear() and assigning {} if there is another variable referencing the dictionary.

d = {1: "one", 2: "two"}
d1 = d
d.clear()    # Clear the reference
print('Removing items using clear()')
print('d =', d)
print('d1 =', d1)

d = {1: "one", 2: "two"}
d1 = d
d = {}   # Create new empty dict
print('Removing items by assigning {}')
print('d =', d)
print('d1 =', d1)

# Removing items using clear() --- Affect on Both
# d = {}
# d1 = {}
# Removing items by assigning {} ---> No affect on other
# d = {}
# d1 = {1: 'one', 2: 'two'}


original = {1: 'one', 2: 'two'}
# This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary
new = original.copy()

print('Original: ', original)
print('New: ', new)

# Difference in Using copy() method, and = Operator to Copy Dictionaries

# When copy() method is used, a new dictionary is created
# which is filled with a copy of the references from the original dictionary.

# When = operator is used, a new reference to the original dictionary is created.

original = {1: 'one', 2: 'two'}
new = original

# removing all elements from the list
#  when the new dictionary is cleared, the original dictionary is also cleared.
new.clear()

print('new: ', new)
print('original: ', original)

original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
# when the new dictionary is cleared, the original dictionary remains unchanged.
new.clear()

print('new: ', new)
print('original: ', original)


# The fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.
#
# If the value argument is set, each element of the newly created dictionary is set to the provided value.

# The fromkeys() method takes two parameters:
#
# sequence - sequence of elements which is to be used as keys for the new dictionary
# value (Optional) - value which is set to each each element of the dictionary

# Create a dictionary from a sequence of keys
keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
# {'a': None, 'u': None, 'o': None, 'e': None, 'i': None}

# Create a dictionary from a sequence of keys with value
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = dict.fromkeys(keys, value)
# {'a': 'vowel', 'u': 'vowel', 'o': 'vowel', 'e': 'vowel', 'i': 'vowel'}

# Create a dictionary from mutable object list
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]
vowels = dict.fromkeys(keys, value)
# updating the value
value.append(2)
# {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}
# {'a': [1, 2], 'u': [1, 2], 'o': [1, 2], 'e': [1, 2], 'i': [1, 2]}

# To avoid this issue, we use dictionary comprehension.
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

vowels = {key: list(value) for key in keys}
# you can also use { key : value[:] for key in keys }
# for each key in keys, a new list from value is created and assigned to it.


sales = {'apple': 2, 'orange': 3, 'grapes': 4}
# items() method returns a view object that displays a
#  list of a given dictionary's (key, value) tuple pair.
print(sales.items())

for i, j in sales.items():
    print(i, j)

# How items() works when a dictionary is modified?
# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)

# Original items: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
# Updated items: dict_items([('orange', 3), ('grapes', 4)])

# Reason : The view object items doesn't itself return a list of sales items but
# it returns a view of sales's (key, value) pair.
# If the list is updated at any time, the changes are reflected on to the view object itself


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# The keys() returns a view object that displays a list of all the keys.
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

# How keys() works when dictionary is updated?
person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)


# # random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

# The values() method returns a view object that displays a list of all values in a given dictionary.
print(sales.values())


person = {'name': 'Phill', 'age': 22}

# Return the value for the specified key if key is in dictionary.
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
# Return None if the key is not found and value is not specified.
print('Salary: ', person.get('salary'))

# value is provided
# Return value if the key is not found and value is specified.
print('Salary: ', person.get('salary', 0.0))


# Python get() method Vs dict[key] to Access Elements

# The get() method returns a default value if the key is missing.

# However, if the key is not found when you use dict[key], KeyError exception is raised.


person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.
result = person.popitem()

print('person = ', person)
print('Return Value = ', result)

# The popitem() raises a KeyError error if the dictionary is empty.


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

# The pop() method removes and returns an element from a dictionary having the given key.
element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

# Pop an element not present from the dictionary, provided a default value
# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava', 'banana')
print('The popped element is:', element)
print('The dictionary is:', sales)


person = {'name': 'Phill'}

# returns the value of a key (if the key is in dictionary). If not, it inserts key with a value(optional) to the dictionary.
# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ', person)
print('salary = ', salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ', person)
print('age = ', age)


# The update() method updates the dictionary with the elements
# from the another dictionary object or from an iterable of key/value pairs.
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)
d1 = {3: "three"}

# adds element with key 3
d.update(d1)
# Iterable
d.update(y=3, z=0)
print(d)
