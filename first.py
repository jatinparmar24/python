n=input("Enter string")
l=len(n)
x=''
for i in range(l-1,-1,-1):
    x=x+n[i]
if n==x:
    print ("Pallindrom")
   
else:
    print("not")