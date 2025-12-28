#private : cannot be accessed use __ starting of the attributes
#public  : can be accessed anywhere
#protected : same working as public. Use _ at the strting of the attributes or method name

# can access with out privte
class factory:
    a="pune"
    def show(self):
        print(self.a,"factory class")
class agra(factory):
    def show2(self):
        print(super().show(),super().a)
ab=agra()
ab.show2()

#cannot access with private
class factory:
    __a="pune"
    def show(self):
        print(self.__a,"factory class")
class agra(factory):
    def show2(self):
        print(super().show(),super().__a)
obj=agra()
obj.show2()


#cannot access 
class fac:
    __a="pune"
    def show(self):
        print(self.__a)
obj2 = fac()
obj2.show()


#we can access using the same class
class fac2:
    __A="agra"
    def run(self,ring):
        print(fac2.__A, ring)
xx=fac2()
xx.run("gold")
