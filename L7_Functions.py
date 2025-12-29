#function is a block of code that pefroms a specific task. you can use it whenever you want by calling its name,
#code readability and reusability
#built in function : print(), Type(), input() etc
#user defined function : coder creates 
""" 
def run(parameter,parameter):
    instruction1
    return result
run(arguments,agrument)   arguments are the values that are passed into function when it's called:
"""
a=2
b=10
def add(a,b):
    c=a+b
    return c
res=add(a,b)
print(res)

def add(y=90,x=10):
    return y+x
ress=add(80,80) #if 80,80 will not pass the it will take 90 and 10 as default
print(ress)

#pass function:- we use when we add the code later not now. 
def runs():
    pass
print("pass function")

