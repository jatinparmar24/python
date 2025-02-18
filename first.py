str2=input("Enter = ")
capital=0
small=0
num=0

for x in str2:
    if x>=chr(65) and x<=chr(90):
        capital=capital+1

    elif x>=chr(97) and x<=chr(122):
        small=small+1

    elif int(x)>=0 and int(x)<=9:
        num=num+1
print("num = ",num , "small = ",small , "capital = ",capital)