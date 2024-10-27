import tkinter as tk
from tkinter import messagebox

# Student class with memory size calculation methods
class Student:
    def __init__(self, regno, name, marks):
        self.regno = regno
        self.name = name
        self.marks = marks
        self.total_marks = self.calculate_total()
        self.cgpa = self.calculate_cgpa()

    def calculate_total(self):
        return sum(self.marks)

    def calculate_cgpa(self):
        return round(self.total_marks / 50, 2)

    # C-like memory size calculation
    def size_in_bytes(self):
        size_regno = len(self.regno)  # Assume each char as 1 byte (C standard)
        size_name = len(self.name)
        size_marks = len(self.marks) * 4  # Assume each integer is 4 bytes (C standard)
        size_total_marks = 4  # int (4 bytes)
        size_cgpa = 4  # float (4 bytes)
        
        total_size = size_regno + size_name + size_marks + size_total_marks + size_cgpa
        
        return {
            "regno": size_regno,
            "name": size_name,
            "marks": size_marks,
            "total_marks": size_total_marks,
            "cgpa": size_cgpa,
            "total": total_size
        }

# List to store student objects
students = []
num_students = 0  # Set number of students

# Function to handle form submission
def submit_form():
    global num_students  # Reference the global num_students variable
    try:
        regno = entry_regno.get()
        name = entry_name.get()
        marks = [int(entry.get()) for entry in entry_marks]

        student = Student(regno, name, marks)
        students.append(student)

        clear_form()

        if len(students) < num_students:
            messagebox.showinfo("Next Student", f"Enter details for Student {len(students) + 1}")
        else:
            visualize_all_students()
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data for all fields.")

# Display memory and data structure visualization
def visualize_all_students():
    for widget in result_frame.winfo_children():
        widget.destroy()

    for index, student in enumerate(students):
        size_info = student.size_in_bytes()

        # Frame for each student's details
        student_frame = tk.Frame(result_frame, borderwidth=2, relief="solid", padx=10, pady=10, bg="#f0f4c3")
        student_frame.grid(row=0, column=index, padx=10, pady=5, sticky="n")

        tk.Label(student_frame, text=f"Student {index+1}", font=("Arial", 14, "bold"), fg="blue", bg="#f0f4c3").grid(row=0, column=0, columnspan=2)

        # Data and Memory Sizes in C Standards
        tk.Label(student_frame, text="Registration Number:", bg="#f0f4c3").grid(row=1, column=0, sticky="e")
        tk.Label(student_frame, text=f"{student.regno} ({size_info['regno']} bytes)", bg="#f0f4c3").grid(row=1, column=1, sticky="w")

        tk.Label(student_frame, text="Name:", bg="#f0f4c3").grid(row=2, column=0, sticky="e")
        tk.Label(student_frame, text=f"{student.name} ({size_info['name']} bytes)", bg="#f0f4c3").grid(row=2, column=1, sticky="w")

        tk.Label(student_frame, text="Marks:", bg="#f0f4c3").grid(row=3, column=0, sticky="e")
        tk.Label(student_frame, text=f"{student.marks} ({size_info['marks']} bytes)", bg="#f0f4c3").grid(row=3, column=1, sticky="w")

        tk.Label(student_frame, text="CGPA:", bg="#f0f4c3").grid(row=4, column=0, sticky="e")
        tk.Label(student_frame, text=f"{student.cgpa} ({size_info['cgpa']} bytes)", bg="#f0f4c3").grid(row=4, column=1, sticky="w")

        tk.Label(student_frame, text="Total Memory:", font=("Arial", 10, "bold"), fg="red", bg="#f0f4c3").grid(row=5, column=0, sticky="e")
        tk.Label(student_frame, text=f"{size_info['total']} bytes", font=("Arial", 10, "bold"), fg="red", bg="#f0f4c3").grid(row=5, column=1, sticky="w")

# Clear the form
def clear_form():
    entry_regno.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    for entry in entry_marks:
        entry.delete(0, tk.END)

# Function to set the number of students
def set_num_students():
    global num_students
    try:
        num_students = int(entry_num_students.get())
        entry_num_students.delete(0, tk.END)  # Clear the input field
        messagebox.showinfo("Set Number of Students", f"Number of students set to {num_students}. Please enter details.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Main window setup
root = tk.Tk()
root.title("Student Structure Visualization")
root.geometry("800x600")
root.configure(bg="#e8eaf6")

# Title Label
title_label = tk.Label(root, text="Enter Student Details", font=("Arial", 18, "bold"), bg="#e8eaf6", fg="#1a237e")
title_label.pack(pady=10)

# Form frame for input
form_frame = tk.Frame(root, bg="#e8eaf6", padx=20, pady=20)
form_frame.pack()

# Number of Students
label_num_students = tk.Label(form_frame, text="Number of Students:", font=("Arial", 12), bg="#e8eaf6", fg="#3949ab")
label_num_students.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num_students = tk.Entry(form_frame, font=("Arial", 12), width=5)
entry_num_students.grid(row=0, column=1, padx=5, pady=5)

# Set number of students button
set_students_button = tk.Button(form_frame, text="Set Number", font=("Arial", 12, "bold"), bg="#5c6bc0", fg="white", command=set_num_students)
set_students_button.grid(row=0, column=2, padx=5, pady=5)

# Registration number
label_regno = tk.Label(form_frame, text="Registration Number:", font=("Arial", 12), bg="#e8eaf6", fg="#3949ab")
label_regno.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_regno = tk.Entry(form_frame, font=("Arial", 12), width=20)
entry_regno.grid(row=1, column=1, padx=5, pady=5)

# Name
label_name = tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#e8eaf6", fg="#3949ab")
label_name.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(form_frame, font=("Arial", 12), width=20)
entry_name.grid(row=2, column=1, padx=5, pady=5)

# Marks for 5 subjects
label_marks = tk.Label(form_frame, text="Marks (5 subjects):", font=("Arial", 12), bg="#e8eaf6", fg="#3949ab")
label_marks.grid(row=3, column=0, padx=5, pady=5, sticky="e")

# Create labels and entries for each subject mark
entry_marks = []
for i in range(5):
    tk.Label(form_frame, text=f"Subject {i+1}:", font=("Arial", 12), bg="#e8eaf6", fg="#3949ab").grid(row=3, column=i+1, padx=5, pady=5)
    entry = tk.Entry(form_frame, font=("Arial", 12), width=5)
    entry.grid(row=4, column=i+1, padx=5, pady=5)
    entry_marks.append(entry)

# Submit button
submit_button = tk.Button(form_frame, text="Submit", font=("Arial", 12, "bold"), bg="#5c6bc0", fg="white", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=6, pady=10)

# Result frame for displaying student structure and memory usage
result_frame = tk.Frame(root, bg="#e8eaf6")
result_frame.pack(fill="both", expand=True, pady=10)

# Run the main loop
root.mainloop()
