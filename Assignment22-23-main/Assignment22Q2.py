# write a python program to implement class named circls with the follwing requirement
# The class should contain three instance variable redius Area and circumfarence 
# The class should contain one class variable named PI, initialized to 3.14.
#Define a constructor (init) that initializes all instance variables to 0.0.
#Implement the fellowing instance methods:
#CalculateArea() calculates the area of the circle and stores it in the Area variable.
#CalculateCircumference() calculates the circumference of the circle and stores it in the Circumference variable.
#Display()-displays the values of Radius, Area, and Circumference.
#Create multiple objects of the Circle class and invoke all the instance methods for each object


class Circle:
    PI= 3.14
    def __init__(self,):
        self.Radius=0.0
        self.area=0.0
        self.circumference=0.0
    def Accept(self):
        self.Radius=float(input("Enter  a Radius:"))

    def CalculateArea(self):
         self.area=Circle.PI * self.Radius * self.Radius


    def CalculateCircumfarance(self):
         self.circumference= 2 * Circle.PI * self.Radius

    def Dispaly(self):
        print("Radius:",self.Radius)
        print("area:",self.area)
        print("circumeference:",self.circumference)

        print("-----------------------------")


c1=Circle()
c2=Circle()

c1.Accept()
c1.CalculateArea()
c1.CalculateCircumfarance()
c1.Dispaly()


c2.Accept()
c2.CalculateArea()
c2.CalculateCircumfarance()
c2.Dispaly()