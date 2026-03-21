# Copy the File Content into another file 
# problem statement 
# write a program which accept two file from user 
    # First file is existing file 
    # second file is new file 
# copy all content from first file into second file 

def copy_content(EXisting,NewFile):
    try:
        with open(EXisting,"r") as src:
            with open(NewFile,"w") as dest:
               for line in src:
                    dest.write(line)
        print("Content copy successfully")
    except:
        print("Unable to open file")

EXisting=input("Enter the name of source file:")
NewFile=input("Enter the new file:")

copy_content(EXisting,NewFile)