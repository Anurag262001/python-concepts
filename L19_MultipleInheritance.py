#if in each class have same attributes then it will take the last child attribute
class a:
    name1="Anurag"
class b:
    name2="Sharma"
class c(a,b):
    name3="best"
obj = c()
print(obj.name1)

 
#the constructor function will be inherited of the first class that has been inherited. This is MRO(method resolution order)
class x:
    def __init__(self,name):
        self.name=name
class y:
    def __init__(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc

class z(x,y): #the constructor function will be inherited of the first class that has been inherited. This is MRO(method resolution order)
    print("hey")
obj=z("anurag")

class z(y,x): #the constructor function will be inherited of the first class that has been inherited. This is MRO(method resolution order)
    print("hey")
obj=z("anurag",23,"noida")