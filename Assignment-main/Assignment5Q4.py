# write a program which accept one number and print binary equivale

n = int(input("Enter the number:"))

if n == 0:
    print("binary equvivalent:0")
else:
    binary=" "

    while n > 0:
        binary=str(n % 2) + binary
        n= n // 2
        print("binary equivalent",binary)