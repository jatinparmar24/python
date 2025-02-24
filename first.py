def outerfun(fun1):
    def innerfun(r,s,t):
        r=r+10
        s=s+10
        t=t+10
        a=fun1(r,s,t)
        print(a)
       
    return innerfun


def fun(x,y,z):
    return x+y+z

res=outerfun(fun)
x=10
y=20
z=30
res(x,y,z)
fun(x,y,z)