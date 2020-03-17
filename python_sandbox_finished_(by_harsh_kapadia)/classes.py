# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greetings(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old!'

    def hasBirthday(self):
        self.age += 1


# extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greetings(self):
        return f'Hello, my name is {self.name}, my age is {self.age} and my balance is {self.balance}!'

# init 'User' obj
user_obj = User('Selena Gomez', 'selenagomez@gmail.com', 27)

print(type(user_obj))
print(user_obj.name)
user_obj.hasBirthday() # 27 + 1 = 28
print(user_obj.greetings()) # age is 28, not 27   

# init 'Customer' obj
customer_obj = Customer('Felix Arvid ulf Kjellberg', 'pewdiepie@gmail.com', 30)
customer_obj.setBalance(30000)

customer_obj.hasBirthday()
print(customer_obj.greetings()) # first pref to fn in customer class