# Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime()-returns True if the number is prime, otherwise returns False
# ChkPerfect()returns True if the number is perfect, otherwise returns False
# I Factors()-displays all factors of the number
# SumFactors()-returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.

class Number:

    def __init__(self,Value):
        self.Value=Value

    def Chkprime(self):
        if self.Value <= 1:
            return False
        for i in range (2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def Chkperfect(self):
        if self.Value <= 0 :
            return False
        s=0
        for i in range(1,self.Value):
            if self.Value % i == 0 :
                s += 1

        return s == self.Value
    
    def Factore(self):
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def sumofFactor(self):
        sum = 0
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                sum += i
                print(sum)
        
c1=Number(int(input("Enter a number:")))

print(c1.Chkprime())

print(c1.Chkperfect())

print(c1.Factore())

print(c1.sumofFactor())


