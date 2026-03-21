# write a program which accept one number than print sum of digit

def sum(no):
    total=0
    while no> 0:
        digit= no % 10
        total += digit
        no //=10
    return total
x=int(input("Enter a number:"))
print("sum of all numbers:",sum(x))