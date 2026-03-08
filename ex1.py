import dotenv
from dotenv import load_dotenv
import os

print(load_dotenv())

name=os.getenv('NAME')
age=os.getenv('AGE')
print(f'my name is {name}')
print(f'my age is {age}')