
import tkinter as tk
from tkinter import messagebox

books = []

def add_book():
    book_id = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()

    books.append({"id": book_id, "title": title, "author": author, "available": True})
    messagebox.showinfo("Success", "Book Added")

def view_books():
    text_area.delete("1.0", tk.END)
    for book in books:
        text_area.insert(tk.END, str(book) + "\n")

def issue_book():
    book_id = entry_id.get()
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                messagebox.showinfo("Success", "Book Issued")
                return
            else:
                messagebox.showwarning("Warning", "Already Issued")
                return
    messagebox.showerror("Error", "Book Not Found")

def return_book():
    book_id = entry_id.get()
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            messagebox.showinfo("Success", "Book Returned")
            return
    messagebox.showerror("Error", "Book Not Found")

root = tk.Tk()
root.title("Library Management System")

tk.Label(root, text="Book ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Title").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Label(root, text="Author").pack()
entry_author = tk.Entry(root)
entry_author.pack()

tk.Button(root, text="Add Book", command=add_book).pack()
tk.Button(root, text="View Books", command=view_books).pack()
tk.Button(root, text="Issue Book", command=issue_book).pack()
tk.Button(root, text="Return Book", command=return_book).pack()

text_area = tk.Text(root)
text_area.pack()

root.mainloop()
