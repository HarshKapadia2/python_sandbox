# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# json to dict
user_json = '{"first_name": "Selena", "last_name": "Gomez", "age": 27}'

# parse to dict
user = json.loads(user_json)

print(user)
print(user['first_name'])


# dict to json
car = {
    'make': 'Ford', 
    'model': 'Mustang',
    'year': 1970    
}

# parse to json
car_json = json.dumps(car)

print(car_json)