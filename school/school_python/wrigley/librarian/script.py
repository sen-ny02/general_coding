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

class Book:
    def __init__(self, author, title, isbn, isAvailable):
        self.__author = author
        self.__title = title
        self.__isbn = isbn
        self.__isAvailable = isAvailable
    
    def to_string(self):
        if self.__isAvailable == True:
            print(f"Book: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nAvailabile: Yes")
        else:
            print(f"Book: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__isbn}\nAvailabile: No")

def menu():
    print(f"What option would you like to do?:\n[1] List all books\n[2] Search for and checkout a book\n[3] Exit program")
    menu_select = int(input("Choose an option 1-3: "))

    exit = None
    if menu_select == 1 or menu_select == 2:
        exit == False
    elif menu_select == 3:
        exit == True
    return exit

display_menu = menu()
if display_menu == True:
    print("Yes")
else:
    print("No")