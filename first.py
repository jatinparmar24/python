import functools

l1=['jatin','raj','abhishek','ajay','vikas']

def sum(x,y):
    if len(x)>len(y):
        return x

    else:
        return y
    
res=functools.reduce(sum,l1)
print(res)