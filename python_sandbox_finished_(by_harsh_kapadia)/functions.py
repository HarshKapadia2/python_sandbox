# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create fn
def sayHello(name = 'Lucas'): # default value is used when nothing is passed
    print(f'Hello {name}!')

sayHello('Selena')
sayHello()

# return values
def getSum(num_1, num_2):
    sum = num_1 + num_2
    return sum

print(getSum(1, 1))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSquare = lambda num: num * num

print(getSquare(2))