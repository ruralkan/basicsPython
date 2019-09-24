#Shifting a list using slicing
def shift_list(array, s):
    """
    shifts the elements of a list to the left to right
    Args: 
        array - list to shift
        s - Amount to shift the list ('+': rigth - shift, '-': left- shift)
    Return:
    shifted_array -the shifted list
    """
    # Calculate acutal shift amount (e.g. 11 --> 1 if lenght of the array is 5)
    s %= len(array)

    # reverse the shift direction to be more intuitive
    s *= -1

    #shift arry with slicing
    shifted_array = array[s:] + array[:s]

    return shifted_array
    

# iteration over whole list
ls = ['alpha', 'bravo', 'charly', 'delta', 'echo']
for s in ls:
    print(s[:1])

# Accessing list values
lst = [1, 2, 3, 4]
lst[1:] #[2,3,4]
lst[:3] #[1,2,3]
lst[::2] #[0,3]
lst[::-1] #[4,3,2,1]
lst[-1:0:-1] #[4,3,2]
lst[5:8] #[] since starting index is greater than length of lst, returns empty list
lst[1:10] # [2,3,4] same as ommitin ending index

# Advance slicing

data = "chandant purohit    22 2000" # Assuming data fields of fixed length
name_slice = slice(0,19)
age_slice = slice(19, 21)
salary_slice = slice(22, None)
print(data[name_slice]) #chandant purohit
print(data[age_salary]) # '22'
print(data[salary_slice]) #'2000'


#List methods and supported operators

a = [1, 2, 3, 4, 5]

#  Append values to the list
a.append(7) # [1, 2, 3, 4, 5, 7]
a.append(6) # [1, 2, 3, 4, 5, 7, 6]

# Append  another list
b = [8, 9]
a.append(b) # [1, 2, 3, 4, 5, 7, 6, [8, 9]]
a[7] #[8, 9]

# Append an element of a different type
my_string = "hello world"
a.append(my_string) # a: [1, 2, 3, 4, 5, 7, 6, [8, 9], "hello world"]

# Extend the list by appending elements from another enumerable
a = [1, 2, 3, 4, 5, 7, 6]
b = [8, 9, 10]
a.extend(b) # a: [1, 2, 3, 4, 5, 7, 6,8 ,9, 10]
# Extend the list with elements from a non-list enumerable
a.extend(range(3)) # a: [1, 2, 3, 4, 5, 7, 6 ,8 ,9, 10, 0, 1, 2]

# index(value, [start index])
a.index(7) # return 5
a.index(49) # ValueError, because 49 is not in a
a.index(1, 7) # Return 11

# insert(index, value)
a.insert(0,0) # a: [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 0, 1, 2]
a..insert(2,5) # a: [0, 1, 5, 2, 3, 4, 5, 7, 6, 8, 9, 10, 0, 1, 2]

# pop([index]) removes and return the item at index, without args removes and returns the last element of the list
a.pop(2) # return 5 a: [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 0, 1, 2]
a.pop(8)  # return 8 a: [0, 1, 2, 3, 4, 5, 7, 6, 9, 10, 0, 1, 2]
a.pop() # return 2 a: [0, 1, 2, 3, 4, 5, 7, 6, 9, 10, 0, 1]

# remove(value) removes the first occurence of the specified value
a.remove(0) # a: [1, 2, 3, 4, 5, 7, 6, 9, 10, 0, 1]
a.remove(9) # a: [1, 2, 3, 4, 5, 7, 6, 10, 0, 1]
a.remove(11) # ValueError, because 11 is not in a

# reverse()
a.reverse() # a: [1, 0, 10, 6, 7, 5, 4, 3, 2, 1]

# count(value) count the number of occurrences of value
a.count(1) # return: 2

#sort() sort the list in numerical and lexicographical order return None
a.sort() # a: [0, 1, 1, 2, 3, 4, 5, 6, 7, 10]

# List can ve reversed when using reverse= True flag in the sort() method
a.sort(reverse=True) # a: [10, 7, 6, 5, 4, 3, 2, 1, 1, 0]

# Sort with a key function as an optional parameter
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
def take_second(val):
    return val[1]
random.sort(key= take_second) # random [(4, 1), (2, 2), (1, 3), (3, 4)]

# clear() removes all items from list
a.clear # a: []

# Replication
b = ["bla"] * 3 # b = ["bla", "bla", "bla"]
b = [1,3,5] * 5 # b = [1,3,5, 1,3,5, 1,3,5, 1,3,5, 1,3,5]

# del
a = list(range(10))
del a[::2] # [1,3,5,7,9]

# Copying
new_list = old_list[:]
new_list = list(old_list)
new_list = old_list.copy()


#Count frequency of elements on a list
fruits = ["banana", "orange", "banana", "melon", "banana", "orange"]
# First approach
temp = [] 
count_fruit = dict() 
for fruit in fruits: 
    count = 0 
    if fruit not in count_fruit: 
        for fruit1 in fruits: 
            if fruit == fruit1: 
                count += 1 
        count_fruit[fruit] = count 

# Second approach
freq = {} 
for fruit in fruits: 
    if fruit in freq: 
        freq[fruit] += 1 
    else: 
        freq[fruit] = 1 

#Third approach
times = {}                                                            
for fruit in fruits: 
    times[fruit] = fruits.count(fruit)

# Fourth approach
{item: fruits.count(item) for item in set(fruits)} 

# Final approach
import collections                                                    
collections.Counter(fruits)