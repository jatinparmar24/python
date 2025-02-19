def finds(x):
    if len(x)<=3:
        return x

li=eval(input("Enter Your Name = "))
res=filter(finds,li)
print(list(res))