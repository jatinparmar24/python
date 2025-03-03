class Book:
    price=100
    totalpages=500
    def __init__(self,title,author):
        self.t=title
        self.a=author

    @classmethod
    def update(cls,newprice,newpagecount):
        cls.price=newprice
        cls.totalpages=newpagecount
    
    @classmethod
    def addnew(cls,author):
        cls.author2=author

    def show(self):
        print(self.t,self.a,Book.price,Book.totalpages)


obj=Book("python","jatin")
Book.update(110,550)
obj.show()