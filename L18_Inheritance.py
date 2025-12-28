class a:
    name="anurag"
    def greet(self):
        print(f"good morning {a}")
class b(a):
    pass
obj=b() 
print(obj.name)
obj.greet()


class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"hi {self.name} your age is {self.age}")
class b(test):
    pass
bobj=b("anurag",24)
bobj.details()

