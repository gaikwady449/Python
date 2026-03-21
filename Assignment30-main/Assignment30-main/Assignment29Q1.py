# Check file Exist in current Directory 
# problem statement 
# write a program which accept a file name from the user and checkwhether the that file exist in current directory or not 
import os
def main():
    Filename=(input("Enter the Name of the file:"))
    Ret= os.path.exists(Filename)
    if Ret == True:
        print("File is exist in dir")

    else:
        print("File does not exist ")

    

if __name__ == "__main__":
    main()