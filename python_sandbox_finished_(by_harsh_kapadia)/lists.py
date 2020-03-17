# A List is a collection which is ordered and changeable. Allows duplicate members.
# index posns start from 0
#create list
num_1 = [1, 2, 3, 4, 5]
fruit = ['mango', 'watermelon', 'strawberry', 'orange', 'dragon fruit']

# use constructor
num_2 = list((1, 2, 3, 4, 5))

# get value
print(num_1, num_2)
print(fruit[1])

# length of list
print(len(fruit))

# append (add to end of list)
fruit.append('kiwi')
print(fruit)

# remove
fruit.remove('dragon fruit')
fruit.pop(2)
print(fruit)

# insert into posn
fruit.insert(10, 'guava') # pushes the element at that posn ahead and inserts itself in that posn.
# If insert posn is beyond last list index posn, then '.insert()' works like '.append()'
print(fruit)

# reverse list
fruit.reverse()
print(fruit)

# sort
fruit.sort()
print(fruit)
fruit.sort(reverse = True)
print(fruit)

# modify value
fruit[0] = 'mangoes'
print(fruit)