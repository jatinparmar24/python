
class Parent:
    def home(self):
        print("parent class")

class Child1(Parent):
    def home(self):
        print("Child 1 class")
        super().home()

class Child2(Parent):
    def home(self):
        print("Child 2 class")

obj1=Child1()
obj1.home()
obj2=Child2()
obj2.home()