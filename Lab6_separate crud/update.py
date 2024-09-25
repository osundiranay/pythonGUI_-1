import tkinter as tk
import csv

class UpdateStudent:
    def __init__(self, student, index):
        self.index = index
        self.student = student

        self.window = tk.Toplevel()
        self.window.title("Edit Student")
        
        # Setting a larger window size
        self.window.geometry("300x250")

        # Form fields
        tk.Label(self.window, text="First Name:").pack(pady=5)
        self.first_name = tk.Entry(self.window)
        self.first_name.pack(pady=5)
        self.first_name.insert(0, student[0])

        tk.Label(self.window, text="Last Name:").pack(pady=5)
        self.last_name = tk.Entry(self.window)
        self.last_name.pack(pady=5)
        self.last_name.insert(0, student[1])

        tk.Button(self.window, text="Update", command=self.update_student).pack(pady=10)

    def update_student(self):
        updated_first = self.first_name.get()
        updated_last = self.last_name.get()

        with open("students.csv", mode="r") as file:
            students = list(csv.reader(file))

        students[self.index] = [updated_first, updated_last]

        with open("students.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        tk.messagebox.showinfo("Success", "Student updated successfully!")
        self.window.destroy()
