# Disign a python application that create two thread 
# Thread 1 should comput sum of all  element from a list
# Thread 2 should comput  product of element from list 
# return the result to the main thread and display

def sum(lst):
    total=0
    for num in lst:
        total += num
    print("sum of all element:",total)

def product(lst):
    product = 1
    for num in lst:
        product *= num
    print("product of all number:",product)



    

lst=list(map(int,input("Enter a integer:").split()))

print(sum(lst))
print(product(lst))