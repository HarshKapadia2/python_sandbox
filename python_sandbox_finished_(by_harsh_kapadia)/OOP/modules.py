# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core module
import datetime # imports entire datetime module
today_1 = datetime.date.today()
print(today_1)
# OR
from datetime import date # just imports date obj from datetime
today_2 = date.today()
print(today_2)

import time
timestamp_1 = time.time()
print(timestamp_1)
# OR
from time import time
timestamp_2 = time()
print(timestamp_2)


'''
pip modules
pip (package manager for python)
pip install --upgrade pip (to update pip)
pip install <module_name> (installs the package globally on your sys)
pip freeze (to check what all is installed in the current scope; scope may be global or a virtual environment)
'''

from camelcase import CamelCase
cc = CamelCase()
print(cc.hump('selena marie gomez'))


# custom model
from validator import validate_email  # (check out validator.py in this folder)
email = 'harshgkapadia@gmail.com'
if validate_email(email):
    print('email is valid')
else:
    print('email is not valid')

'''
A module is a single file (or files) that are imported under one import and used. 
e.g. import my_module

A package is a collection of modules in directories that give a package hierarchy.
e.g. from my_package.timing.danger.internets import function_of_love
'''