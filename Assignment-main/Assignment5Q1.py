#write a program which accept length and width of rectangle and print area 

def CalArea(Length,width):
    Area=Length*width
    print("area is",Area)

x=int(input("Enter the Length:"))
Y=int(input("Enter the width:"))
CalArea(x,Y)