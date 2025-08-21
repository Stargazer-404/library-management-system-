from datetime import datetime, timedelta

class Library:

    # constructor
    def __init__(self, listofbooks, library_valid_user_name):
        self.listofbooks = listofbooks
        self.library_valid_user_name = library_valid_user_name
        self.lendbooks = {}

    # functon to check valid user
    def validUser(self,nameofperson):
        if nameofperson not in self.library_valid_user_name:
            print(f"Access denirld: '{nameofperson}' is not a valid library user")
            print(f"Registration needed to access the Library")
            return False
        return True
        
    # function to create new user    
    def createUser(self, nameofperson):
        if nameofperson not in self.library_valid_user_name:
            self.library_valid_user_name.append(nameofperson)
            print(f"User '{nameofperson}' has been registered")
        else:
            print(f"User '{nameofperson}' is already registered")


    # Function to display books 
    def displayBook(self, nameofbook=None):
        if nameofbook:
            if nameofbook in self.listofbooks:
                print(f"The book '{nameofbook}' is Available")
            
            elif nameofbook in self.lendbooks:
                record = self.lendbooks[nameofbook]
                print(f"The book '{nameofbook}' is borrowed by {record['person']}, will be available on {record['due_date']}")
            
            else:
                print(f"The book '{nameofbook}' does not exist in the library records.")
            
        else:
            print("Available books are:")
            for i, book in enumerate(self.listofbooks):
                print(f"{i+1}. {book}")
        
    # Fucntion to lend books    
    def lendBook(self,nameofbook, nameofperson):

        if nameofbook in self.listofbooks:
            current_date = datetime.now()
            expired_date = current_date + timedelta(weeks = 1)
            print(f"Name of Book {nameofbook} -> Book lend to {nameofperson}")
                
            self.lendbooks[nameofbook] = {
                "person": nameofperson,
                "issue_date": current_date,
                "due_date": expired_date
            }
                
            # another way to update
            # self.lendbooks.update({
            #     nameofbook: {
            #     "person": nameofperson,
            #     "issue_date": current_date,
            #     "due_date": expired_date
            #     }
            # })


            self.listofbooks.remove(nameofbook)
            print(f"Book '{nameofbook}' has been lent to {nameofperson} until {expired_date.date()}")# here only date is shown like 12-4-2023 not the full formate in which it is stored(date,month,year,time)
        
        elif nameofbook in self.lendbooks:
            print(f"Sorry, '{nameofbook}' is already borrowed by {self.lendbooks[nameofbook]['person']} until {self.lendbooks[nameofbook]['due_date'].date()}")

        else:
            print(f"'{nameofbook}' does not exist in the library.")


    # ********Function to add book in library******* 
    # def addBook(self):
    #     print("Adding New Books to the library")
    #     print("To exit press 1")
    #     while True:
    #         book = input("--> ")
    #         if book != "1":
    #             self.listofbooks.append(book)
    #         else:
    #             break
    def addBook(self, book):
        self.listofbooks.append(book)
        print(f"Book '{book}' has been added to the library.")

    #       
    def returnBook(self,nameofbook, nameofperson):

        current_date = datetime.now()

        if nameofbook in self.lendbooks:
            record = self.lendbooks[nameofbook] 

            if record["person"] == nameofperson:

                if current_date <= record["due_date"]:

                    print(f"'{nameofbook}' returned on time by {nameofperson}.")
                    
                else:
                    fine_days = (current_date - record["due_date"]).days
                    print(f"'{nameofbook}' returned late by {nameofperson}. Fine = {fine_days * 100} Rs")

                # Put book back into library
                self.listofbooks.append(nameofbook)
                self.lendbooks.pop(nameofbook)

            else:
                print(f"'{nameofbook}' was not borrowed by {nameofperson}.")
        
        else:
            print(f"'{nameofbook}' is not recorded as borrowed.")



if __name__ == "__main__":
    listofbooks = ["a","b","c","d"]
    library_valid_user_name = ["1","2","3"]

    obj = Library(listofbooks, library_valid_user_name)  

    while True:
        print("\n===== Library Menu =====")
        print("1. Display all books")
        print("2. Search for a book")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Add a book")
        print("6. Register User")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            obj.displayBook()
        elif choice == "2":
            name = input("Enter the name of book")
            obj.displayBook(name)
        elif choice == "3":
            user = input("Enter your name: ")
            if not obj.validUser(user):
                register = input("Do you want to register? (y/n): ").lower()
                if register == "y":
                    obj.createUser(user)
                else:
                    continue
            book = input("Enter book name to borrow: ")
            obj.lendBook(book, user)
        elif choice == "4":
            user = input("Enter your name: ")
            book = input("Enter book name to return: ")
            obj.returnBook(book,user)
        elif choice =="5":
            book = input("Enter new book name: ")
            obj.addBook(book)
        elif choice == "6":
            user = input("Enter name to register: ")
            obj.createUser(user)
        elif choice == "7":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again")
