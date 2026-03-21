# write a program which contain filter(),map(),reduce(),in it python application which contain one list of number
#  list contain a number which is accepted from user. filter should filter out all such number which is even
#   map funtion will get square of that number 
# reduce will return addition of than number 

from functools import reduce 
num=[10,20,50,70,86,85,90,56]

Filter=list(filter(lambda x:x % 2 ==0,num))

print(num)
print(Filter)

MAp=list(map(lambda x:x**2,Filter))
print(MAp)

Reduce=reduce(lambda x,y: x+y,MAp)
print(Reduce)