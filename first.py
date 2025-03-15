def even(x):
    if x%2==0:
        return 'even'

    else :
        return 'odd'

li=[1,2,3,4,5,6,7,8,9,10]
res=map(even,li)
print(list(res))