import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button

from gui.registration.student import Student

window = Tk()
window.title("Student Registration")
window.geometry("700x350")

students = []


def add():
    student = Student(
        fullname_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender_entry.get(),
        phone_entry.get(),
        course_entry.get(),
        datetime.now()
    )
    students.append(student.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    with open("students.csv", "a", newline="\n") as file:
        header = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("students.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(students)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    gender_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


# Fullname
fullname_label = Label(window, text="Fullname: ", padx=20, pady=10)
fullname_label.grid(row=0, column=0)
fullname_entry = Entry(window, width=30, borderwidth=3)
fullname_entry.grid(row=0, column=1)

# Email
email_label = Label(window, text="Email: ", padx=20, pady=10)
email_label.grid(row=1, column=0)
email_entry = Entry(window, width=30, borderwidth=3)
email_entry.grid(row=1, column=1)

# DOB - Date of birth
dob_label = Label(window, text="DOB: ", padx=20, pady=10)
dob_label.grid(row=2, column=0)
dob_entry = Entry(window, width=30, borderwidth=3)
dob_entry.grid(row=2, column=1)

# Gender
gender_label = Label(window, text="Gender: ", padx=20, pady=10)
gender_label.grid(row=3, column=0)
gender_entry = Entry(window, width=30, borderwidth=3)
gender_entry.grid(row=3, column=1)

# Phone
phone_label = Label(window, text="Phone: ", padx=20, pady=10)
phone_label.grid(row=4, column=0)
phone_entry = Entry(window, width=30, borderwidth=3)
phone_entry.grid(row=4, column=1)

# Course
course_label = Label(window, text="Course: ", padx=20, pady=10)
course_label.grid(row=5, column=0)
course_entry = Entry(window, width=30, borderwidth=3)
course_entry.grid(row=5, column=1)

# Save button
save_btn = Button(window, text="Save", padx=20, pady=10, command=save)
save_btn.place(x=60, y=250)

# Add button
add_btn = Button(window, text="Add", padx=20, pady=10, command=add)
add_btn.place(x=140, y=250)

# Clear button
clear_btn = Button(window, text="Clear", padx=18, pady=10, command=clear)
clear_btn.place(x=215, y=250)

# Exit button
exit_btn = Button(window, text="Exit", padx=20, pady=10, command=window.quit)
exit_btn.place(x=295, y=250)

if __name__ == "__main__":
    window.mainloop()
