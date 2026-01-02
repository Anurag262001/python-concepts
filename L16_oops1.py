class L16_oops: #class
    a=1
    b=2
obj = L16_oops()
print(obj.a, obj.b) 
 
 
class a:
    x="pune"
    def show(self):
        print(f"hello {self.x}")
obj = a()
obj.show()
 

class L_16_oops:
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
    def studDetails(self): #method
        print("student name age is",self.name, self.age)
    def detail(self,carname,bikename):
        print(carname,bikename,self.name)
obj = L_16_oops("anurag",13)
print(obj.name,obj.age)
obj.studDetails()

obj2 = L_16_oops("ram",14)
obj2.studDetails()

obj.detail("bmw","bmw")


