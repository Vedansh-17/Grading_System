import tkinter as tk
from tkinter import ttk

# Dictionary containing courses and their corresponding subjects
Courses_and_Subjects = {
    "Computer Engineering Technician": ["Maths", "Python", "Electrical Fundamentals"],
    "Chemical Lab Technician": ["Organic Chemistry", "Statistics", "Microbiology"],
    "International Business Management": ["Financial Analysis", "International Trade Logistics", "Computer Software Applications"],
    "Mechanical Engineering": ["Mechanics and Statics","Thermodynamics","Material Science and Engineering","Machine Design","Fluid Mechanics and Hydraulics"], # type: ignore
    "Project Management":["Project Planning","Risk Management","Quality Management","Stakeholder Management","Cost Estimating and Budgeting"], # type: ignore
}

# Dictionary containing list of student ids 
course_student_ids = {
    "Computer Engineering Technician": list(range(998810, 998820)),
    "Chemical Lab Technician": list(range(998821, 998830)),
    "International Business Management": list(range(998831, 998840)),
    "Mechanical Engineering": list(range(998841,998850)),
    "Project Management": list(range(998851,998860))
}

# Dictionary containing marks for each subject for each student
student_marks = {998810: {"Maths": 85, "Python": 90, "Electrical Fundamentals": 75, "Tech Reports": 87, "Practical Circuits": 83},

    998811: {"Maths": 78, "Python": 76, "Electrical Fundamentals": 82, "Tech Reports": 85, "Practical Circuits": 92},
    998812: {"Maths": 85, "Python": 65, "Electrical Fundamentals": 73, "Tech Reports": 83, "Practical Circuits": 57},
    998813: {"Maths": 67, "Python": 69, "Electrical Fundamentals": 65, "Tech Reports": 68, "Practical Circuits": 60},
    998814: {"Maths": 65, "Python": 88, "Electrical Fundamentals": 90, "Tech Reports": 74, "Practical Circuits": 83},
    998815: {"Maths": 72, "Python": 83, "Electrical Fundamentals": 84, "Tech Reports": 69, "Practical Circuits": 74},
    998816: {"Maths": 83, "Python": 74, "Electrical Fundamentals": 64, "Tech Reports": 87, "Practical Circuits": 57},
    998817: {"Maths": 79, "Python": 69, "Electrical Fundamentals": 74, "Tech Reports": 58, "Practical Circuits": 85},
    998818: {"Maths": 80, "Python": 84, "Electrical Fundamentals": 75, "Tech Reports": 68, "Practical Circuits": 64},
    998819: {"Maths": 58, "Python": 75, "Electrical Fundamentals": 82, "Tech Reports": 54, "Practical Circuits": 74},
    998820: {"Maths": 67, "Python": 90, "Electrical Fundamentals": 67, "Tech Reports": 78, "Practical Circuits": 82},

    998821 : {"Organic Chemistry": 87, "Statistics": 64, "Microbiology": 75,"Inorganic Chemistry": 58,"Environmental Science": 74},
    998822 : {"Organic Chemistry": 63, "Statistics": 80, "Microbiology": 58,"Inorganic Chemistry": 69,"Environmental Science": 80},
    998823 : {"Organic Chemistry": 74, "Statistics": 73, "Microbiology": 64,"Inorganic Chemistry": 74,"Environmental Science": 63},
    998824 : {"Organic Chemistry": 57, "Statistics": 85, "Microbiology": 83,"Inorganic Chemistry": 80,"Environmental Science": 85},
    998825 : {"Organic Chemistry": 68, "Statistics": 49, "Microbiology": 90,"Inorganic Chemistry": 72,"Environmental Science": 59},
    998826 : {"Organic Chemistry": 91, "Statistics": 67, "Microbiology": 59,"Inorganic Chemistry": 63,"Environmental Science": 60},
    998827 : {"Organic Chemistry": 85, "Statistics": 52, "Microbiology": 62,"Inorganic Chemistry": 84,"Environmental Science": 73},
    998828 : {"Organic Chemistry": 83, "Statistics": 90, "Microbiology": 78,"Inorganic Chemistry": 73,"Environmental Science": 77},
    998829 : {"Organic Chemistry": 68, "Statistics": 73, "Microbiology": 82,"Inorganic Chemistry": 65,"Environmental Science": 84},
    998830 : {"Organic Chemistry": 57, "Statistics": 58, "Microbiology": 58,"Inorganic Chemistry": 85,"Environmental Science": 90},

    998831 : {"Financial Analysis":58, "International Trade Logistics":74, "Computer Software Applications":89,"Cross-cultural Communications":59,"International Business Law":74},
    998832 : {"Financial Analysis":64, "International Trade Logistics":82, "Computer Software Applications":77,"Cross-cultural Communications":83,"International Business Law":57},
    998833 : {"Financial Analysis":90, "International Trade Logistics":65, "Computer Software Applications":83,"Cross-cultural Communications":57,"International Business Law":63},
    998834 : {"Financial Analysis":74, "International Trade Logistics":87, "Computer Software Applications":62,"Cross-cultural Communications":90,"International Business Law":81},
    998835 : {"Financial Analysis":53, "International Trade Logistics":59, "Computer Software Applications":57,"Cross-cultural Communications":81,"International Business Law":90},
    998836 : {"Financial Analysis":86, "International Trade Logistics":67, "Computer Software Applications":90,"Cross-cultural Communications":74,"International Business Law":69},
    998837 : {"Financial Analysis":72, "International Trade Logistics":72, "Computer Software Applications":84,"Cross-cultural Communications":63,"International Business Law":58},
    998838 : {"Financial Analysis":90, "International Trade Logistics":81, "Computer Software Applications":69,"Cross-cultural Communications":58,"International Business Law":74},
    998839 : {"Financial Analysis":59, "International Trade Logistics":58, "Computer Software Applications":71,"Cross-cultural Communications":71,"International Business Law":63},
    998840 : {"Financial Analysis":60, "International Trade Logistics":73, "Computer Software Applications":57,"Cross-cultural Communications":90,"International Business Law":77},
    
    998841 : {"Mechanics and Statics":60,"Thermodynamics":78,"Material Science and Engineering":64,"Machine Design":72,"Fluid Mechanics and Hydraulics":80},
    998842 : {"Mechanics and Statics":90,"Thermodynamics":68,"Material Science and Engineering":82,"Machine Design":61,"Fluid Mechanics and Hydraulics":76},
    998843 : {"Mechanics and Statics":84,"Thermodynamics":81,"Material Science and Engineering":74,"Machine Design":55,"Fluid Mechanics and Hydraulics":65},
    998844 : {"Mechanics and Statics":77,"Thermodynamics":57,"Material Science and Engineering":81,"Machine Design":83,"Fluid Mechanics and Hydraulics":80},
    998845 : {"Mechanics and Statics":53,"Thermodynamics":81,"Material Science and Engineering":58,"Machine Design":60,"Fluid Mechanics and Hydraulics":59},
    998846 : {"Mechanics and Statics":60,"Thermodynamics":64,"Material Science and Engineering":64,"Machine Design":49,"Fluid Mechanics and Hydraulics":62},
    998847 : {"Mechanics and Statics":84,"Thermodynamics":83,"Material Science and Engineering":83,"Machine Design":74,"Fluid Mechanics and Hydraulics":74},
    998848 : {"Mechanics and Statics":74,"Thermodynamics":90,"Material Science and Engineering":90,"Machine Design":81,"Fluid Mechanics and Hydraulics":82},
    998849 : {"Mechanics and Statics":68,"Thermodynamics":54,"Material Science and Engineering":48,"Machine Design":68,"Fluid Mechanics and Hydraulics":90},
    998850 : {"Mechanics and Statics":90,"Thermodynamics":62,"Material Science and Engineering":77,"Machine Design":75,"Fluid Mechanics and Hydraulics":58},

    998851 : {"Mechanics and Statics":60,"Thermodynamics":78,"Material Science and Engineering":64,"Machine Design":72,"Fluid Mechanics and Hydraulics":80},
    998851 : {"Mechanics and Statics":90,"Thermodynamics":68,"Material Science and Engineering":82,"Machine Design":61,"Fluid Mechanics and Hydraulics":76},
    998853 : {"Mechanics and Statics":84,"Thermodynamics":81,"Material Science and Engineering":74,"Machine Design":55,"Fluid Mechanics and Hydraulics":65},
    998854 : {"Mechanics and Statics":77,"Thermodynamics":57,"Material Science and Engineering":81,"Machine Design":83,"Fluid Mechanics and Hydraulics":80},
    998855 : {"Mechanics and Statics":53,"Thermodynamics":81,"Material Science and Engineering":58,"Machine Design":60,"Fluid Mechanics and Hydraulics":59},
    998856 : {"Mechanics and Statics":60,"Thermodynamics":64,"Material Science and Engineering":64,"Machine Design":49,"Fluid Mechanics and Hydraulics":62},
    998857 : {"Mechanics and Statics":84,"Thermodynamics":83,"Material Science and Engineering":83,"Machine Design":74,"Fluid Mechanics and Hydraulics":74},
    998858 : {"Mechanics and Statics":74,"Thermodynamics":90,"Material Science and Engineering":90,"Machine Design":81,"Fluid Mechanics and Hydraulics":82},
    998859 : {"Mechanics and Statics":68,"Thermodynamics":54,"Material Science and Engineering":48,"Machine Design":68,"Fluid Mechanics and Hydraulics":90},
    998860 : {"Mechanics and Statics":90,"Thermodynamics":62,"Material Science and Engineering":77,"Machine Design":75,"Fluid Mechanics and Hydraulics":58}
}

def show_student_marks():
    selected_student_id = int(student_combobox.get())
    selected_course = course_combobox.get()
    
    # Get the subjects for the selected course
    subjects = Courses_and_Subjects[selected_course]
    
    # Display the marks for the selected student
    marks_text.delete('1.0', tk.END)  # Clear previous content
    marks_text.insert(tk.END, "Marks for Student ID " + str(selected_student_id) + ":\n\n")
    for subject in subjects:
        marks_text.insert(tk.END, subject + ": " + str(student_marks[selected_student_id][subject]) + "\n")

# Create a Tkinter window
window = tk.Tk()
window.title("Student Marks")

# create a label for the heading 
heading_label = ttk.Label(window, text="Student Grading", font= ('Times New Roman',45), foreground=('red'), background=('light blue'))
heading_label.grid(row=1, column=4)


# Create a label prompting the user to choose a course
course_label = ttk.Label(window, text="Choose a course:", font=('Arial',20), foreground=('black'))
course_label.grid(row=5, column=1)

# Define course options
courses = list(Courses_and_Subjects.keys())

# Create a combobox for course selection
course_combobox = ttk.Combobox(window, values=courses, state="readonly",foreground=('blue'))
course_combobox.grid(row=5, column=4)

# Create a label for student ID selection
student_label = ttk.Label(window, text="Choose Student ID:", font=('Arial',20), foreground=('black'))
student_label.grid(row=7, column=1)

# Create a combobox for student ID selection
student_combobox = ttk.Combobox(window, values=[], state="readonly")
student_combobox.grid(row=7, column=4)

# Create a button to show student marks
search_button = ttk.Button(window, text="Search", command=show_student_marks)
search_button.grid(row=8, column=2)

# Create a Text widget to display student marks
marks_text = tk.Text(window, height=20, width=45)
marks_text.grid(row=11, column=1)


# Function to update student combobox based on selected course
def update_student_combobox(event):
    selected_course = course_combobox.get()
    student_combobox['values'] = course_student_ids[selected_course]

# Bind event to update student combobox
course_combobox.bind("<<ComboboxSelected>>", update_student_combobox)

# Run the Tkinter event loop
window.mainloop()
