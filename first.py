n=int(input("Enter row"))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1

i=n
while i>=1:
    print('*'*i)
    i=i-1