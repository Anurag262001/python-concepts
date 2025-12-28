name="anurag sharma is a good boy"
#slicing
print(name[0:2])
print(name[0:5:2]) #-->aua
print(name[::]) #--> get all the character
print(name[::-1])#--> reverse the character

#len(string)
print(len(name))

#string.count("")
print(name.count("a"))
#string.find("")-->gives you index number, if not found -1
print(name.find("a"))

#string.index("")-->gives you index number, if not found error
print(name.index("a"))

#split --> string into list
print(name.split())
#string.upper()

#string.replace(old,new)
print(name.replace("anurag","sharma"))
#string.lstrip()
print(name.lstrip())
#string.rstrip()
print(name.rstrip())
#string.strip()


print(name.upper())
#string.lower()
print(name.lower())

