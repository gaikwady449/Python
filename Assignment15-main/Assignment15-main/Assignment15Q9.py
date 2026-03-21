# write a lambda funtion using REDUCE() which accept list of numbers and return product of all number
from functools import reduce
nums=[2,4,6,8,10,12,5,3,7]

product=reduce(lambda x,y:x*y,nums,1)
print(product)

