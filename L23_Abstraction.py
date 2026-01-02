from abc import ABC, abstractmethod
class a(ABC):
    @abstractmethod
    def catrun(self):
        pass
    @abstractmethod
    def dogrun(self):
        pass
class b(a):
    def allitems(self):
        print("all items method")
    def catrun(self):
        print("the cat is running by her 4 legs")
    def dogrun(self):
        print("the dog barks")
obj = b()
obj.allitems()




class ab(ABC):
    @abstractmethod
    def perimenter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class square(ab):
    def __init__(self,side):
        self.side=side
class circle(ab):
    def __init__(self,radius):
        self.radius=radius
    def perimenter(self):
        print("perimeter")
    def area(self):
        print("area")
obj = circle()
obj.area()
obj.perimenter()




from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def catrun(self, speed):
        pass
    @abstractmethod
    def dogrun(self, sound, times):
        pass
class B(A):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def allitems(self):
        print("all items method")
    def catrun(self, speed):
        print(f"The cat is running at {speed} km/h")
    def dogrun(self, sound, times):
        print(f"The dog {sound} {times} times owner name is {self.name}")
obj = B("anurag",23)
obj.allitems()
obj.catrun(20)
obj.dogrun("barks", 3)