# print('hello world')

class Book:
    def __init__(self ,title , author):
        self.title = title;
        self.author = author
    
    def fullBookName(self):
        return f"{self.title} by {self.author}"


myBook = Book("acha prhlo" , "qutaiba")

# print(myBook.fullBookName())


class Ebook(Book):
    def __init__(self , title , author, fileSize):
        super().__init__(title , author)
        self.fileSize = fileSize

myEbook = Ebook("prhlo bhai" , "abdullah" , "5mb")

print(myEbook.fullBookName())