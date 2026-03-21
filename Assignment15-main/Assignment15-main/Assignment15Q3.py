# write a lambda funtion using which accept list return list of all odd number using filter()


nums=[2,4,6,8,10,12,5,3,7]

Data=(list(filter(lambda x:x % 2 != 0,nums)))

print(Data)