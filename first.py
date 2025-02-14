def showdetail(**n):
    l=[]
    for v in n.value():
        l.append(v)
    return l

    
x=eval(input("Enter Key Value = "))
res=showdetail(**x)
print(res)

