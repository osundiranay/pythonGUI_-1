import tkinter as tk
import csv

class CreateStudent:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Add Student")

        # Setting a slightly larger window size
        self.window.geometry("300x250")

        # Form fields with more padding around components
        tk.Label(self.window, text="First Name:", anchor="w").pack(padx=20, pady=10)
        self.first_name = tk.Entry(self.window, width=30)
        self.first_name.pack(padx=20, pady=5)

        tk.Label(self.window, text="Last Name:", anchor="w").pack(padx=20, pady=10)
        self.last_name = tk.Entry(self.window, width=30)
        self.last_name.pack(padx=20, pady=5)

        tk.Button(self.window, text="Submit", command=self.save_student, width=15).pack(pady=20)

    def save_student(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()

        if first_name and last_name:
            with open("students.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([first_name, last_name])
            tk.messagebox.showinfo("Success", "Student added successfully!")
            self.window.destroy()
        else:
            tk.messagebox.showerror("Error", "All fields are required!")
