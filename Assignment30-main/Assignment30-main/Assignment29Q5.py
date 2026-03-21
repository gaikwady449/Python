# Frequency of sting in a File
# problem statement 
# write a program which accept a file name and one srting from the user and return the Frequency of that number
#  (count of occarance  ) of that sring in the file 

def count_string_in_file(Filename,search_string):
    try:
        file=open(Filename,"r")
        Data=file.read()
        file.close()
  

        count=Data.count(search_string)
        print("count of string is:",count)


    except:
        print("File does not exist")

Filename=input("Enter the name of file: ")
search_string=input("Enter the string :")

count_string_in_file(Filename,search_string,)

