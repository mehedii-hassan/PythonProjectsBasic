books=[]
books.append("c")
books.append("java")
books.append("python")
print(books)
books.pop()
books.pop()
print("Now the top book is : ",books[-1])
books.pop()
if not books:
    print("No books left")


