# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 2.5             # auto assigned to float
is_cool = True      # first letter caps for bool var
# multiple assignment
y, z, z = (1, 2.5, 'Selena')

print(z)            # will print 'selena'
print(x + x)

# find type of var
print(type(is_cool))

# type casting
y = str(y)
print(type(y))