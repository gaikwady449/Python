# write aprogram which contain one lambda funtion which accept one parameter and return power of two
#Ex input= 4 O/p= 16

power_of_two=lambda X:X**2

num=int(input("Enter a number:"))


result=power_of_two(num)
print("power of two is:",result)