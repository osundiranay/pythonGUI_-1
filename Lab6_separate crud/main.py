import tkinter as tk
from tkinter import messagebox
import create, read

def open_create():
    create.CreateStudent()

def open_read():
    read.ReadAllStudents()

app = tk.Tk()
app.title("Student CRUD")
app.geometry('400x300')

# Main buttons
tk.Button(app, text="Create Student", command=open_create, width=20).pack(pady=10)
tk.Button(app, text="View Students", command=open_read, width=20).pack(pady=10)

app.mainloop()
