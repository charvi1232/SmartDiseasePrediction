from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from model import predict_disease

# =========================================
# MAIN WINDOW
# =========================================

root = Tk()

root.title("Smart Disease Prediction System")

root.geometry("1000x700")

root.config(bg="#dff6ff")

root.state("zoomed")

# =========================================
# USER VARIABLES
# =========================================

user_name = StringVar()
user_dob = StringVar()

symptoms = {
    "Fever": StringVar(value="No"),
    "Cough": StringVar(value="No"),
    "Headache": StringVar(value="No"),
    "Fatigue": StringVar(value="No"),
    "Nausea": StringVar(value="No"),
    "Body Pain": StringVar(value="No"),
    "Sore Throat": StringVar(value="No"),
    "Vomiting": StringVar(value="No"),
    "Dizziness": StringVar(value="No"),
    "Cold": StringVar(value="No")
}

# =========================================
# CLEAR WINDOW
# =========================================

def clear_window():

    for widget in root.winfo_children():

        widget.destroy()

# =========================================
# PAGE TITLE
# =========================================

def page_title(title):

    Label(
        root,
        text=title,
        font=("Helvetica", 30, "bold"),
        bg="#dff6ff",
        fg="#003366"
    ).pack(pady=25)

# =========================================
# STYLED BUTTON
# =========================================

def styled_button(text, command):

    button = Button(
        root,
        text=text,
        command=command,
        font=("Helvetica", 16, "bold"),
        bg="#4da6ff",
        fg="white",
        activebackground="#3399ff",
        activeforeground="white",
        width=20,
        height=2,
        bd=0,
        cursor="hand2"
    )

    return button

# =========================================
# WELCOME PAGE
# =========================================

def welcome_page():

    clear_window()

    page_title("SMART DISEASE PREDICTION SYSTEM")

    Label(
        root,
        text="Machine Learning Based Healthcare Application",
        font=("Helvetica", 18),
        bg="#dff6ff",
        fg="#004466"
    ).pack(pady=10)

    Label(
        root,
        text="Predict diseases quickly using symptoms",
        font=("Helvetica", 16),
        bg="#dff6ff",
        fg="#005580"
    ).pack(pady=5)

    Label(
        root,
        text="""
✔ Easy to Use
✔ Interactive GUI
✔ Machine Learning Prediction
✔ Healthcare Assistance
""",
        font=("Helvetica", 15),
        bg="#dff6ff",
        fg="#006699",
        justify=LEFT
    ).pack(pady=20)

    styled_button(
        "GET STARTED",
        info_page
    ).pack(pady=40)

# =========================================
# INFO PAGE
# =========================================

def info_page():

    clear_window()

    page_title("PROJECT INFORMATION")

    info_frame = Frame(
        root,
        bg="white",
        bd=4,
        relief=RIDGE
    )

    info_frame.pack(pady=30, padx=120)

    info_text = """
This system predicts diseases based on symptoms
using Machine Learning algorithms.

Technologies Used:
• Python
• Tkinter GUI
• Pandas
• Scikit-learn

Workflow:
1. Enter user details
2. Select symptoms
3. Predict disease
4. Display result
"""

    Label(
        info_frame,
        text=info_text,
        font=("Helvetica", 16),
        bg="white",
        fg="#003366",
        justify=LEFT,
        padx=35,
        pady=35
    ).pack()

    styled_button(
        "CONTINUE",
        user_details_page
    ).pack(pady=30)

# =========================================
# USER DETAILS PAGE
# =========================================

def user_details_page():

    clear_window()

    page_title("ENTER YOUR DETAILS")

    outer_frame = Frame(
        root,
        bg="#dff6ff"
    )

    outer_frame.pack(expand=True)

    card = Frame(
        outer_frame,
        bg="white",
        bd=5,
        relief=RIDGE
    )

    card.pack(pady=20, ipadx=30, ipady=20)

    # NAME LABEL

    Label(
        card,
        text="👤 Full Name",
        font=("Helvetica", 17, "bold"),
        bg="white",
        fg="#003366"
    ).pack(anchor="w", pady=(10, 5), padx=20)

    # NAME ENTRY BOX

    name_entry = Entry(
        card,
        textvariable=user_name,
        font=("Helvetica", 16),
        width=30,
        bd=3,
        relief=GROOVE,
        bg="#f7fbff"
    )

    name_entry.pack(padx=20, pady=5, ipady=8)

    # DOB LABEL

    Label(
        card,
        text="📅 Date of Birth",
        font=("Helvetica", 17, "bold"),
        bg="white",
        fg="#003366"
    ).pack(anchor="w", pady=(20, 5), padx=20)

    # CALENDAR DATE PICKER

    dob_entry = DateEntry(
        card,
        textvariable=user_dob,
        font=("Helvetica", 15),
        width=27,
        background="#4da6ff",
        foreground="white",
        borderwidth=3,
        date_pattern="dd/mm/yyyy"
    )

    dob_entry.pack(padx=20, pady=10, ipady=5)

    # VALIDATION FUNCTION

    def validate_user():

        name = user_name.get()

        dob = user_dob.get()

        if name == "" or dob == "":

            messagebox.showerror(
                "Error",
                "Please enter all details"
            )

            return

        try:

            birth_date = datetime.strptime(
                dob,
                "%d/%m/%Y"
            )

            today = datetime.today()

            age = today.year - birth_date.year - (
                (today.month, today.day)
                <
                (birth_date.month, birth_date.day)
            )

        except:

            messagebox.showerror(
                "Error",
                "Invalid Date Format"
            )

            return

        if age < 18:

            messagebox.showwarning(
                "Access Denied",
                "Advice available only for users above 18 years."
            )

            return

        symptom_page()

    # CONTINUE BUTTON

    Button(
        card,
        text="CONTINUE",
        command=validate_user,
        font=("Helvetica", 16, "bold"),
        bg="#4da6ff",
        fg="white",
        activebackground="#3399ff",
        activeforeground="white",
        width=20,
        height=2,
        bd=0,
        cursor="hand2"
    ).pack(pady=30)

# =========================================
# SYMPTOM PAGE
# =========================================

def symptom_page():

    clear_window()

    page_title("SELECT YOUR SYMPTOMS")

    symptom_frame = Frame(
        root,
        bg="white",
        bd=4,
        relief=RIDGE
    )

    symptom_frame.pack(pady=20, padx=80)

    row = 0

    for symptom, variable in symptoms.items():

        Label(
            symptom_frame,
            text=symptom,
            font=("Helvetica", 15, "bold"),
            bg="white",
            fg="#003366",
            width=18,
            anchor="w"
        ).grid(row=row, column=0, padx=20, pady=12)

        dropdown = OptionMenu(
            symptom_frame,
            variable,
            "Yes",
            "No"
        )

        dropdown.config(
            font=("Helvetica", 13),
            width=10,
            bg="#e6f2ff"
        )

        dropdown.grid(row=row, column=1, padx=20)

        row += 1

    styled_button(
        "PREDICT DISEASE",
        show_result
    ).pack(pady=30)

# =========================================
# RESULT PAGE
# =========================================

def show_result():

    values = []

    yes_count = 0

    for symptom in symptoms.values():

        if symptom.get() == "Yes":

            values.append(1)

            yes_count += 1

        else:

            values.append(0)

    if yes_count == 0:

        result = "No major disease detected"

    else:

        result = predict_disease(values)

    clear_window()

    page_title("PREDICTION RESULT")

    result_frame = Frame(
        root,
        bg="white",
        bd=5,
        relief=RIDGE
    )

    result_frame.pack(pady=50, padx=120)

    Label(
        result_frame,
        text=f"Hello, {user_name.get()}",
        font=("Helvetica", 22, "bold"),
        bg="white",
        fg="#003366"
    ).pack(pady=20)

    Label(
        result_frame,
        text=f"Predicted Disease:\n{result}",
        font=("Helvetica", 24, "bold"),
        bg="white",
        fg="#cc0000",
        padx=40,
        pady=20,
        justify=CENTER
    ).pack()

    Label(
        result_frame,
        text="""
⚠ This prediction is for educational purposes only.
Please consult a doctor for professional medical advice.
""",
        font=("Helvetica", 14),
        bg="white",
        fg="#003366",
        justify=CENTER
    ).pack(pady=20)

    styled_button(
        "CHECK AGAIN",
        symptom_page
    ).pack(pady=20)

# =========================================
# START GUI
# =========================================

def start_gui():

    welcome_page()

    root.mainloop()