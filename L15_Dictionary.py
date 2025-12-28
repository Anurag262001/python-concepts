#key must be unique, value can be same
#ordered
#using dict constructor
#using list of tuples
a={
    "a":1,
    "b":"sharma",
    2:"anurag"
}
#access
print(a["a"])   #if there is no such key then it will return as an error

#methods
print(a.keys())    #retrun as view object
print(a.values())  #retrun as view object
print(a.items())   #retrun as view object
print(a.get("b"))  #if dont have that key it will return none
a["new"]="anurag sharma" #adding key value pair
a["b"]="B" #modify
del a[2]
a.pop("b")

#looping
for key in a:
    print(key)
for value in a:
    print(a[value])
for value in a.values():
    print(value)
for key, value in a.items():
    print(key,value)