# Write a python program to implement a class named Bankaccount with the following requirement
#The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (init) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display()-displays account holder name and current balance
# Deposit()-accepts an amount from the user and adds it to balance
# Withdraw()-accepts an amount from the user and subtracts it from balance (
# Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest()-calculates and returns interest using formula:
# Interest (Amount ROI) / 100
# Create multiple objects and demonstrate all methods,

class BankAccount:
    ROI= 10.5
    
    def __init__(self,name,Amount):
        self.name = name
        self.Amount = Amount
        
    def Display(self):
        print("Account holder name:",self.name)
        print("Account Balance :",self.Amount)

    def Deposite(self):
        Depositeamount=int(input("Enter a Deposite Ammount:"))
        AfterDeposite= Depositeamount + self.Amount
        print("Account Balance:",AfterDeposite)

    def Withdraw(self):
        withdrawl=int(input("Enter  a Withdraw Amount:"))
        if withdrawl <= self.Amount:
          Afterwithdraw=self.Amount - withdrawl
          print("Account Balance:",Afterwithdraw)
        else: 
            print("Incufficient Bank Balnce")
    
    def Calculateintrest(self):
        intrest= self.Amount * BankAccount.ROI / 100
        print("Rate of interest is:",intrest)
    

c1=BankAccount("yash",50000)

c1.Display()
c1.Deposite()
c1.Withdraw()
c1.Calculateintrest()


          


