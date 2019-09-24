empty_set=set()
literal_set={'foo', 'bar', 'baz'}
set_from_list=set(['foo', 'bar', 'baz'])
set_from_iter={x for x in range(30)}

# Get unique elements of a list
restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants) # {'Burger King', 'Chicken Chicken', "McDonald's"}

# Convert set to list
list(unique_restaurants)

# Remove all duplicates an return another list
list(set(restaurants))

# Operations on sets

# Intersection or intersection update
{1,2,3,4,5}.intersection({3,4,5,6}) # {3,4,5}
{1,2,3,4,5} & {3,4,5,6} # {3,4,5}

test = {1,2,3,4,5} 
test &= {3,4,5,6} # {3,4,5}

# Union or update
{1,2,3,4,5}.union({3,4,5,6}) # {1,2,3,4,5,6}
{1,2,3,4,5} | {3,4,5,6}  # {1,2,3,4,5,6}

{1,2,3,4,5}.update({3,4,5,6}) # {1,2,3,4,5,6}
test = {1,2,3,4,5}
test |= {3,4,5,6} # {1,2,3,4,5,6}

# Difference or difference update
{1,2,3,4}.difference({2,3,5}) # {1,4}
{1,2,3,4} - {2,3,5} # {1,4}
test = {1,2,3,4}
test -= {2,3,5}  # {1,4}

# Symmetric difference
{1,2,3,4}.symmetric_difference({2,3,5}) # {1,4,5}
{1,2,3,4,5} ^ {2,3,5} # {1,4,5}

# Superset check
{1,2}.issuperset({1,2,3}) # False
{1,2} <= {1,2,3} # False

# Subset check
{1,2}.issubset({1,2,3}) # True
{1,2} <= {1,2,3} # True

# Disjoint check
{1,2}.isdisjoint({3, 4}) # True
{1,2}.isdisjoint({1,4}) # True


# With single elements
 2 in {1,2,3} # True
 4 in {1,2,3} # False
 4 not in {1,2,3} # True

 # Add and remove
 s = {1,2,3}
 s.add(4) # s: {1,2,3,4}
 s.discard(3) # s: {1,2,4}
 s.discard(5) # s: {1,2,4}

 s.remove(2) # s: {1,4}
 s.remove(3) # KeyError

 # Length
 len({1,2,3}) # 3

# Set of sets
 {{1,2}, {3,4}}  # unhashable type: 'set'
{frozenset({1,2}), frozenset({3,4})}
# Multisets
from collections import Counter
counterA = Counter(['a', 'b', 'b', 'c']) # Counter({'a': 1, 'b': 2, 'c': 1})

