#immutable
#ordered
#indexed
#duplicate
color=("red","green",1,3.5)
print("red" in color)
color2=1,2,3,4,3,"anurag"
#using constructor 
color3=tuple(("apple","banana",1.5,5))
#single-item tuple
color4=("only",)

""" List Slicing """
#listname[Start:stop:step]
l=(1,2,3,4,5,6,7,8,9,9)
print(l[1:4]) #2,3)4
print(l[:3]) #1,2,3
print(l[2:]) #3,4,5,6,7,8,9
print(l[-3:]) #8,9,9

#join two tuple we use + operator or append using loop
#tuples has two method 1:count 2:index() other methods that can be used are len(), sorted()(After sorting tuple will act as list so we need to typecast back to tuple ), sum(l), min(l), max(l)

#packing tuple
a="A"
b=21
c="Eng"
packing = a,b,c
print(packing)
#unpacking
num,age,pro=packing
print(num)
print(age)
print(pro)