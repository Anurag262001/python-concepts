#Converting datatype value into another datatype
# Implicit: Automatically typecasting
x=1.9
y=5
print(type(x+y))

# Explicit: manually converting one data type into another using built-in functions
a = 26
res=str(26)  #--> int to str
print(type(res))
ab="24"
res2=int(ab)
print(type(res2))
# we can do convert 
#int to string
#string(numbers) to int
# float to int
# int to float
# float to string
# string(number) to float
#string to boolean ---> only true is conatin string, false if have empty string
#all will give true even space is count to be non empty
print(bool("False")) 
print(bool("True"))
print(bool("Hello"))
print(bool("0"))
print(bool(" "))


#tuple into list and vicevera
#we connot convert complex to init

a=5.9
print(int(a))  #5.9
print(round(a))#6

""" 
What errors occur in type casting?
ValueError
TypeError
"""