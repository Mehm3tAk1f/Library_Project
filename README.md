# Library_Project
This project is a Library Management System implemented using Python and Tkinter for the GUI. It allows users to manage a library's book inventory with functionalities such as adding books, searching books by serial number or author name, displaying all books, and checking the status of a book. The data is stored in CSV files. Here are the key features and functionalities:

Add Book:
- Users can add a new book to the library by entering details such as serial number, author, book type, explanation, and book name.
- The book details are saved in a CSV file (books.csv).

Search Book by Serial Number:
- Users can search for a book using its serial number.
- If the book is found, its details are displayed in a message box.

Search Book by Author Name:
- Users can search for books by entering the author's name.
- If a book by the specified author is found, its details are displayed in a message box.

Show All Books:
- Users can view a list of all books available in the library.
- The book details are read from the books.csv file and displayed in a listbox.

Check Who Has a Book:
- Users can check the status of a book by entering its name.
- The system checks if the book is available or with a student and displays the relevant information.
  
The project uses CSV files (books.csv and students.csv) to store book and student information. The GUI is built using Tkinter, with various frames and widgets to facilitate user interaction. The main functionalities are implemented through functions that handle file operations and data retrieval.
