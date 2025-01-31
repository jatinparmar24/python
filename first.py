a=int(input("Enter 1st Number = "))
b=int(input("Enter 2nd Number = "))
c=int(input("Enter 3rd Number = "))


if (a==b and b==c ):
    print("a and  b and c are equal")

elif (a>b and a>c):
    print(f'{a} is greater')

elif (b>c and b>a):
     print(f'{b} is greater')

elif (c>a and c>b):
     print(f'{c} is greater')

elif (a==b ):
    print("a and  b are equal")


elif (b==c ):
    print("b and  c are equal")

elif (c==a ):
    print("c and  a are equal")






