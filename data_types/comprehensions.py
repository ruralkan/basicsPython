# Get a list of uppercase characters from a strin
[ch.upper() for ch in "Hello world"]

# Strip off any commas from the end of strings in a list
[item.strip(',') for item in ["these,", "words,", "mostly,", "have,commas,"]]

#Organize letters in words in an alphabetical order
sentence = "Beatiful is better than ugly"
[''.join(sorted(words, key = lambda x: x.lower())) for words in sentence.split()]

# Reverse characters in words of a string and return list
[''.join(sorted(words, reverse = True)) for words in sentence.split()]

# Reverse characters in words
' '.join([''.join(reversed(words)) for words in sentence.split()])

#Reverse words and characters of strings
sentence[::-1]

# When  using if/else thogether use them before the loop
[char if char in "aeiou" else "*" for char in "apple"]

# Dictionaries comprehension
{x: x * x for x in range(10)}
#dictionary using a generator expression
dict((x, x * x) for x in range(10))

#set comprehension
{x for x in range(5)}

#Unique alphabetic characters in a string of text
text = "When in the Course of human events it becomes necessary for one people..."
{ch.lower() for ch in text if ch.isalpha()}

#Comprehension involving tuples
[(x,y) for x, y in [[1, 2], [3, 4], [5, 6]]]

# Ternary expression
[x if  x % 2 == 0 else None for x in range(10)]
[2 * (x if  x % 2 == 0 else -1) + 1 for x in range(10)]

# List comprehension with nested loops
data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]

# List comprehension with nested loops and if
data = [[1], [4, 5], [7, 6], [3, 4, 2]]
output = [element for each_list in data if each_list ==2 for element in each_list if element != 5]


# List comprehension and filter & map

#The following lines are considered "not pythonic"
filtered = filter(lambda x: x%2 == 0, range(10)) #even numbers < 10
results = map(lambda x: 2*x, range(10)) # Multiply each number by two
reduce(lambda x,y: x+y, range(10)) # sum of all elements in a list

#Pythonic way with comprehension
results = [2*x for x in range(10) if x % 2 == 0]
reduced = sum(results)

#Nested List comprehension

#list comprehension with nested loop
[x + y for x in [1, 2, 3] for y in [3, 4, 5]]

#Nested list comprehension
[[x +  y for x in [1, 2, 3]] for y in [3, 4, 5]]

#Nested comprehension used to transpose a matrix
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
[[raw[i] for raw in matrix] for i in range(len(matrix))]

# there is not limit to how deep comprehension can be nested
[[[i + j + k for k in 'cd'] for j in 'ab'] for i in '12']

# Iterate two or more list simultaneously with list comprehension
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']
#two lists
[(i,j) for i, j in zip(list_1, list2)]
#Three lists
[(i, j, k) for i, j, k in zip(list_1, list_2, list_3)]

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
[x for x in range(101) if is_prime(x)]


# Combining filtering and transformation
prime_square_divisor = {x*x:(1, x, x*x) for x in range(101) if is_prime(x)}
