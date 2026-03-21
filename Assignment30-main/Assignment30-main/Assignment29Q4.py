# compared to file (Command line )
# problem statement
# Write a program which accept two file through command line argument and comare the content of both file

  # if both file contains a same content display success
  # otherwise dispaly Failure



import sys 

def main():

    if len(sys.argv) != 3:
        print("Usage:python program.py <file1> <file2>")
        return 

    file1=sys.argv[1]
    file2=sys.argv[2]


    try:
        f1 = open(file1,"r")
        f2 = open(file2,"r")

        data1=f1.read()
        data2=f2.read()

        if data1 ==  data2 :
            print("success")

        else:
            print("Falure")


        f1.close()
        f2.close()

    except:
        print("source file does not exist")

if __name__ == "__main__":
    main()