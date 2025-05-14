import datetime

class LMS:
    def __init__(self, books_file, library_name):
        # Initialize the LMS with the list of books file and library name
        self.books_file = books_file  # File list of books
        self.library_name = library_name  # Library name
        self.books = {}  # Dictionary to hold book data
        book_number = 1001  # Starting book ID

        # Read the book list file and the books dict with books
        with open(self.books_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Read all lines 

        for one_line in lines:
            one_line = one_line.strip()  # Remove any space from each line
            if one_line:  # Skip blank lines
                self.books[str(book_number)] = {
                    "book_title": one_line,  # Title of the book
                    "lender_name": "",  # Lender name, 1st time empty
                    "issue_date": "",  # Issue date, 1st time empty
                    "status": "Available"  # 1st status is "Available"
                }
                book_number += 1

    def display_books(self):
        print("\n------ List of Books ------")
        # Adjust column alignment
        print(f"{'Book ID':<8} {'Title':<60} {'Status':<10}")  # Display header with aligned columns
        print("-" * 85)  # Separator line to match column widths

        for key in self.books:
            value = self.books[key]
            print(f"{key:<8} {value['book_title']:<60} {value['status']:<10}")  # Align Book ID, Title, and Status

    # Issue a book by updating its status 
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Addded current date and time

        if book_id in self.books:
            if self.books[book_id]["status"] != "Available":
                print(f"Book already issued to {self.books[book_id]['lender_name']} on {self.books[book_id]['issue_date']}")
            else:
                name = input("Enter your name: ")
                self.books[book_id]["lender_name"] = name
                self.books[book_id]["issue_date"] = current_time
                self.books[book_id]["status"] = "Issued"
                print("Book issued successfully.")  # Confirmation message
        else:
            print("Invalid Book ID!")  # Error message if the ID is not found

    # Add a new book to the library
    def add_book(self):
        new_book_title = input("Enter new book title: ").strip()
        if new_book_title == "":
            print("Book title cannot be empty.")
            return

        with open(self.books_file, "a", encoding='utf-8') as file:
            file.write(f"{new_book_title}\n")

        all_ids = list(self.books.keys())
        last_id = int(all_ids[-1])
        new_id = str(last_id + 1)

        self.books[new_id] = {
            "book_title": new_book_title,
            "lender_name": "",
            "issue_date": "",
            "status": "Available"
        }
        print(f"Book '{new_book_title}' added successfully with ID {new_id}.")

    # Return a book and mark it as available
    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        if book_id in self.books:
            if self.books[book_id]["status"] == "Available":
                print("Book is already available in the library.")
            else:
                self.books[book_id]["lender_name"] = ""
                self.books[book_id]["issue_date"] = ""
                self.books[book_id]["status"] = "Available"
                print("Book returned successfully.")  # greeting message
        else:
            print("Invalid Book ID!")

# Main Program execution
try:
    my_library = LMS("list_of_books.txt", "Python's Library")

    choice_menu = {
        "D": "Display Books", 
        "I": "Issue Book", 
        "A": "Add Book",  
        "R": "Return Book",  
        "Q": "Quit"  
    }

    while True:
        print(f"\n---- Welcome to {my_library.library_name} ----")
        for key in choice_menu:
            print(f"Press '{key}' to {choice_menu[key]}")

        user_choice = input("Enter your choice: ").upper()

        if user_choice == "D":
            my_library.display_books()
        elif user_choice == "I":
            my_library.issue_book()
        elif user_choice == "A":
            my_library.add_book()
        elif user_choice == "R":
            my_library.return_book()
        elif user_choice == "Q":
            print("Thanks for using the Library Management System!")
            break
        else:
            print("Invalid choice! Try again.")
except Exception as error:
    print("An error occurred:", error)
