class Parent1:
    z=12
    def home(self):
        print("Parent's 1  property")

class Parent2:
    y=122
    def home(self):
        print("Parent's 2  property")

class Child(Parent1,Parent2):
    def car(self):
        print("Child's car")

obj=Child()
obj.home()

  