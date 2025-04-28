import json

class library:
    def __init__(self):
        self.filename = 'library_data.json'
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except:
            self.data = {"available_books": [], "borrowed_books": {}}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_book(self, book):
        self.data["available_books"].append(book)
        
        self.save_data()

    def borrow_book(self, student, book):
        if book in self.data["available_books"]:
            self.data["available_books"].remove(book)
            self.data["borrowed_books"][book] = student
            self.save_data()
            print(f"{book} borrowed by '{student}'.")
        else:
            print(f"'{book}' is not available.")

    def return_book(self, student):
        found = False
        for book, borrower in list(self.data["borrowed_books"].items()):
            if borrower == student:
                found = True
                self.data["borrowed_books"].pop(book)
                self.data["available_books"].append(book)
                self.save_data()
                print(f"{student} returned '{book}'.")
                break
        if not found:
            print(f"{student} has not borrowed any book.")

library = library()

def menu():
    while True:
        print("\n*=-=-=-library menu-=-=-=*")
        print("\npress 1 for add book.")
        print("press 2 for borrow book.")
        print("press 3 for return book.")
        print("press 0 for exit.")
        
        option = input("\nplease select your option:- ")

        if option == '1':
            book = input("please enter the book name:- ")
            library.add_book(book)
            print(f"book '{book}' added successfully.")

        elif option == '2':
            name = input("please enter your name:- ")
            book = input("please enter the book to borrow:- ")
            library.borrow_book(name, book)

        elif option == '3':
            name = input("please enter your name to return book:- ")
            library.return_book(name)

        elif option == '0':
            print("Exit.")
            break

        else:
            print("invalid option! please select the correct option.")
menu()
