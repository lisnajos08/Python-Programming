class publisher:
    def __init__(self):
        print ("parent class")
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)
class pyton(book):
    def __init__(self,price, pages):
        self.price=price
        self.pages=pages
    def display(self):
        print("The price of the book is ",self.price)
        print("Total pages of the book is ", self.pages)
c=book("Learning Python","khaled hussain")
c.display()
c=pyton(550,852)
c.display()