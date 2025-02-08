x=int(input("Enter First Number = "))
y=int(input("Enter Second Number = "))
maxN=max(x,y)

while True:
    if maxN%x==0 and maxN%y==0:
        break
    maxN=maxN+1
print(f'LCM of {x} and {y} is = {maxN}')
