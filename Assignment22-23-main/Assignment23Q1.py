# Write a Python program to implement a class named BookStore with the following specifications:
# The class should contain two instance variables:
# Name (Book Name)
# Author (Book Author)
# The class should contain one class variable:
# NoOf Books (initialize it to 0)
# Define a constructor (init) that accepts Name and Author and initializes instance variables.
# Inside the constructor, increment the class variable NoOf Books by 1 whenever a new object is created.
# Implement an instance method:
# Display()-should display book details in the format: <BookName> by <Author>. No of books: <NoOfBooks>
# Example usage:
# Obj1 BookStore ("Linux System Programming", "Robert Love") Objl.Display()
#Linux System Programming by Robert Love. No of

class Bookstore:
    Noofbook= 0
    def __init__(self,name,author,):
        self.name= name
        self.author = author
        Bookstore.Noofbook += 1
    
    def dispaly(self):
        print("Book name:", self.name,"Book author:",self.author,"Noof book:",Bookstore.Noofbook)

obj1=Bookstore("linux system Proggraming","Robert Love")
obj1.dispaly()

obj2 = Bookstore("c programing","Dennis Ritchie")
obj2.dispaly()