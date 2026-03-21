# write a lambda funtion using filter() which accept list of numbers and return list of number 
# is divisible by 3 and 5


nums=[2,4,6,8,10,12,5,3,7]

Data=(list(filter(lambda x:x % 3 == 0,nums)))

print(Data)