# @dataclass
class test_Class_1:
    items : list = [] 

#  Now after understanding the issue of shared mutable , create this class without using dataclass



# Intuitively one would write this but this is wrong.
class Test_class_2:
    def __init__(self , items = []):
        self.items = items
    
o1 = Test_class_2()
o2 = Test_class_2()
o1.items.append("test_item")

# Both objects share the same list , this is a bug , every object should contain its own list.


# Correct way
class Test_class_3:
    def __init__(self , items = None):
        if items is None:
            self.items = []
        else:
            self.items = items

o3 = Test_class_3()
o4 = Test_class_3()

o3.items.append("test_item")
print(o3.items, o4.items)
o5 = Test_class_3(["test_item1" , "test_item2"])
print(o5.items)