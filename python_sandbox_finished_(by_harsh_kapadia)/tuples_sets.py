# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create tuple
fruit_1 = ('mango', 'watermelon', 'strawberry', 'orange', 'dragon fruit')
# using constructor
fruit_2 = tuple(('mango', 'watermelon', 'strawberry', 'orange', 'dragon fruit'))

print(fruit_1, fruit_2)

fruit_3 = ('apple')
print(fruit_3, type(fruit_3)) # type str

fruit_4 = ('blueberry',) # single value needs trailing comma to be a tuple
print(fruit_4, type(fruit_4)) # type tuple

# get value
print(fruit_1[0])

# values cannot be changed in tuples
# fruit_1[0] = 'water apple' # error

# deleting a tuple
del fruit_2
# print(fruit_2) # o/p: error. 'fruit_2' not defined

# length of tuple
print(len(fruit_1))


# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_5 = {'mango', 'apple'}

# check if in set
print('mango' in fruit_5) # RT: bool

# add to set
fruit_5.add('watermelon')
print(fruit_5)

# add duplicte member
fruit_5.add('watermelon') # doesn't give err, but doesn't insert the duplicate val
print(fruit_5)

# remove from set
fruit_5.remove('watermelon')
print(fruit_5)

# clear the set (remove all elements)
fruit_5.clear()
print(fruit_5)

# delete set
del fruit_5
# print(fruit_5) # o/p: error. 'fruit_5' not defined