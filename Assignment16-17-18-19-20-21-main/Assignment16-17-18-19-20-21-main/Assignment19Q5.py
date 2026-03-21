# write a program which contain filter(),map(),reduce(),in it python application which contain one list of number
#  list contain a number which is accepted from user.
# filter should filter of all prime number 
# map funtion shold multiply by 2 
# Reduce funtion should  return maximum number from that list

from functools import reduce 
num=[3,7,2,70,5,8,9,5]

is_prime=lambda n:n >1 and all(n % i  != 0 for i in range(2, int(n**0.5)+1))

primes=list(filter(is_prime,num))
print(primes)


Multiply=list(map(lambda x:x*2,primes))
print(Multiply)

Maximum_num =reduce(lambda x,y:x if x > y else y ,Multiply)
print(Maximum_num)