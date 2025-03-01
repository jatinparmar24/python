class Mobile:
    '''mobile name'''
    another="oppo"
    def __init__(self,name,comp):
        self.a=name
        self.s=comp
        print(Mobile.another)

    def addnew(self):
        x=2
        print("value of x",x)

    def show(self):
        print(self.a,self.s,Mobile.another)

obj=Mobile("apple","vivo")

obj.addnew()
obj.show()