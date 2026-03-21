# Display file line by line 
# problem statement
# Write a program which accept a file name from user and display the contents of the line by line on the screen 


def line_by_line(Filename):
    try:
        with open(Filename,"r") as file:
            for line in file:
                print(line,end=" ")

    except:
        print("Unable to open the file ")

Filename=input("Enter the Name of file")

line_by_line(Filename)
