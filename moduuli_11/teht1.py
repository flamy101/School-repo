
class publication_class:
    def __init__(self, name):
        self.name = name

class book(publication_class):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"Name: {self.name} | Author: {self.author} | Pages: {self.page_count}")

class magasine(publication_class):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        print(f"Name: {self.name} | Author: {self.editor}")





def main():
    new_book = book("Compartment No. 6", "Rosa Liksom", 192)
    new_magasine = magasine("Donald Duck", "Aki Hyyppä")

    new_book.print_info()
    new_magasine.print_info()

main()



