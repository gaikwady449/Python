# write a lambda funtion using Filter() which accept list of numbers and return count of even numbers

nums=[2,4,6,8,10,12,5,3,7]

product=len(list(filter(lambda x,:x % 2 == 0,nums)))


print(product)

