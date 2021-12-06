import os
from typing import List
#import utils
print(os.getcwd())

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

print(os.listdir("honeybee-json-files")) 