# wap a progamm which accept one num ans print reverse of num

def reverse(num):
    rev=0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //=10
    return rev
n = int(input("Enter a number:"))
print("reverse num is :",reverse(n))