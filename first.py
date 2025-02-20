x=lambda p,q:[r for r in range(p) for i in range(q)]
p=int(input("Enter Number of Collection required = "))
q=int(input("Enter Number of times to repeat collection = "))
print(x(p,q))