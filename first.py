x=10
def new():
    global y
    x=20
    y=30
    print("Enter global variable = ",globals()['x'])
    print("Enter local variable = ",x)
    print("Enter local variable = ",y)


new()
print(x)
print(y)