#unordered no indexing
#no duplicate
#mutable(add or remove elements only)
#Elements Must Be Immutable (cannot replace)
#No Indexing / No Slicing
""" 
Supports Mathematical Set Operations
Union, Intersection, Difference, Symmetric Difference.
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # union
a & b   # intersection
a - b   # difference
a ^ b   # symmetric difference 
"""
#Empty Set Syntax: s = set()
#s=set([1,2,3,4,5,6])
s={1,2,3,4,5,6,7,"anurag"}
s.remove(7) #--> remove gives error if removing element is not in the set
print(s) #-->1,2,3,4,5,6,"anurag"

s.discard(3) #--> it will not throw any error
print(s)

s.pop()
s.clear()
s.update([5,6])
s.add("sharma")
print(s)
