class Book():
    def __init__(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year
    def get_book_info(self):
        return f"{self.name} - {self.author} - {self.year}"
class Library:
    def __init__(self):
        self.dictionary = {}
    def add_book(self):
        
            name = input("Book: ")
            if name in self.dictionary:
                print(f"This{name} have in dictionary")
            else:      
                author = input("Author: ")
                year = int(input("Year: "))
                self.dictionary[name] = Book(name,author,year)
                print(f"{name} - {author} - {year}")
         
    def remove_book(self):
            name = input("Input your book you want to delete: ")
            if name in self.dictionary:
                del self.dictionary[name]
                print(f"This {name} have to delete")
            else:
                print(f"this {name} not in dictionary")
        
    def find_book_by_author(self):
      
            author = input("Search by author: ")
            query = author.lower()
            found = False
            for book in self.dictionary.values():
                    if query in book.author.lower():
                        print(f"Found: {book.get_book_info()}")
                        found = True
            if not found:
                        print(f"{query} not in dictionary")
    def show(self):
      if not self.dictionary:
          print("Emty")
      else:
          for book in self.dictionary.values():
              print(book.get_book_info())

class App:
    def __init__(self) -> None:
        self.library = Library()
    def menu(self):
        while True:
            print("\n===== System of Library =====")
            print("1. Add book")
            print("2. Remove book")
            print("3. Find book by author")
            print("4. Show all books")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.library.add_book()
            elif choice == '2':
                self.library.remove_book()
            elif choice == '3':
                self.library.find_book_by_author()
            elif choice == '4':
                self.library.show()
            elif choice == '5':
                print("Exiting the library system. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")

App().menu()

        