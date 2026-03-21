#write a lambda funtion which accept number return  true if number is divisible by 5

num = int(input("enter a number:"))

is_divisible= lambda x: x % 5 == 0

print(is_divisible(num))