# write a program which contain filter(),map(),reduce(),in it python application which contain one list of number
#  list contain a number which is accepted from user. filter should filter out all such number which greater
#  than equal to 70 and less than equal to 90. map funtion will increase by 10 reduce can 
# return product of all number 

from functools import reduce 
num=[10,20,50,70,86,85,90,56]

Filter=list(filter(lambda x:x >= 70 and  x <= 90,num))

print(num)
print(Filter)

MAp=list(map(lambda x:x+10,Filter))
print(MAp)

Reduce=reduce(lambda x,y: x*2 + y*2 ,MAp)
print(Reduce)