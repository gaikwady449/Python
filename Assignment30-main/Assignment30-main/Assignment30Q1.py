# count a lines in the File
# Problem sstatement
# write a program which accept a file name from the user and count how many lines present in the file 

def count_lines(FileName):

    try:
        with open(FileName,"r") as file:
            line_count = 0 
            for line in file:
                line_count += 1

        print("Number of lines in the file:",line_count)

    except:
        print("unable to open the file")
         

FileName=input("Enter a file name:")

count_lines(FileName)



    
