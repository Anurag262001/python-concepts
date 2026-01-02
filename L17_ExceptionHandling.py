""" 
try 
except 
else 
raise
finally

"""
a=int(input("enter the number you want to divide"))
try:
    print(10/a)
except ZeroDivisionError:
    print('you cannit divide it by zero')
else:
    print("number is good to divide by")



a=int(input("enter the number you want to divide"))
try:
    print(10/a)
except Exception as ex:
    print(f"you cannit divide it by zero {ex}")
else:
    print("number is good to divide by")
finally:
    print("i will run no matter what")


try:
    a=int(input("enter a num"))
    if(a<18):
        print("age is less than 18")
    else:
        print("you are good to go")
except ValueError as err:
    print(f"{err} pls enter in the form of number" )
finally:
    print("club will open soon") 



a=int(input("enter a num"))
try:
    if(a<18):
        raise ValueError("age is less than 18")
    else:
        print("you are good to go")
except Exception as err:
    print(f"{err} error occured" )
finally:
    print("club will open soon")