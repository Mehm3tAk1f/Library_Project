import csv
import pandas as pd
import regex as re
import tkinter as tk
from tkinter import messagebox, ttk

def main():
    root = tk.Tk()
    root.title("Library Management System")

    # Left Side Frames
    left_frame = ttk.Frame(root)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Right Side Frames
    right_frame = ttk.Frame(root)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Add Book Frame
    add_book_frame = ttk.LabelFrame(left_frame, text="Add Book")
    add_book_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(add_book_frame, text="Serial Number:").grid(row=0, column=0, padx=5, pady=5)
    serial_number_entry = ttk.Entry(add_book_frame)
    serial_number_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(add_book_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
    author_entry = ttk.Entry(add_book_frame)
    author_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(add_book_frame, text="Book Type:").grid(row=2, column=0, padx=5, pady=5)
    book_type_entry = ttk.Combobox(add_book_frame, values=["Fiction", "Non-Fiction", "Science Fiction", "Mystery", "Horror", "Romance", "Biography", "History", "Health", "Children"], width=17)
    book_type_entry.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(add_book_frame, text="Explanation:").grid(row=3, column=0, padx=5, pady=5)
    explanation_entry = ttk.Entry(add_book_frame)
    explanation_entry.grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(add_book_frame, text="Book Name:").grid(row=4, column=0, padx=5, pady=5)
    book_name_entry = ttk.Entry(add_book_frame)
    book_name_entry.grid(row=4, column=1, padx=5, pady=5)

    def add_book_command():
        serial_number = serial_number_entry.get()
        author = author_entry.get()
        book_type = book_type_entry.get()
        explanation = explanation_entry.get()
        book_name = book_name_entry.get()
        if add_book(serial_number, author, book_type, explanation, book_name):
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add book!")

    ttk.Button(add_book_frame, text="Add Book", command=add_book_command).grid(row=5, column=0, columnspan=2, pady=10)

    # Search Book by Serial Number Frame
    search_book_frame = ttk.LabelFrame(left_frame, text="Search Book by Serial Number")
    search_book_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(search_book_frame, text="Serial Number:").grid(row=0, column=0, padx=5, pady=5)
    search_serial_number_entry = ttk.Entry(search_book_frame)
    search_serial_number_entry.grid(row=0, column=1, padx=5, pady=5)

    def search_book_command():
        serial_number = search_serial_number_entry.get()
        book = search_book_with_serial_number(serial_number)
        if book:
            messagebox.showinfo("Book Found", f"Book Details: {book}")
        else:
            messagebox.showwarning("Not Found", "Book not found!")

    ttk.Button(search_book_frame, text="Search Book", command=search_book_command).grid(row=1, column=0, columnspan=2, pady=10)

    # Search Book by Author Name Frame
    search_author_frame = ttk.LabelFrame(left_frame, text="Search Book by Author Name")
    search_author_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(search_author_frame, text="Author Name:").grid(row=0, column=0, padx=5, pady=5)
    search_author_entry = ttk.Entry(search_author_frame)
    search_author_entry.grid(row=0, column=1, padx=5, pady=5)

    def search_author_command():
        author = search_author_entry.get()
        book = search_book_with_author_name(author)
        if book:
            messagebox.showinfo("Book Found", f"Book Details: {book}")
        else:
            messagebox.showwarning("Not Found", "Book not found!")

    ttk.Button(search_author_frame, text="Search Book", command=search_author_command).grid(row=1, column=0, columnspan=2, pady=10)

    # Show All Books Frame
    show_all_books_frame = ttk.LabelFrame(right_frame, text="All Books")
    show_all_books_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    books_listbox = tk.Listbox(show_all_books_frame, width=50)
    books_listbox.grid(row=0, column=0, padx=5, pady=5)

    def show_all_books_command():
        books_listbox.delete(0, tk.END)
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                books_listbox.insert(tk.END, row)

    ttk.Button(show_all_books_frame, text="Show All Books", command=show_all_books_command).grid(row=1, column=0, pady=10)

    # Who Has Book Frame
    who_has_book_frame = ttk.LabelFrame(right_frame, text="Who Has Book")
    who_has_book_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(who_has_book_frame, text="Book Name:").grid(row=0, column=0, padx=5, pady=5)
    who_has_book_book_name_entry = ttk.Entry(who_has_book_frame)
    who_has_book_book_name_entry.grid(row=0, column=1, padx=5, pady=5)

    def who_has_book_command():
        book_name = who_has_book_book_name_entry.get()
        result = who_has_book(book_name)
        messagebox.showinfo("Book Status", result)

    ttk.Button(who_has_book_frame, text="Check Book Status", command=who_has_book_command).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

#Adding a Book to Library.
def add_book(serial_number, author, book_type, explanation, book_name):
    with open('books.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, author, book_type, explanation, book_name, ","]) #comma is used to show that the book is available.
    return True

#Search a Book with its Serial number.
def search_book_with_serial_number(serial_number):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # first column is serial number
            if row[0] == serial_number:
                return row
        return None

#Search Books With Author Name.
def search_book_with_author_name(author):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # second column is author name
            if row[1].upper() == author.upper():
                return row
        return None

#Show all Books and their related Information.
def show_all_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def who_has_book(book_name):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4].upper() == book_name.upper():
                if row[5] == "": #if the book is available.
                    return "Book is available in the library."
                else:
                    #the name of the person who has the book.
                    student = book_to_owner(row[0])
                    return f"{row[4]} is with {student}."
        #any problems with the serial number.
        return "Book not found."
    
def book_to_owner(serial_number):
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == serial_number:
                return row[1]
            elif row[3] == serial_number:
                return row[1]
            elif row[4] == serial_number:
                return row[1]
        return False

if __name__ == "__main__":
    main()