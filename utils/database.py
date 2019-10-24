#Concerned with the data management

books = []

def show_books():
    for book in books:
        print(f"{book['name']} by {book['author']}. Read: {book['read']}")

def add_book(name, author):
    book = {'name': name, 'author': author, 'read': False}
    books.append(book)

def delete_book(name, author):
    global books
    books = [book for book in books if book['name'] != name and book['author'] != author]

def read_book(name, author):
    for book in books:
        if book['name'] == name and book ['author'] == author:
            book['read'] = True

