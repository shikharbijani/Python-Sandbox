class Book():
    def __init__(self,author: str,title: str,year: int) -> None:
        self.author = author
        self.title = title
        self.year = year
        self.available=True

    def borrow_book(self) -> None:
        if self.available:
            print(f"{self.title} Has Been Borrowed Successfully!")
            self.available=False
        else:
            print(f"{self.title} Is Already Borrowed")

    def return_book(self) -> None:
        if not self.available:
            print(f"{self.title} Returned Successfully!")
            self.available=True
        else:
            print(f"Woah, We Already Have Our All Copies!")

    def __str__(self) -> None:
        return f"{self.title} - {self.author}"

class Library():
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)


def main():
    book1=Book("Robert Greene","The Laws Of Human Nature",2018)
    book2=Book("Darius Foroux","Think Straight",2020)
    library=Library()
    library.add_book(book1)
    library.add_book(book2)
    print(library.books)


if __name__=="__main__":
    main()
