import tkinter as tk

window = tk.Tk()
window.title("P10 Registration")

width = 600
height = 500
window.geometry(f"{width}x{height}")

# Fullname
fullname_label = tk.Label(window, text="Fullname:")
fullname_label.place(x=165, y=10)
# name_label.grid(row=0, column=2)

fullname_entry = tk.Entry(window, width=20)
fullname_entry.place(x=250, y=10)
# name_entry.grid(row=0, column=3)

# Email
email_label = tk.Label(window, text="Email:")
email_label.place(x=165, y=45)
email_entry = tk.Entry(window, width=20)
email_entry.place(x=250, y=45)

# DOB: Date of birth
dob_label = tk.Label(window, text="DOB:")
dob_label.place(x=165, y=80)
dob_entry = tk.Entry(window, width=20)
dob_entry.place(x=250, y=80)

# Gender
gender_label = tk.Label(window, text="Gender:")
gender_label.place(x=165, y=115)
gender_entry = tk.Entry(window, width=20)
gender_entry.place(x=250, y=115)

# Phone
phone_label = tk.Label(window, text="Phone:")
phone_label.place(x=165, y=150)
phone_entry = tk.Entry(window, width=20)
phone_entry.place(x=250, y=150)

# Course
course_label = tk.Label(window, text="Course:")
course_label.place(x=165, y=185)
course_entry = tk.Entry(window, width=20)
course_entry.place(x=250, y=185)

# Save button
save_btn = tk.Button(window, text="Save")
save_btn.place(x=165, y=225)

# Add button
add_btn = tk.Button(window, text="Add")
add_btn.place(x=240, y=225)

# Clear button
clear_btn = tk.Button(window, text="Clear")
clear_btn.place(x=315, y=225)

# Exit button
exit_btn = tk.Button(window, text="Exit", command=window.destroy)
exit_btn.place(x=390, y=225)

if __name__ == "__main__":
    window.mainloop()
