# Dictionaries from tuples
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28)]
d = dict(names_and_ages)

# Dictionaries from  keyword arguments
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta')

# Copying dictionaries
d = dict(godenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
e = d.copy
f = dict(e)

# Makes a shallow copy of another dict (only possible if keys are only strings)
h = {**d}
# Also updates the shallow copy with the contents of the yetanotherdict
h = {**d, **otherdict}


# Extend dictionaries
g = dict(wheat=0xF5FEB3, khahi=0xF0E68C, crimson=0xDC132C)
f.update(g)

# If keys are already present in the target dictionary, the value associated
# with these keys are replaced in the target
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM', 194}
stock.update({'GOOG': 894, 'YHOO': 894})

#Marging dictionaries
dic1 = {'w': 1, 'x':2}
dic2 = {'x':2, 'y':3, 'z': 2}

{k: v for d in [dic1, dic2] for k, v in d.items()}

#Marging dictionaries pythonic way
{**dic1, **dic2}

# Iterating over keys
for key in colors:
    print("{key} => {value}".format(key=key, value= color[key]))

# Iterating over values
for value in colors.value():
    print(value)

# Iterating over keys
for key in colors.keys():
    print(key)

# Iterating over key- value pairs
for key, value in colors.items()
    print("{key} => {value}".format(key=key, value= color[key]))

# Removing dictionary items
del stocks['GOOG']

# Dictionaries comprehension
{x: x * x for x in range(10)}
#dictionary using a generator expression
dict((x, x * x) for x in range(10))


# Get values from keys
#value = my_dict.get(key, default_value)

dictionary = {"hello": 1234, "world": 5678}   
w = dictionary.get("hello") # 1234

w = dictionary.get("whatever") # None                                      

w = dictionary.get("whatever", "nuh-uh") # 'nuh-uh'


#switching key and value of dictionary (invert dictionary)
my_dict = {1: 'a', 2: 'b', 3: 'c'}
swapped = {v : k for k, v in my_dict.items()}
swapped = dict(zip(my_dict.values(), my_dict))
swapped = dict(zip(my_dict.values(), my_dict.keys()))
swapped = dict(map(reversed, my_dict.items()))


# All combination of dictionary values
# You can create a list that returns all such combinations of values
import itertools

options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}

keys = options.key()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
