# field() is a helper function used inside a @dataclass to customize how a particular attribute behaves.
from dataclasses import dataclass, field
import uuid


@dataclass
class Order: 
    id : int 
    items : list = field(default_factory=list)

# Why default_factory?
# Used when the default value should be a new object each time 
# Because mutable objects like lists should not be shared.

# @dataclass
# class test_Class_1:
#     items : list = [] 

# o1 = test_Class_1(1)
# o2 = test_Class_1(2)
# o1.items.append("test_item")

# print(o1.items , o2.items) 


# This will print "test_item , test_item" , but code wont run because the items : list = [] line will throw an error , as python internally recognizes the issue and wont allow you to create a shared object.


# Example 3 — init=False
# Prevents a field from appearing in the constructor.
# Example:


@dataclass
class User:
    name: str
    age: int
    id: str = field(init=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

# Usage:

u = User("Alice", 25)
print(u)

# Output:

# User(name='Alice', age=25, id='random-uuid')

# User cannot pass id manually.
# This is useful for:
# database ids
# timestamps
# generated values


# Example 4 — repr=False
# Controls whether a field appears in __repr__.
# Example:

@dataclass
class Account:
    username: str
    password: str = field(repr=False)

# Usage:

a = Account("admin", "secret123")
print(a)

# Output:

# Account(username='admin')

# Password is hidden.
# Very useful for:
# passwords
# API keys
# secrets


# Example 5 — compare=False
# Controls whether the field participates in comparisons.

# Example:

@dataclass
class Student:
    name: str
    marks: int
    cache: dict = field(default_factory=dict, compare=False)

# Now:

s1 = Student("Alice", 90 , "asdasd")
s2 = Student("Alice", 90, "asdasdasdasdasdas")
s3 = Student("Alice" , 90 )
print(s1 == s2 == s3) 
print(s1)
print(s3)

# Output
# True
# Even if cache differs, comparison ignores it.
# Useful for:
# internal caches
# temporary data