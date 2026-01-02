#self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class
class test:
    a=10
    def run(self):
        print("hi i am running")
obj = test()
print(obj.a)
obj.run()

class test2:
    a=10    #class attribute
    def __init__(self,name,age,loc):
        self.name=name #instance attribute
        self.age=age
        self.loc=loc
    def details(self): #instance method
        print(self.name , self.age , self.loc)
    @classmethod
    def mymethod(cls): #class method it donot point to the self it points to the class location 
        print("how are you")
    @staticmethod
    def staticmeth():
        print("hello this is static method")


obj1 = test2("anurag",20,"greater noida")
print(obj1.name)
print(obj1.age)
print(obj1.loc)
obj1.details()
    
obj2 = test2("sharma",23,"hyd")
print(obj2.name)
print(obj2.age)
print(obj2.loc)
obj2.details()

obj3=test2()
obj3.mymethod

obj4=test2()
obj4.staticmeth()