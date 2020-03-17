# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print('hey')
    if x > 2*y:
        print('hey hey')
elif x == y:
    print('eq')
else:
    print('ugh')


# Logical operators (and, or, not) - Used to combine conditional statements

if x > y or x < 2*y:
    print('hey hey 2')
else:
    if not(x == y):
        print('not eq')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

if 3 in numbers:
    print('yay!')
    print(3 in numbers) # RT: bool


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is not y:
    print(x is not y) # RT: bool