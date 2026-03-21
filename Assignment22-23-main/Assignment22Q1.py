# Write a python program to implement a class named Demo with the follwing specification 
#The class should contain two instance variables: nol and no2.
#The class should contain one class variable named Value.
#Define a constructor (init) that accepts two parameters and initializes the instance variables.
#Implement two instance methods:
#Fun()-displays the values of instance variables nol and no2.
#Gun()displays the values of instance variables nol and no2.
#Create two objects of the Demo class as follows:
#obj1 Demo (11, 21)
#obj2 Demo (51, 101)
#Call the instance methods in the given sequence:


class Demo:
    def __init__(self,NO1,NO2):
        self.i=NO1
        self.j=NO2
    def fun(self):
        print("inside fun")
        print(self.i,self.j)

    def gun(self):
        print("inside Gun")
        print(self.i,self.j)

obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
