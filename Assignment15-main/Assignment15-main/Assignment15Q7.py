# write a lambda funtion using Filter() which accept a list of str and return list of string have length
#  is greter than 5


char=["yash","samadhan","vedika","ganesh"]

Data=(list(filter(lambda x: len(x) > 5 ,char)))

print(Data)