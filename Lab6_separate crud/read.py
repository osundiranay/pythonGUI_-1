import tkinter as tk
import csv
import update, delete

class ReadAllStudents:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("All Students")
        
         # Setting a larger window size
        self.window.geometry("500x400")

        self.students = self.load_students()

        # Table header
        tk.Label(self.window, text="First Name", width=20, anchor="w").grid(row=0, column=0)
        tk.Label(self.window, text="Last Name", width=20, anchor="w").grid(row=0, column=1)
        tk.Label(self.window, text="Actions", width=20).grid(row=0, column=2)

        # Display students
        for i, student in enumerate(self.students):
            tk.Label(self.window, text=student[0], width=20, anchor="w").grid(row=i+1, column=0)
            tk.Label(self.window, text=student[1], width=20, anchor="w").grid(row=i+1, column=1)
            tk.Button(self.window, text="Edit", command=lambda i=i: self.edit_student(i)).grid(row=i+1, column=2)
            tk.Button(self.window, text="Delete", command=lambda i=i: self.delete_student(i)).grid(row=i+1, column=3)

    def load_students(self):
        try:
            with open("students.csv", mode="r") as file:
                return list(csv.reader(file))
        except FileNotFoundError:
            return []

    def edit_student(self, index):
        update.UpdateStudent(self.students[index], index)

    def delete_student(self, index):
        delete.DeleteStudent(index)
