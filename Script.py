import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from fpdf import FPDF

roles = [
    "Software Developer", "Web Developer", "Data Scientist", "Machine Learning Engineer", "Big Data Analyst",
    "Network Administrator", "Database Administrator", "Cyber Security Analyst", "IoT Specialist",
    "Cloud Computing Engineer", "Software Project Manager", "AI Researcher", "System Analyst", "Game Developer",
    "Mobile App Developer", "Data Analyst", "UI/UX Designer", "IT Consultant", "Full Stack Developer", "Ethical Hacker",
    "Technical Writer", "IT Support Specialist", "DevOps Engineer", "Automation Engineer", "Lecturer/Trainer in Computer Applications"
]

resume_template = """PARASMANI KHUNTE\nEmail: parasmanikhunte@gmail.com | Phone: +91 8103713757 | Location: Bilaspur\nLinkedIn: https://www.linkedin.com/in/parasmani-khunte-330488228/ | GitHub: https://github.com/PARASMANI-KHUNTE\n\n---\n\nCAREER OBJECTIVE\nTo leverage my strong foundation in {selected_roles} to deliver innovative solutions and contribute to impactful projects.\n\n---\n\nEDUCATION\nBachelor of Computer Applications (BCA), Computer Science\nGuru Ghasidas University | 2022 - 2025\n\n---\n\nTECHNICAL SKILLS\n- Relevant Skills for {selected_roles}\n\n---\n\nPROJECTS\n- Projects tailored for {selected_roles}\n\n---\n\nWORK EXPERIENCE\n- Experience highlighting {selected_roles}\n\n---\n\nREFERENCES\nAvailable upon request.\n"""

def generate_resume(selected_roles):
    # Create a new PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Fill content
    content = resume_template.format(selected_roles=', '.join(selected_roles))
    for line in content.split("\n"):
        pdf.multi_cell(0, 10, line)

    # Save the PDF
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf.output(file_path)
        messagebox.showinfo("Success", "Resume saved successfully!")

def main():
    def create_resume():
        selected = [role for role, var in zip(roles, role_vars) if var.get()]
        if selected:
            generate_resume(selected)
        else:
            messagebox.showwarning("Warning", "Please select at least one role.")

    # Create the main window
    root = tk.Tk()
    root.title("Resume Builder")

    # Title
    ttk.Label(root, text="Select Roles for Your Resume", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    # Role selection
    role_vars = [tk.BooleanVar() for _ in roles]
    for idx, role in enumerate(roles):
        ttk.Checkbutton(root, text=role, variable=role_vars[idx]).grid(row=idx // 2 + 1, column=idx % 2, sticky=tk.W, padx=10)

    # Generate Button
    ttk.Button(root, text="Generate Resume", command=create_resume).grid(row=len(roles) // 2 + 2, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
