def showdetail(**n):
    l=[]
    for v in n.values():
        l.append(v)
    return l

    
x=eval(input("Enter Key Value = "))
showdetail(**x)
