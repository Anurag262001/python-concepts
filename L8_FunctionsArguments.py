 #Required argument function
def course(coursename,time):
    print(coursename,time)
course("history","10")

#Default arguemnt
def greet(name="anurag"):
    print(name)
greet("Sharma")
greet() # if no value given then it will take default argument

#Keyword argument
def div(a,b):
    return a/b
result = div(b=10,a=20) #keyword argument
result = div(20,10) #positional argument 

#Arbitary Positional arguments
#if you r not sure how many arguments will be passed in that case we use *args
#The arguments are stored as Tuple
def addnum(*args):
    return sum(args)
_res = addnum(1,2,3,4,5,6,7,8,9)
print (_res)


#Arbitary Keyword argument(**kwargs)
#The argument are store as dictionary
def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
fun(name="anurag",agr=10,occupation="working")