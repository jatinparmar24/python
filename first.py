class School:
    '''School Details'''
    def __init__(self,name,roll,marks):
        self.a=name
        self.b=roll
        self.c=marks
    
    def addcity(self,city):
        self.d=city

    def show(self):
        print(self.a,self.b,self.c,self.d)

obj=School('jatin',101,90)
obj.addcity('sehore')
obj.show()
       



