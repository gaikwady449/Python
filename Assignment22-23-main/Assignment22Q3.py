# Write a Python program to implement a class named Arithmetic with the follow characteristics:
# The class should contain two instance variables: Valuel and Value2.
# Define a constructor (init) that initializes all instance variables to 0
# Implement the following instance methods
# Accept()accepts values for Valuel and Value2 from the user.
# # Addition() returns the addition of Valuel and Value2.
# Subtraction()returns the subtraction of Valuel and Value2.
# Multiplication() returns the multiplication of Valuel and Value2.
# Division()-returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.


class Arithmatic:

    def __init__(self):
        self.Value1=0
        self.Value2=0
        self.Add=0
        self.sub=0
        self.Mul=1
        self.div=0

    def Accept(self):
        self.Value1=int(input("Enter a No1:"))
        self.Value2=int(input("Enter a No2:"))

    def Addition(self):
        self.Add=self.Value1 + self.Value2
        print("Addition of Number is:",self.Add)

    def subtraction(self):
        self.sub=self.Value1 - self.Value2
        print("Suntraction of number is:",self.sub)

    def Multiplication(self):
        self.Mul=self.Value1*self.Value2
        print("Multiplication if two number is :",self.Mul)

    def Division(self):
        self.div=self.Value1 % self.Value2
        print("DIvision of NUmber is:",self.div)


c1=Arithmatic()


c1.Accept()
c1.Addition()
c1.subtraction()
c1.Multiplication()
c1.Division()