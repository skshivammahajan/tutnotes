"""
What are generators in Python?

Python generators are a simple way of creating iterators.
Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).


How to create a generator in Python?

It is as easy as defining a normal function with yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. 

Both yield and return will return some value from a function.
The difference is that, while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls.

Differences between Generator function and a Normal function?

Generator function contains one or more yield statement.
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().


Unlike normal functions, the local variables are not destroyed when the function yields. 

Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object using something like a = my_gen().

Note: One final thing to note is that we can use generators with for loops directly.


"""


def generate_infinite_even():
    a = 2
    while 1 == 1:
        if a % 2 == 0:
            print(a)
            yield a
        a += 2


# num = generate_infinite_even()
# num.__next__()
# num.__next__()
# num.__next__()
# num.__next__()
# num.__next__()
# num.__next__()


# for n in num:
#     print(n)


def my_gen():
    n = 1
    print("This is first value ", n)
    yield n

    n += 1
    print("This is second value ", n)
    yield n

    n += 1
    print("This is third value ", n)
    yield n


for i in my_gen():
    print(i)


def rev_str(my_str):
    length_str = len(my_str)
    for i in range(length_str - 1, -1, -1):
        yield my_str[i]


for s in rev_str("SHIVAM"):
    print(s)


"""
Python Generator Expression

generator expression creates an anonymous generator function.

The syntax for generator expression is similar to that of a list comprehension in Python. 
But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that 
while list comprehension produces the entire list, generator expression produces one item at a time.

They are kind of lazy, producing items only when asked for. 
For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

 generator expression did not produce the required result immediately. 
 Instead, it returned a generator object with produces items on demand.

"""


# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x**2 for x in my_list))


for i in (x**2 for x in my_list):
    print(i)

# Generator expression can be used inside functions.
# When used in such a way, the round parentheses can be dropped.
sum(x**2 for x in my_list)


"""
Why generators are used in Python?

1. Easy to Implement
2. Memory Efficient

A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large.

Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

3. Represent Infinite Stream


"""