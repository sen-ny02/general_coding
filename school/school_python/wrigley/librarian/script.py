'''
Class Construction: Write the Book class. Ensure you have a constructor (__init__) and a method to display the book's details nicely (e.g., toString() or __str__).

Class construction: Write the ProjectLibrarian class that holds the Main method, the menu and the other associated methods.

File Reading: Write a function loadBooks() that reads books.txt.

    Tip: Watch out for the "newline" character (\n) at the end of lines!

Main Loop: Create a menu system (using a while loop) that asks the user to:

    [1] List all books.
    [2] Search for and check out a book.
    [3] Exit.

Text file: Create the text file for the project. See above for the contents. 
'''
def get_info():
    books = []
    with open("books.txt", "r") as f:
        #removes unnecesary shit
        for line in f:
            line = line.strip()

            #skips if no line so no dumbass error
            if not line:
                continue

            #splits parts with the comma as splitter
            parts = line.split(",")

            #ez error handling
            if len(parts) != 3:
                print("Invalid line: ", line)
                continue

            #assigns parts to shit
            title, author, isbn = parts
            books.append((title, author, isbn))
    
    return books

class Book:
    def __init__(self, title, author, isbn):
        self.__author = author
        self.__title = title
        self.__isbn = isbn
        self.__isAvailable = True #default state

    

    def check_out(self):
        if self.__isAvailable:
            self.__isAvailable = False
            return True
        else:
            return False
    
    def to_string(self):
        if self.__isAvailable == True:
            return f"Book: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nAvailabile: Yes"
        else:
            return f"Book: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nAvailabile: No"
    
    def __str__(self):
        return self.to_string()


library_list = []
books = get_info()
for title, author, isbn in books:
    new_book = Book(title, author, isbn)
    library_list.append(new_book)

for book in library_list:
    print(book)
    print()