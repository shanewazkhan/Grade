import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class AdmitCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Admit Card Generator")

        # Student Details
        self.labels = ["Student Name", "Father's Name", "Mother's Name", "Class Roll", "Admission Session", "Exam Year", "Department"]
        self.details = {}
        for idx, label in enumerate(self.labels):
            tk.Label(root, text=label).grid(row=idx, column=0)
            self.details[label] = tk.Entry(root, width=50)
            self.details[label].grid(row=idx, column=1, columnspan=2)

        # Number of Years
        self.year_label = tk.Label(root, text="Number of Years:")
        self.year_label.grid(row=len(self.labels), column=0)
        self.year_count = tk.Entry(root, width=10)
        self.year_count.grid(row=len(self.labels), column=1)
        self.year_button = tk.Button(root, text="Add Years", command=self.add_years)
        self.year_button.grid(row=len(self.labels), column=2)

        # Years List
        self.years = []

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Admit Card", command=self.generate_admit_card)
        self.generate_button.grid(row=len(self.labels) + 1, column=0, columnspan=3)

    def add_years(self):
        try:
            num_years = int(self.year_count.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the number of years.")
            return

        self.years = []
        for i in range(num_years):
            year_subjects = []
            try:
                num_subjects = int(simpledialog.askstring("Number of Subjects", f"Enter the number of subjects for year {i+1}:"))
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for the number of subjects.")
                return

            for j in range(num_subjects):
                subject_name = simpledialog.askstring("Subject Name", f"Enter the name of subject {j+1} for year {i+1}:")
                if subject_name:
                    subject_gpa = simpledialog.askfloat("Subject GPA", f"Enter the GPA for subject {subject_name}:")
                    if subject_gpa:
                        year_subjects.append((subject_name, subject_gpa))
            self.years.append(year_subjects)

    def generate_admit_card(self):
        # Collect all inputs
        student_info = {label: self.details[label].get() for label in self.labels}

        # Validate inputs
        for key, value in student_info.items():
            if not value:
                messagebox.showerror("Input Error", f"Please fill out the {key}.")
                return

        if not self.years:
            messagebox.showerror("Input Error", "Please add the years and subjects.")
            return

        # Display the student info, years, subjects, and GPAs
        info_text = "\n".join([f"{key}: {value}" for key, value in student_info.items()])
        years_text = ""
        for i, year in enumerate(self.years):
            year_text = f"Year {i+1} Subjects:\n"
            for j, subject in enumerate(year):
                year_text += f"  {j+1}. {subject[0]} - GPA: {subject[1]}\n"
            years_text += year_text
        messagebox.showinfo("Admit Card Info", f"Student Info:\n{info_text}\n\n{years_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdmitCardApp(root)
    root.mainloop()
