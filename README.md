# library-management-system-
📚 A simple Library Management System in Python with book lending, returns, fines, and user registration.


##📚 Library Management System (Python)

A simple Library Management System built in Python using OOP (Object-Oriented Programming) concepts.<br>
This project allows users to register, borrow, return, search, and add books to the library.<br>
It also includes due date tracking and fine calculation for late returns.


## 🚀 Features

✅ Display Books – View all available books in the library<br>
✅ Search Book – Check if a book is available or already borrowed<br>
✅ Lend Book – Borrow a book with a 7-day due date<br>
✅ Return Book – Return borrowed books, with fine calculation for late returns<br>
✅ Add Book – Add new books to the library collection<br>
✅ User Registration – Register new users to the system<br>
✅ Validation – Only registered users can borrow books<br>

## 🛠️ Tech Used
Python 3 <br>
datetime module (to handle book lending dates and fines)<br>

## 📂 Project Structure
Library-System/<br>
│── library.py   # Main Python script with Library class and menu-driven interface<br>
│── README.md    # Project documentation<br>

## 📖 Example Menu
===== Library Menu ===== <br>
1. Display all books<br>
2. Search for a book<br>
3. Lend a book<br>
4. Return a book<br>
5. Add a book<br>
6. Register User<br>
7. Exit<br>

## 🖼️ Sample Output Screenshot
Here’s an example of how the program looks when running in the terminal: <br><br>
===== Library Menu =====<br>
1. Display all books<br>
2. Search for a book<br>
3. Lend a book<br>
4. Return a book<br>
5. Add a book<br>
6. Register User<br>
7. Exit<br>
Enter your choice: 1<br>
<br>
Available books are<br>
1. a<br>
2. b<br>
3. c<br>
4. d<br><br>

Enter your choice: 3<br>
Enter your name: John<br>
Access denied: 'John' is not a valid library user<br>
Registration needed to access the Library<br>
Do you want to register? (y/n): y<br>
User 'John' has been registered<br>
Enter book name to borrow: b<br>
Book 'b' has been lent to John until 2025-08-28<br>


## 🔮 Future Improvements

clean and optimize the code <br>
Add GUI version (Tkinter / PyQt)<br>
Store data in a database (SQLite/MySQL) instead of in-memory lists<br>
Add user login system with passwords<br>
Generate reports of borrowed/returned books<br>

## 🤝 Contributing

Pull requests are welcome!
If you’d like to contribute:<br><br>
Fork the repo<br>
Create a new branch (feature-xyz)<br>
Commit your changes<br>
Open a pull request<br>

## 📜 License
This project is open-source and available under the MIT License.<br>
