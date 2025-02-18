def sum(x,y,z):
    return x+y+z

l1=[2,3,4]
l2=[3,4,5]
l3=[4,5,6]

res=map(sum,l1,l2,l3)
print(list(res))