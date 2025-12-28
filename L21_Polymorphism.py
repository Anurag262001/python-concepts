class a:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def run(self,loc):
        print(f"hello I'm {self.name} I live in {self.address} and my loc is {loc}")

class b(a):
    def run(self):
        print("b is running")

obj = a("anurag","3490")
obj.run("delhi")

obj2 = b("sharma","3455")
obj2.run()



class x:
    def show(self):
        print("hello this is class x")
class y(x):
    def show(self):
        print("this is class y")
he=y()
he.show()
he2=x()
he2.show()