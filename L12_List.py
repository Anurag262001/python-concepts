#ordered
#mutable
#indexed
#allow duplicate elements
fruits=["apple","apple",1,3.9,True]
print("apple" in fruits)
print(len(fruits))
print(fruits[2])
for x in fruits:
    print(x)
nestedList=[1,2,[3,4],True,[2,3,4,5]]
print(nestedList)

""" List Slicing """
#listname[Start:stop:step]
l=[1,2,3,4,5,6,7,8,9,9]
print(l[1:4]) #2,3,4
print(l[:3]) #1,2,3
print(l[2:]) #3,4,5,6,7,8,9
print(l[-3:]) #8,9,9

""" Methods """
l.append(40) #one element
l.extend([40,30]) #multiple element
l.insert(1,15) #insert an element at specific index
l.remove(4) #gives error if not found the element
l.pop() #removes last element as default
l.pop(5) #removes index 5 element, error if index is not present
l.clear() #empty the list
l.index(6) #gives the value of the specified index error if not found the index
l.count(5) #count the occurance of the value
l.sort() #it will sort on the bases
l.reverse()
l.copy() #creates the shallow copy of list
len(l) #gives the length of the list

#join two list we use + operator or append using loop 