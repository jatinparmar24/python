def use_decorator(func):
    def wrap():
        print(f"Starting :{func. __name__}:function")
        func()
        print("Completed")
    return wrap

@use_decorator
def first():
    print(" First Started")

@use_decorator
def second():
    print("Second Started")

first()
second()