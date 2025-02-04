n=int(input("Enter Any Number"))
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit**2
    n=n//10
print(sum)
print(n)