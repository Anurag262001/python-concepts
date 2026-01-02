#List comprehension is a short and clean way to create a list from another list, string, range, etc.


#square of the elements in the list
a=[1,2,3,4,5,6]
print([a*a for a in a])

#only even elements 
nms=[2,5,4,7,8,9,5,6,7,3,4]
print([even for even in nms if even % 2 ==0])

#with if-elif 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#string comprehension
s = "python"
chars = [c for c in s]
print(chars)

#count vowel
s="automation"
vowels=[vo for vo in s if vo in "aieou"]

#set comprehension 
s = {x * x for x in range(5)}
print(s)