#write a lambda funtion which accept number return  true if it is odd

num = int(input("enter a number:"))

is_odd= lambda x: x % 2 != 0

print(is_odd(num))