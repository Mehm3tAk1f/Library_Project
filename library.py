import csv
import pandas as pd
import regex as re

def main():
    print("Hello World!")


#Adding a Book to Library.
def add_book(serial_number, author, book_type, explanation, book_name):
    with open('books.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, author, book_type, explanation, book_name, ","]) #comma is used to show that the book is available.

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
            if row[1] == author:
                return row
        return None


#Show all Books and their related Information.
def show_all_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

#Registering a Student.
def register_student(student_id, student_name):
    # check if student is already registered
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                print("Student is already registered")
                return

    # id validation (id needs to be 3 numbers, 3 letters, and 3 numbers) with regex
    pattern = r"^\d{3}[A-Za-z]{3}\d{3}$"
    if bool(re.match(pattern, student_id)) == False:
        print("Invalid student ID")
        return

    # name validation (name needs to be 2 words with only letters) with regex
    pattern = r"^[A-Za-z]+ [A-Za-z]+$"
    if bool(re.match(pattern, student_name)) == False:
        print("Invalid student name")
        return
    
    with open('students.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, student_name, "", "", ""]) # 3 empty books
    

#Show All Registered Students.
def show_students():
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

#Students can Check Out the Book From the Library (if registered).
#Students can not Check Out max than 3 Books
#You can only borrow a Book If it is Available in the Library
def check_out_book(student_id, serial_number):
# it is easier to implement this by using the Pandas library since we are editing the csv file
    book_csv = pd.read_csv('books.csv')
    student_csv = pd.read_csv('students.csv')

    # check if student is registered
    student_row = student_csv[student_csv['Student ID'] == student_id] # get the row of the student
    if student_row.empty:
        print("Student is not registered")
        return

    # check if book is available  
    book_row = book_csv[book_csv['Serial Number'] == serial_number] # get the row of the book
    if book_row.empty:
        print("Book is not available")
        return


    # check if student has already checked out 3 books
    if student_row['Book 3'].values[0] != "":
        print("Student has already checked out 3 books")
        return
    
    # check out the book (needs to be improved)
    if student_row['Book 1'].values[0] == "":
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 1'] = serial_number
    elif student_row['Book 2'].values[0] == "":
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 2'] = serial_number
    elif student_row['Book 3'].values[0] == "":
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 3'] = serial_number

    # mark the book as checked out
    book_csv.loc[book_csv['Serial Number'] == serial_number, 'Available(empty if yes)'] = student_row['student_id'].values[0]

    # save the changes
    book_csv.to_csv('books.csv', index=False)
    student_csv.to_csv('students.csv', index=False)
    return True





#Students can Check In the Book at the Library.
#You can also see the Books which a Student has Checked Out(only while checking in)
def check_in_book(student_id, serial_number):
    book_csv = pd.read_csv('books.csv')
    student_csv = pd.read_csv('students.csv')

    # check if student is registered
    student_row = student_csv[student_csv['Student ID'] == student_id] # get the row of the student
    if student_row.empty:
        print("Student is not registered")
        return

    # check if serial number is valid
    book_row = book_csv[book_csv['Serial Number'] == serial_number] # get the row of the book
    if book_row.empty:
        print("Book is not available")
        return

    # check if student has checked out this book
    if student_row['Book 1'].values[0] != serial_number or student_row['Book 2'].values[0] != serial_number or student_row['Book 3'].values[0] != serial_number:
        print("Student has not checked out this book")
        return

    # check in the book (needs to be improved)
    if student_row['Book 1'].values[0] == serial_number:
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 1'] = ""
    elif student_row['Book 2'].values[0] == serial_number:
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 2'] = ""
    elif student_row['Book 3'].values[0] == serial_number:
        student_csv.loc[student_csv['Student ID'] == student_id, 'Book 3'] = ""

    # mark the book as checked in
    book_csv.loc[book_csv['Serial Number'] == serial_number, 'Available(empty if yes)'] = ""

    # save the changes
    book_csv.to_csv('books.csv', index=False)
    student_csv.to_csv('students.csv', index=False)
    return True







if __name__ == "__main__":
    main()