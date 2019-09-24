# References http://www.dabeaz.com/generators/
# http://www.dabeaz.com/finalgenerator/FinalGenerator.pdf

#NOTE: all generator expression have their own equivalent functions, but not viceverse 

(x**2 for x in range(10))

# Simulating a expensive function
def f(x):
    import time
    time.sleep(.1)
    return x**2

# Avoid this, because this result in two calls of f(x) for 1000 values of x,
#one call for generating the value and the other for checking the if condition
[f(x) for x in range(1000) if f(x) > 10]

# Instead, you shoud evaluate the expensive operation only once for each
# value of x by generating an intermediate iterable
[v for v in (f(x) for x in range(1000)) if v > 10]

#Or using the built-in map
[v for v in map(f, range(1000)) if v > 10]

#Separete generators function is recommended over complex one-liner
def process_prime_numbers(iterable):
    for x in iterable:
        if is_prime(x):
            yield f(x)

def isPrime(n):
    from math import sqrt
    from itertools import count, islice
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

"""
from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
"""

[x for x in process_prime_numbers(range(1000)) if x > 10]


# Counting occurrences using generator expression
sum(1 for i in range(1000)
        if i % 2 == 0 and
        '9' in str(i))

lists = ["platano", "mango", "piña", "platano", "piña", "platano", "mango", "piña", "platano"]

# Using dict comprehension
{item: sum(1 for inner in lists if inner == item) for item in set(lists)} 

#Or
{ítem: list.count(item) for item in lists}

# Converting types in a List
items = ["1", "2", "3", "4"]
[int(item) for item in items]

#or
list(map(float, items))


# Useful generators

#To take and yield only a specific number of items
def take(count, iterable): 
    counter = 0 
    for item in iterable: 
        if counter == count: 
            return 
    yield item 
    counter += 1 
[x for x in take(2,[[1.2], [3,4], [5,6], [7, 8], [9, 10]])] 

# Or
from itertools import islice
[x for x in islice([[1.2], [3,4], [5,6], [7, 8], [9, 10]], 2)]

# To take only the distinct elements of a list and yield
def distinct(iterable): 
        seen = set() 
        for item in iterable: 
            if item in seen: 
                continue 
            yield item 
            seen.add(item) 

items = [3,6,6,2,1,1]
for item in take(3,distinct(items)): 
    print(item)


# Send to a generator
def receiver():
    while True:
        item = yield
        print("Got", item)

recv = receiver()
next(recv)
recv.send("Hello")
recv.send("World")
# To finish a generator
recv.close
next(recv)

# Delegation or yield from
def countdown(n):
    while n > 0:
        yield n
        n -= 1
def countup(stop):
    while n < stop:
        yield n 
        n += 1

def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)

for x in up_and_down(3):
    print(x)

# Chain iterables
def chain(x, y):
    yield from x
    yield from y
a = [1,2,3]
b = [4,5,6]
for x in chain(a, b):
    print(x, end=' ')

# Chain iterables with itertools
from itertools import chain
joined = chain(a, b)

# Merging sequences with zip
for x in zip(a,b):
    print(x)

# Infinite generator

# First approach
def infinite_gen():
    step = 0
    while True:
        yield step
        step += 1
# Iterator
test = infinite_gen()
next(test)
next(test)
# Generator 
f = (x for x in test)

# Second approach
from itertools import count
# Iterator
g = count()
next(g)
next(g)
# Generator
f = (x in count())

# Sending objects to  a generator
def accumulator():
    total = 0
    value = None
    while True:
        # Receive sent value
        value = yield total
        if value is None: break
        #aggregate values
        total += value

generator = accumulator()

# Advance until the first "yield"
next(generator) # 0

from this point on, the generator aggregates values
generator.send(1) # 1
generator.send(10) # 11
generator.send(100) # 110

# Calling next(generator) is equvalent to calling generator.send(None)
next(generator) # StopIteration

# Using a generator to find Fibonacci numbers
def fib(a = 0, b = 1):
    """Generator that yields Fibonacci numbers. a and b  are the seed values"""
    while True:
        yield a 
        a, b = b, a+b
f = fib()
print(', '.join(str(next(f)) for _ in range(10)))

# Infinite sequences
def integers_starting_from(n):
    while True:
        yield n
        n += 1

natural_numbers = integers_starting_from(1)
#Or
natural_numbers = count(1)

# Infinite generatos
multiples_of_three = (x for x in natural_numbers if x%3 == 0)
# List comprehension with range
first_five_ multiples_of_three = [next(multiples_of_three) for _ in range(5)]
# Or
first_five_ multiples_of_three = list[islice(multiples_of_three, 5)]

# Coroutines
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def adder(sum = 0):
    while True:
        x = yield sum
         sum += x

