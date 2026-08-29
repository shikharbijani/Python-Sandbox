class Book():
    def __init__(self,author: str,title: str,year: int) -> None: #Book Strucutre
        self.author = author
        self.title = title
        self.year = year
        self.available=True

    def borrow_book(self) -> None:  #Validation and checking status of book (Borrow)
        if self.available:
            print(f"{self.title} Has Been Borrowed Successfully!")
            self.available=False
        else:
            print(f"{self.title} Is Already Borrowed")

    def return_book(self) -> None:  #Validation and checking status of book (Return)
        if not self.available:
            print(f"{self.title} Returned Successfully!")
            self.available=True
        else:
            print(f"Woah, We Already Have Our All Copies!")

    def __str__(self) -> str: #Formats printing of book object
        return f"{self.title} - {self.author}"

class Library():
    def __init__(self) -> None: #Makes an empty list to contains book objects
        self.books = []

    def add_book(self,book) -> None: #Add book objects to the list
        self.books.append(book)

    def view_books(self) -> None: #Prints All available book in Library
        for book in self.books:
            print(book)

    def find_book(self,book_name):  #Finds the books in Library
        for book in self.books:
            if book_name == book.title:
                return book



def main():
    book1=Book("Robert Greene","The Laws Of Human Nature",2018)
    book2=Book("Darius Foroux","Think Straight",2020)

    library=Library()
    library.add_book(book1)
    library.add_book(book2)
    found_book=library.find_book("The Laws Of Human")
    if found_book:                                              #Book is Found or not                                   
        if found_book.available:                                #Book is Found in Library check if it can be borrowed or not
            print(f"{found_book} available of borrowing!")     
        else:
            print(f"{found_book} not available for borrowing!")
    else:
        print("Book Not Found!")

if __name__=="__main__":
    main()
