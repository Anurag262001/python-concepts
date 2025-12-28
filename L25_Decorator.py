def greetingsMethod(func): #we have capture the decorator fucntion  here func is the argument that holds the function greet step2
    def time(): #wrapper function if greet fucntion holds any arguments then we have to pass it here also step4
        print("time is evening")
        func()
        print("have a nice time")
    return time
@greetingsMethod  #this is decorator fucntion step1
def greet():
    print("greeting from anurag")
greet()


#decorator with known arguments
def sum(fun):
    def wrapper(a,b):
        print("wlcm sir")
        fun(a,b)
        print("hope you like the calc")
    return wrapper 
@sum
def a(a,b):
    print(f"the sum is {a+b}")
a(10,10)