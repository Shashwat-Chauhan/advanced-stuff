# A metaclass in Python is the class of a class.
# Just like:
# Objects are created from classes
# Classes are created from metaclasses

# In Python, the default metaclass is type.

# In Python, everything is an object, including classes.
# The default metaclass is `type`.

print(type(int))        # <class 'type'>
print(type(str))        # <class 'type'>
print(type(list))       # <class 'type'>
print(type(dict))       # <class 'type'>
print(type(object))     # <class 'type'>
print(type(type))       # <class 'type'>

# This means classes are objects, and they are created by the `type` metaclass.

class Person:
    pass

print(type(Person))


# You can actually create a class manually using type.


# class Person2:
#     name : "Shashwat"

# The above class is equivalent to the following:


Person2 = type(
    "Person2" , 
    (),
    {"name" : "Shashwat"}                                   
)

print(Person2.name)

# Explanation:

# type(class_name, parent_classes, attributes)
# Create a class called Person
# No parent classes
# Add attribute name


# ========================================================================================

# Python internally does:

# Person = type(
#     "Person",
#     (),
#     {"age": 21}
# )

# If you specify a metaclass:

# class Person(metaclass=MyMeta):

# Python does:

# Person = MyMeta(
#     "Person",
#     (),
#     {...attributes...}
# )


# ==================================== Example ============================================

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        print("Attributes:", attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    x = 10
    def greet(self):
        print("Hello")


# Output:
# Creating class: MyClass
# Attributes: {'__module__': '__main__', '__qualname__': 'MyClass', 'x': 10, 'greet': <function MyClass.greet at 0x...>}


class UpperAttrMeta(type):

    def __new__(cls, name, bases, attrs):

        new_attrs = {}

        for key, value in attrs.items():
            if not key.startswith("__"):
                new_attrs[key.upper()] = value
            else:
                new_attrs[key] = value

        return super().__new__(cls, name, bases, new_attrs)
        # This line creates the class object of the parent (type)
        # so it is equivalent to:
        # return type.__new__(cls, name, bases, new_attrs)
        

class Test(metaclass=UpperAttrMeta):
    name = "python"

t = Test()

print(t.NAME)