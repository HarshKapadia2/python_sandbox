# Python has functions for creating, reading, updating, and deleting files.

# open a file
my_file = open('my_file.txt', 'w') # w = write mode

# get file info
print('Name: ', my_file.name)
print('is_closed: ', my_file.closed) # ie, whether the file is closed within this script (RT: bool)
print('Opening mode: ', my_file.mode)

# write to file
my_file.write('I love Selena Gomez! ')
my_file.write('\'Who says\' is my favourite song! ')

my_file.close()

# append to file
my_file = open('my_file.txt', 'a') # a = append mode
my_file.write('Selena Gomez is a good person!')

my_file.close()

# read from file
my_file = open('my_file.txt', 'r+')
print(my_file.read(100)) # no of characters to be read

my_file.close()