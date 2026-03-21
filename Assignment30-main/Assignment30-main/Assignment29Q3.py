#n copy file content on new file (command line )
# problem statement
# write an program which accept an existing  file name through a command line argument . create new file named
# demo.txt and copy all thr content in thr demo.txt 
import sys 

def main():

    if len(sys.argv) != 2:
        print("Usage:python program.py <source_file>")
        return 

    src=sys.argv[1]
    dest="demo.txt"


    try:
        f1 = open(src,"r")
        f2 = open(dest,"w")


        data=f1.read()
        f2.write(data)

        print("File created demo.txt and content copied successfully")

        f1.close()
        f2.close()

    except:
        print("source file does not exist")

if __name__ == "__main__":
    main()