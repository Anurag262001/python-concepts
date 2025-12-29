#super with method
class a:
    def show(self):
        print("Parent class")
class b(a):
    def show(self):
        super().show()
        print("child class")
obj=b()
obj.show()


class y:
    a="pune"
    def show(self):
        print("hello this is from pune")
class x(y):
    def show(self):
        print(super().a)
OBJ=x()
OBJ.show()

#super with constructor
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calls Parent constructor
        print("Child constructor")
obj = Child()
 

#super with constructor variables
class emp:
    def __init__(self,name):
        self.name=name
        print(f"Employee name {self.name}")
class mang(emp):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(f"age is {self.age}")
objnew = mang("anurag",56)