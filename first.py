a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.issuperset(y))
print(y.issuperset(x))

