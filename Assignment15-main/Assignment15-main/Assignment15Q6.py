# write a lambda funtion  which accept list return minimum number from list reduced()
from functools import reduce

nums=[2,4,6,8,10,12,5,3,7]

Data=reduce(lambda x,y: x if x < y  else y , nums)

print(Data)