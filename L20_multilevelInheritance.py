class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(B):
    def show(self):
        super().show()
        print("Class C")

obj = C()
obj.show()




class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips
        print(self.material,self.zips)
class BhopalFactory(Factory):
    def __init__(self,material,zips,items):
        super().__init__(material,zips)
        self.items = items
        print(self.items,self.zips,self.material)

class PuneFacotory(BhopalFactory):
    def __init__(self,material,zips,items,color):
        super().__init__(material,zips,items)
        self.color=color
        print(self.items,self.zips,self.material)
objectin=PuneFacotory("silicon","tight","coal","black")