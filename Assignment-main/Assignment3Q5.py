# wap a progamm which accept one num check it is palindromr

def is_palindrome(num):
    temp=0
    rev=0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //=10
    if temp == rev:
        return True
    else:
        return False

n = int(input("Enter a number:"))

if is_palindrome(n):
    print("is palindrome")
else:
    print("not a palindrome")