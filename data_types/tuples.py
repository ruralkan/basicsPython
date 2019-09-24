# Indexing
x = (1,2,3)
x[0] # 1
x[1] # 2
x[2] # 3
x[-1] # 3
x[-2] # 2
x[-3] # 1

x[:-1] #(1,2)
x[-1:] # (3,)

# Tuples dont have .append, .extend
# += operator can be used like append to a tuple
t = (1,2)
q = t 
t += (3,4) # (1,2,3,4)
q # (1,2)

t = tuple("lupins") # ('l', 'u', 'p', 'i', 'n', 's')

# Reversing elements
t[::-1] # ('s', 'n', 'i', 'p', 'u', 'l')

# length
len(t) # 6

# Max of a tuple
max(t) # 'u'
min(t) # 'i'

# Convert list into a tuple
lists = [1, 2, ,3, 4]
tuple(lists) # (1, 2, 3, 4)

# Comparation
# cmp(a,b)
# -1 if a<b
# 0 if a=b 
# 1 if a>b

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1', '2', '3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

tuple1 > tuple2 # True

tuple1 < tuple2 # False


# Tuple concatenation
tuple1 + tuple2 # ('a', 'b', 'c', 'd', 'e', '1', '2', '3')
