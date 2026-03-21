# write program which accept N number of element from user and store it into a list return addition of all elemnt 
# from a list

N = int(input("Enter a number:"))
lst=[]
total=0

for i in range(N):
    num=int(input(f"Enter a element {i + 1}:"))
    lst.append(num)
    total += num

print("list of all element:",lst)
print("addition of all element:",total)
