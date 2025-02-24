def outerfun(fun1):
    def innerfun():
        print("Before Modification")
        fun1()
        print("After Modification")
    return innerfun

def fun():
    print("This is from main Function")

res=outerfun(fun)
res()