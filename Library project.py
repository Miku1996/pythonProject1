class Library:
    def __init__(self,booklist):
        self.books=booklist

    def displayavailablebooks(self):
        print("The books available is:- ")
        for book in self.books:
            print(" * ",book)

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname} .Please return it withnin 30 days")
            self.books.remove(bookname)
        else:
            print("Sorry this book is not available it is out of stock.Please wait till some one returns it")

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("thank you for returning this book")

class Student:

    def borrowbook(self):
        self.book=input("enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book=input("enter the book you want to return or you want to donate to library: ")
        return self.book

if __name__ == '__main__':
    centrallibrary = Library(["Arithmetic","Algorithm","C++","Html","Django","Java","Python"])
    centrallibrary.displayavailablebooks()
    student =Student()
    while True:
        welcomemsg="""
====== Welcome to Book Library ======
    Choose what to do
    1.Display book list
    2.Request a book
    3.Add/Return a book
    4.Exit from Library
    """
        print(welcomemsg)
        a=int(input("Enter choice: "))
        if a == 1:
            centrallibrary.displayavailablebooks()
        elif a==2:
            centrallibrary.borrowbook(student.borrowbook())
        elif a==3:
            centrallibrary.returnBook(student.returnBook())
        elif a==4:
            print("thank you for using this. have a great day ahead! ")
            exit()
        else:
            print("incorrect choice Please choose within option")

