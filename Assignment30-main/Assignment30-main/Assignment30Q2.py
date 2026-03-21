# Count the NUMBER of Words in the file
# problem statement
# write a program which accept a name of file from the user and count the number of word in the file 


def Count_Word(FileName):

    try:
        with open(FileName,"r",encoding="utf-8") as file:
            Word_count = 0
            for line in file:
                Word_count += len(line.split())

        print("Count the words in the file:",Word_count)

    except:
        print("unable to open the file")


FileName=input("Enter the name of the File:")

Count_Word(FileName)