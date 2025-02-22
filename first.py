def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i=i+1
res=even(10)
x=next(res)
y=next(res)
z=next(res)
print(x,y,z)