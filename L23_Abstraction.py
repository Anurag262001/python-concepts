from abc import ABC, abstractmethod
""" class a(ABC):
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
obj.allitems() """

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
