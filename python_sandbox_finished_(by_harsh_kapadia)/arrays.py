# no fixed size
# arrays can be from numpy or scipy or arrays modules: https://stackoverflow.com/questions/111983/python-array-versus-numpy-array
# only one datatype allowed with arrays module


import array

arr_1 = array.array('i', [1, 2, -3, 4, 5]) # i = int, l = long, caps for unsigned types, f =  float, d = double
print(arr_1)

print(arr_1.buffer_info()) # o/p: add of arr_1 & no. of elements
print(arr_1.typecode) # o/p: i

arr_1.reverse()
print(arr_1)

for i in range(len(arr_1)):
    print(arr_1[i])
# OR
# for i in arr_1:
#   print(i)

# creating an array if you don't know the types or values
arr_2 = array.array(arr_1.typecode, (ele**2 for ele in arr_1)) # you can change the name of 'ele', but both have to be same
print(arr_2)

# taking values from the user and searching for ele
arr_3 = array.array('i', []) # blank int arr

arr_length = int(input('Enter the len of the arr: '))
for i in range(arr_length):
    arr_3.append(int(input('Enter Value: ')))
print(arr_3)

ele_check = int(input('Enter ele to be searched: '))
print(arr_3.index(ele_check)) # or manual loop search



# OR
# import array as arr
# val = arr.array(...)

# OR
# from array import *
# val = array(...) # easiest