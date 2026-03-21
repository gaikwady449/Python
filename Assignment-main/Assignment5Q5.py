#write A PROGRAM WHICH ACCEPT A MARKS AND PRINT GRADE 

def Marks(num):
    if num >= 75:
        print("distinction")
    elif num >= 60:
        print("First class")
    elif num >= 50:
        print("second class")
    else:
        print("Fail")

x=int(input("Enter the marks:"))
Marks(x)
    
