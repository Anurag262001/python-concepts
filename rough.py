class test:
    a="anurag"
    b="sharma"
    def __init__(self,driver):
        self.driver=driver
    def run(self,name):
        print(self.a,name)
obj = test("chrome")
obj.run("running dog")

















































""" print("hello world")
a=5
print(a)
print("anurag sharma",a)
print("A"+"b") """
""" a="anurag"
b=(bool(a))
print (b)
print(type(b))
#why we use return, when to use when not 
#slicing
#.round .join
#list comprehension
#tuple comprehension
#set comprehension
#list element conver into capital coding_Question
#super 
#multiple inheritance no concept of interface, pyhton donot support method overloading """
""" #split --> string into list
print(name.split())
#string.upper() """

""" #The arguments are stored as Tuple
def addnum(*args):
    return sum(args)
_res = addnum(1,2,3,4,5,6,7,8,9)
print (_res)


#Arbitary Keyword argument(**kwargs)
#The argument are store as dictionary
def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
fun(name="anurag",agr=10,occupation="working") """