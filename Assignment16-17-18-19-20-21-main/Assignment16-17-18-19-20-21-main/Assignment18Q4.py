# write a programm which accept N number from user and store it into list accept a another number and return 
# frequency of that number in a list 

N = int(input("Enter a number:"))
N1= int(input("Enter a number"))
lst = []


for i in range(N):
    num=int(input(f"enter a element: { i + 1} "))
    lst.append(num)
print(lst)

search=int(input("Enter a  number to find frequency:"))

Frequancy= lst.count(search)

print("frequancy of",search,"is:",Frequancy)
        
