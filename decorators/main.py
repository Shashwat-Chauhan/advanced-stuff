import time

# A function that takes another function and returns a modified function.
# Decorators are used when we want to wrap a function with some other functionality , This wont change the main function's task / or when we want to perform some task before or after a function , 
# Hardcoding those tasks in every function would be repetitive , hence we use decorators


# ---------------------------------Example 1-----------------------------------------

def my_decorator(func):
    def wrapper():
        print("Before function completion")
        func()
        print("After function completion")
    
    return wrapper

@my_decorator 
# Internally =>   greet = my_decorator(greet)
def greet():
    print("Main task")

greet()

# ---------------------------------Example 2-----------------------------------------

def time_it(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start: .4f}s")
        return result
    return wrapper


@time_it
def heavy_task():
    time.sleep(1)

heavy_task()


# ---------------------------------Example 3-----------------------------------------


def log_calls(func):
    def wrapper(*args , **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args , **kwargs)
    return wrapper

# process_data = log_calls(process_data)
@log_calls
def process_data():
    print("Processing ...")
    return 

process_data()