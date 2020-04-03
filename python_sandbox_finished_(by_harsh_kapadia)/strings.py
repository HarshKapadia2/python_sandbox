# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Selena'
age = 27

# concatenate
print('My name is ' + name + ' and my age is ' + str(age)) # gives error if int age is not type casted to str

# String Formatting
# positional arguments
print('My name is {arg_1} and my age is {arg_2}.'.format(arg_1 = name, arg_2 = age))
#f-strings (python 3.6+)
print(f'Hey! My name is {name} and my age is {age}.')

# String Methods
s = 'hello WorLd'

# capitalize first letter of str and make all others small
print(s.capitalize()) # i/p: hello World o/p: Hello world

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('WorLd', 'everyone')) # o/p: hello everyone
print(s) # o/p: hello WorLd ie, s does not get over written

# Count
sub = 'o'
print(s.count(sub))

# Starts with
print(s.startswith('hello')) # RT: bool

# Ends with
print(s.endswith('d')) # RT: bool

# Split into a list
print(s.split())
print(s.split('llo')) # splits at specified str, whenever it occurs. That str is not included

# Find position
print(s.find('l'))
print(s.find('z')) # -1 if not found

# Is all alphanumeric
print(s.isalnum()) # RT: bool. FYI, 'space' is not alpha or numeric

# Is all alphabetic
print(s.isalpha()) # RT: bool

# Is all numeric
print(s.isnumeric()) # RT: bool
