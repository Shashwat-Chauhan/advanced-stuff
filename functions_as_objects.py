# In python a function is actually an object stored in memory.

def test_func():
    pass
print(type(test_func))

test_func.author = "Shashwat"
print(test_func.author)

# ==================================== Example ============================================

def prepare_pizza(order_id):
    print(f"Preparing Pizza for order {order_id}")
    print("Pizza ready!\n")

def prepare_burger(order_id):
    print(f"Preparing Burger for order {order_id}")
    print("Burger ready!\n")

def prepare_pasta(order_id):
    print(f"Preparing Pasta for order {order_id}")
    print("Pasta ready!\n")

def kitchen_manager(recipe_function , order_id):
    print("Order recieved by kitchen")
    recipe_function(order_id)
    print("Order sent for delivery \n")

menu = {
    "pizza": prepare_pizza,
    "burger": prepare_burger,
    "pasta" : prepare_pasta
}

def process_order(food_item , order_id):
    recipe = menu[food_item]

    if recipe:
        kitchen_manager(recipe, order_id)
    else:
        print("Item not available")
    

process_order("pizza", 101)
process_order("burger", 102)
process_order("pasta", 103)

# stored functions in a dictionary , passed them as arguments to another function 
# functions being treated as objects is why python supports decorators , callbacks , event systems