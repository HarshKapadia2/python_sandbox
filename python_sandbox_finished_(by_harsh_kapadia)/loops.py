# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Selena', 'Lucas', 'Felix', 'Brad']

# for person in people:
#     print(person)

# break
# for person in people:
#     if person == 'Felix':
#         break

#     print(person)
    
# continue
# for person in people:
#     if person == 'Felix':
#         continue

#     print(person)

# range
# for i in range(len(people)):
#     print(i)
#     print(people[i])

# for i in range(0, 5): # 0 is included, but 5 is not
#     print(i)

# for i in range(6): # starts from 0, goes till 5
#     print(i)


# While loops execute a set of statements as long as a condition is true.
count = 10

while count > 0:
    print(count)
    count -= 1 # count-- does not exist in python (ie, post/pre increment ops do not exist in python)