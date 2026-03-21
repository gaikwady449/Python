#write a lambda funtion which accept number return  true if it is even

num = int(input("enter a number:"))

is_even= lambda x: x % 2 == 0

print(is_even(num))