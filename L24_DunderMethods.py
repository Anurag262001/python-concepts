#when we pint the obj dunder method direclty access the __str__ method
#dunder method works on the object

class animal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"the animal is {self.name}"
obj = animal("lion")
print(obj)