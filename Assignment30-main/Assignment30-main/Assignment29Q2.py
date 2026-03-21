# Display the file contents
# problem statement 
# write a program which accept Filename from user open thet file and dispalay the entire content on the console 
import os
def main():
    try:
        fname=input("Enter name of file:")
        fobj=open(fname,"r")

        print("File get succsesfully open")
        
        Data=fobj.read()

        print("Data from file is:",Data)

        fobj.close()

    except:
        print("unable to open such file as thre is no such file ")

    
    finally:
        print("end of application")
        fobj.close()

if __name__ == "__main__":
    main()