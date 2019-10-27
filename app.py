from utils import database
# Main menu


def show():
    books = database.show_books()
    for book in books:
        book_is_read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {book_is_read}")


def add():
    name = input("\nEnter the book's name: ")
    author = input("Enter the author's name: ")
    database.add_book(name, author)


def delete():
    name = input("\nEnter the book's name: ")
    author = input("Enter the author's name: ")
    database.delete_book(name)


def read():
    name = input("\nEnter the book's name: ")
    author = input("Enter the author's name: ")
    database.read_book(name, author)


menu_description = """
Welcome to your library!
Please select an option number and press Enter:
1.-Show your entire library
2.-Add a new book
3.-Delete a book
4.-Mark a book as read
5.-Exit
Your choose: """


def menu():
    database.create_table()
    option = int(input(menu_description))
    while option != 5:
        if option == 1:
            show()
        elif option == 2:
            add()
        elif option == 3:
            delete()
        elif option == 4:
            read()
        elif option < 1 or option > 5:
            print(f"{option} is not a valid option. Please select a valid option.")
        option = int(input(menu_description))


menu()
