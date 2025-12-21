class Book():
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' by {self.author}"
    
    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"The book '{self.title}' is being deleted.")
    

myBook = Book("1984", "George Orwell", 328)
print(myBook)    #This will call the __str__ method
print(myBook.get_info())
print(len(myBook))  #This will call the __len__ method

del myBook  #This will delete the myBook instance
#print(myBook)  #This will raise an error because myBook has been deleted

myBook = Book("2022", "Abhijeet Kulshreshtha", 400)
print(myBook)    #This will call the __str__ method
print(myBook.get_info())
print(len(myBook))  #This will call the __len__ method