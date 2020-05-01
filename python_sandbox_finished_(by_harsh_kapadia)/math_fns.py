import math

num_1 = 2.3
num_2 = -10

# ceil and floor
print(math.ceil(num_1))
print(math.floor(num_1))

# absolute val
print(math.fabs(num_1))
print(math.fabs(num_2)) # o/p: 10.0

# factorial
print(math.factorial(0)) # only int num >= 0

# copysign
print (math.copysign(5.5, -10))

# gcd
print (math.gcd(5,15)) 

# exp (e**a)
print (math.exp(4))

# pow (a**b)
print (math.pow(3,2)) 

# log(a, b) a to base b (If base is not mentioned, the computed value is of natural log.)
print (math.log(2,3))

print (math.log2(16))
print (math.log10(10000)) 

# sqrt
print (math.sqrt(25)) 

# pi
print(math.pi)

# e
print(math.e)

# hypotenuse
print(math.hypot(3, 4))

# Not a number (nan)
if (math.isnan(math.nan)): 
       print ("The number is nan") 
else : print ("The number is not nan") 

'''
for more:
https://www.geeksforgeeks.org/mathematical-functions-in-python-set-3-trigonometric-and-angular-functions/?ref=rp
https://www.geeksforgeeks.org/mathematical-functions-in-python-set-4-special-functions-and-constants/?ref=rp
'''
'''
PS: To round off to 2 decimals, use print('{:0.2f}'.format(answer)). Math library NOT reqd to be imported.
'''