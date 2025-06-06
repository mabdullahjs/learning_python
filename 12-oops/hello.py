# print('hello world')

class Book:
    total_books = 0
    def __init__(self ,title , author):
        self.__title = title;
        self.__author = author
        Book.total_books += 1

    def get_title (self):
        return self.__title + "!"
    
    def fullBookName(self):
        return f"{self.__title} by {self.__author}"
    def reading_format(self):
        return "printed book"
    
    @staticmethod
    def general_Description():
        return "books are for reading"
    
    @property
    def get_author(self):
        return self.__author



# print(myBook.fullBookName())


class Ebook(Book):
    def __init__(self , title , author, fileSize):
        super().__init__(title , author)
        self.fileSize = fileSize
    
    def reading_format(self):
        return "digital book"
    
    



# myBook = Book("acha prhlo" , "qutaiba")
myEbook = Ebook("prhlo bhai" , "abdullah" , "5mb")
# my_second_book = Book("rehna do" , "abdullah")

# print(myEbook.fullBookName())
# print(myEbook.general_Description())
# print(Book.total_books)
# print(Book.general_Description())

# myBook.author = "updated abdullah"

# print(myBook.get_author)

# print(isinstance(myEbook , Book))
# print(isinstance(myEbook , Ebook))