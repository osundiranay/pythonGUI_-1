import tkinter as tk
import csv

class DeleteStudent:
    def __init__(self, index):
        self.index = index

        self.window = tk.Toplevel()
        self.window.title("Delete Student")
        
        # Setting a larger window size
        self.window.geometry("300x150")

        tk.Label(self.window, text="Are you sure you want to delete this student?").pack(pady=10)

        tk.Button(self.window, text="Yes", command=self.delete_student).pack(pady=5)
        tk.Button(self.window, text="No", command=self.window.destroy).pack(pady=5)

    def delete_student(self):
        with open("students.csv", mode="r") as file:
            students = list(csv.reader(file))

        students.pop(self.index)

        with open("students.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        tk.messagebox.showinfo("Success", "Student deleted successfully!")
        self.window.destroy()
