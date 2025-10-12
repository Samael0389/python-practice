books = []
while True:
    book = input("Enter a book title (type 'stop' to end: ")
    if book == 'stop':
        break
    books.append(book)
print ("Your reading list:")
for b in books:
    print(b)
print("Total books:", len(books))