class A:
    x=10
    y=20

    def home(self):
        print("Home = ")

    def car(self):
        print("Car = ")

class B(A):
    def new(self):
        print("New Home")
  

obj=B()
obj.home()
obj.car()
obj.new()
print(A.x)
print(B.y)