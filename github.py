# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:50:09 2024

@author: salih
"""

class Library:

    

    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")
        
    def __del__(self):
        self.file.close()
    
        
    def AddBook(self):
        title = input("enter title:")
        author = input("enter author:")
        release_year = input("enter release year:")
        num_of_page = input("enter number of page:")
        add_book=f"{title},{author},{release_year},{num_of_page}"
        self.file.write(add_book + "\n")
        print(f" {title}  added ")


        
    def ListBooks(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for x in books:
            book= x.split(',')
            print(f"Title: {book[0]}, Author: {book[1]}")
            
    def RemoveBook(self):
        title = input("Please enter the title of the book to be removed: ")
        books = self.file.readlines()
        self.file.seek(0)
        books_list = []
        found = False

        for book in books:
            if title not in book:
                books_list.append(book)
            else:
                found  = True

        if not found:
            print(f"{title} not found.")
        else:
            self.file.truncate(0)
            self.file.seek(0)
            for book in books_list:
                self.file.write(book)
            print(f" {title} removed ")
            
            
            
lib = Library()


while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("Enter number: ")

    if choice == '1':
        lib.ListBooks()
    elif choice == '2':
        lib.AddBook()
    elif choice == '3':
        lib.RemoveBook()
    elif choice == 'q':
        break
    else:
        print("Invalid number. Please enter a valid number.")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            