f=open("f1.txt","w")
f.write("hello this is my first file")
f.close()

f=open("f2.txt","w")
l=[45,2,3,4,5,6,7,88,9,9,5,43,3,5,56,7]
for num in l:
    f.write(str(num))
