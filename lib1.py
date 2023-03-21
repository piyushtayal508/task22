//hello simran
# we will store all books in our library in the following list.
books = []

# This function adds a new book into our library
def addBook():
    bookName = input('Enter book name: ')
    bookAuthor = input('Enter book author name: ')
    # book[0] = Book ID
    # book[1] = Book Name
    # book[2] = Book Author
    # book[3] = User name to whom book is issued
    book = [len(books) + 1, bookName, bookAuthor, '']
    books.append(book)
    print("\nBook added successfully")

# This function will delete a book from our library
def deleteBook():
    bookId = int(input('\nEnter ID of book to be deleted: '))
    idx = 0
    bookDeleted = False
    while idx < len(books):
        if books[idx][0] == bookId:
            print("Found book. Book ID: {}, Book name: {}, Book author: {}, Issued to: {}".format(books[idx][0], books[idx][1], books[idx][2], books[idx][3]))
            del books[idx]
            print("Book with ID: {} successfully deleted".format(bookId))
            bookDeleted = True
            break
        idx = idx + 1
    if bookDeleted == False:
        print("Invalid book ID. There is no book with ID: {}".format(bookId))

# This function lists all the books in our library
def listBooks():
    print('\nListing all books in library\n')
    if len(books) == 0:
        print("There are no books in the library")
    else:
        for book in books:
            print("Book ID: {}, name: {}, author: {}, Issued to: {}".format(book[0], book[1], book[2], book[3]))

# This function will issue a book to a user
def issueBook():
    bookFound = False

    bookId = int(input("Enter book ID to issue: "))
    for book in books:
        if book[0] == bookId:
            bookFound = True
            if len(book[3]) > 0:
                print("\nCannot issue as book with ID: {} is already issued to user: {}".format(bookId, book[3]))
                break
            else:
                userName = input("Enter name of user to whom to issue this book: ")
                book[3] = userName
                print("Book with ID: {} issued to user name: {}".format(bookId, userName))

    if bookFound == False:
        print('No book found with ID: {}'.format(bookId))

