# write a lambda funtion using which accept list return adition of all number using reduced()
from functools import reduce

nums=[2,4,6,8,10,12,5,3,7]

Data=reduce(lambda x,y:x+y,nums)

print(Data)