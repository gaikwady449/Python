#write a program which accept  one number and print odd numbers till that number

def even(No):
     for i in range(10):
          if i % 2 != 0 :
               print(i)

x=int(input("Enter a number:"))
even(x)
