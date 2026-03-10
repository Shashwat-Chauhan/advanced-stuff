from dataclasses import dataclass
from typing import Callable, Any
# @dataclass is a decorator from the dataclasses module (Python 3.7+) that automatically generates boilerplate methods for classes that mainly store data.

# Normally when you create a class for storing data, you must write:
# __init__
# __repr__
# __eq__
# @dataclass automatically generates these methods based on class attributes.

@dataclass
class Person:
    name: str
    age: int
    email : str = "shashwat@gmail.com" # default value 

person = Person("Shashwat", 21 )
print(person)



# ======================================= Example ===============================================

@dataclass
class StepMeta:
    name: str
    fn: Callable[..., Any]
    retries: int = 0
    order: int = 0

def process_data(x):
    return x * 2

step = StepMeta(
    name="process",
    fn=process_data,
    retries=3,
    order=1
)

print(step.fn(10))