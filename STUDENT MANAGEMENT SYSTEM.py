# File: student_management_gui.py

import mysql.connector as con
from tkinter import simpledialog, messagebox, ttk, font
import tkinter as tk
import sys  # To ensure complete termination of the program


# Function to get database connection
def connect_db():
    return con.connect(host="localhost", user="root", password="Srik@1408", database="STUDENT_MANAGEMENT_SYSTEM")


def setup_tkinter():
    root = tk.Tk()
    root.title("Student Management System")
    root.attributes('-fullscreen', True)  # Fullscreen mode
    root.configure(bg="lightblue")

    # Font adjustments
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=20)  # Adjust the default font size globally

    # Welcome message
    welcome_label = tk.Label(
        root,
        text="WELCOME TO STUDENT MANAGEMENT SYSTEM",
        font=("Arial", 36, "bold"),
        bg="lightblue",
        fg="darkblue"
    )
    welcome_label.pack(pady=20)  # Adds padding above the table

    # Frame for table display
    table_frame = tk.Frame(root, bg="lightblue")
    table_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Treeview widget for table with font and spacing adjustments
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 18, "bold"))  # Header font
    style.configure("Treeview", font=("Arial", 14), rowheight=30)  # Cell font and row height

    table = ttk.Treeview(table_frame, show="headings")
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar for the Treeview
    scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    table.configure(yscrollcommand=scrollbar.set)

    return root, table


# Function to handle the termination logic
def handle_cancel(value, root):
    if value is None:  # Check if Cancel was pressed
        messagebox.showinfo("Exit", "Program terminated by user.", parent=root)
        root.destroy()
        sys.exit(0)


# Function to display table contents dynamically
def display_in_tkinter(table, headers, rows):
    # Clear existing content
    table.delete(*table.get_children())
    table["columns"] = headers

    # Set column headers
    for header in headers:
        table.heading(header, text=header)
        table.column(header, anchor="center", stretch=True)

    # Insert rows
    for row in rows:
        table.insert("", "end", values=row)


# Core functions
def search_student(table, root):
    d = connect_db()
    c = d.cursor()
    c.execute('SELECT name FROM student_details')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)

    root.update()
    k = simpledialog.askstring("Search Student", "Enter name to search student Name:", parent=root)
    handle_cancel(k, root)  # Terminate if Cancel is pressed

    c.execute('SELECT * FROM STUDENT_DETAILS WHERE NAME LIKE %s', ("%" + k + "%",))
    a = c.fetchall()
    if a:
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, a)
    else:
        messagebox.showinfo("Search Result", "Student Details Not Found", parent=root)
    d.close()


def update_details(table, root):
    d = connect_db()
    c = d.cursor()
    root.update()

    opt = simpledialog.askinteger(
        "Update Details",
        "1. Update Name\n2. Update Gender\n3. Update Class\n4. Update Section\n"
        "5. Update Phone Number\n6. Update Email ID\n7. Update Stream\nEnter your choice:",
        parent=root
    )
    handle_cancel(opt, root)

    if opt == 1:
        c.execute('SELECT name, admission_number FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        admission_number = simpledialog.askstring("Update Name", "Enter Admission Number:", parent=root)
        handle_cancel(admission_number, root)
        new_name = simpledialog.askstring("Update Name", "Enter New Name:", parent=root)
        handle_cancel(new_name, root)

        c.execute('UPDATE STUDENT_DETAILS SET NAME=%s WHERE ADMISSION_NUMBER=%s', (new_name, admission_number))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()
    elif opt == 2:
         c.execute('SELECT name, sex FROM student_details')
         r = c.fetchall()
         headers = [i[0] for i in c.description]
         display_in_tkinter(table, headers, r)
         name = simpledialog.askstring("Update Gender", "Enter Name:", parent=root)
         new_gender = simpledialog.askstring("Update Gender", "Enter New Gender:", parent=root)
         c.execute('UPDATE STUDENT_DETAILS SET SEX=%s WHERE NAME=%s', (new_gender, name))
         if c.rowcount == 0:
             messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
         else:
             d.commit()

    elif opt == 3:
        c.execute('SELECT name, class FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        name = simpledialog.askstring("Update Class", "Enter Name:", parent=root)
        new_class = simpledialog.askinteger("Update Class", "Enter New Class:", parent=root)
        c.execute('UPDATE STUDENT_DETAILS SET CLASS=%s WHERE NAME=%s', (new_class, name))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()

    elif opt == 4:
        c.execute('SELECT name, sec FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        name = simpledialog.askstring("Update Section", "Enter Name:", parent=root)
        new_section = simpledialog.askstring("Update Section", "Enter New Section:", parent=root)
        c.execute('UPDATE STUDENT_DETAILS SET SEC=%s WHERE NAME=%s', (new_section, name))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()

    elif opt == 5:
        c.execute('SELECT name, phone_number FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        name = simpledialog.askstring("Update Phone Number", "Enter Name:", parent=root)
        new_phone = simpledialog.askstring("Update Phone Number", "Enter New Phone Number:", parent=root)
        c.execute('UPDATE STUDENT_DETAILS SET PHONE_NUMBER=%s WHERE NAME=%s', (new_phone, name))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()

    elif opt == 6:
        c.execute('SELECT name, email_id FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        name = simpledialog.askstring("Update Email", "Enter Name:", parent=root)
        new_email = simpledialog.askstring("Update Email", "Enter New Email ID:", parent=root)
        c.execute('UPDATE STUDENT_DETAILS SET EMAIL_ID=%s WHERE NAME=%s', (new_email, name))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()

    elif opt == 7:
        c.execute('SELECT name, stream FROM student_details')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)

        name = simpledialog.askstring("Update Stream", "Enter Name:", parent=root)
        new_stream = simpledialog.askstring("Update Stream", "Enter New Stream:", parent=root)
        c.execute('UPDATE STUDENT_DETAILS SET STREAM=%s WHERE NAME=%s', (new_stream, name))
        if c.rowcount == 0:
            messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
        else:
            d.commit()

    else:
        messagebox.showinfo("Invalid Choice", "Invalid Option Selected.", parent=root)

    # Display the updated table
    c.execute('SELECT * FROM STUDENT_DETAILS')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)
    d.close()

def delete_student(table, root):
    d = connect_db()
    c = d.cursor()
    root.update()

    c.execute('SELECT name FROM student_details')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)

    name = simpledialog.askstring("Delete Student", "Enter the name of the student to delete:", parent=root)
    handle_cancel(name, root)

    c.execute('DELETE FROM STUDENT_DETAILS WHERE NAME=%s', (name,))
    if c.rowcount == 0:
        messagebox.showinfo("Error", "STUDENT NOT FOUND", parent=root)
    else:
        d.commit()
        messagebox.showinfo( "Message","Student data deleted", parent=root)

    # Display updated table
    c.execute('SELECT * FROM STUDENT_DETAILS')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)
    d.close()


def view_table(table):
    d = connect_db()
    c = d.cursor()
    c.execute('SELECT * FROM STUDENT_DETAILS')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)
    d.close()


def add_student(table, root):
    root.update()

    # Collect student details via dialogs
    data = {
        "name": simpledialog.askstring("Add Student", "Enter student name:", parent=root),
        "admission_number": simpledialog.askinteger("Add Student", "Enter student admission number:", parent=root),
        "gender": simpledialog.askstring("Add Student", "Enter gender (M/F):", parent=root),
        "class": simpledialog.askinteger("Add Student", "Enter class (numeric value):", parent=root),
        "section": simpledialog.askstring("Add Student", "Enter section:", parent=root),
        "phone_number": simpledialog.askinteger("Add Student", "Enter phone number:", parent=root),
        "email": simpledialog.askstring("Add Student", "Enter email:", parent=root),
        "stream": simpledialog.askstring("Add Student", "Enter stream:", parent=root),
        "marks": simpledialog.askinteger("Add Student", "Enter marks:", parent=root)
    }

    for key, value in data.items():
        handle_cancel(value, root)

    try:
        d = connect_db()
        c = d.cursor()
        c.execute(
            'INSERT INTO STUDENT_DETAILS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (data["admission_number"], data["name"], data["gender"], data["class"],
             data["section"], data["phone_number"], data["email"], data["stream"], data["marks"])
        )
        d.commit()
        messagebox.showinfo("Success", "Student added successfully!", parent=root)

        # Display updated table
        c.execute('SELECT * FROM STUDENT_DETAILS')
        r = c.fetchall()
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, r)
        d.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add student. Error: {e}", parent=root)

def view_Marks(table, root):
    d = connect_db()
    c = d.cursor()
    
    # Fetch and display student names in the table
    c.execute('SELECT name FROM student_details')
    r = c.fetchall()
    headers = [i[0] for i in c.description]
    display_in_tkinter(table, headers, r)

    root.update()
    
    # Prompt for student name and handle cancel
    student_name = simpledialog.askstring("View Marks", "Enter name to view student marks:", parent=root)
    handle_cancel(student_name, root)  # Exit if Cancel is pressed

    # Fetch and display marks for the student
    c.execute('SELECT NAME, MARKS FROM STUDENT_DETAILS WHERE NAME LIKE %s', ("%" + student_name + "%",))
    s = c.fetchall()
    if s:
        headers = [i[0] for i in c.description]
        display_in_tkinter(table, headers, s)
    else:
        messagebox.showinfo("Marks Result", "No marks found.", parent=root)
    
    d.close()

# Admin and User Menus
def admin(root, table):
    while True:
        root.update()
        ch = simpledialog.askinteger(
            "Admin",
            "1. Search Student\n2. Update Details\n3. Delete Student\n4. View Marks\n5. Add Student\n6. View Table\n7. Exit\nEnter your choice:",
            parent=root
        )
        handle_cancel(ch, root)
        if ch == 1:
            search_student(table, root)
        elif ch == 2:
            update_details(table, root)
        elif ch == 3:
            delete_student(table, root)
        elif ch == 4:
            view_Marks(table,root)
        elif ch == 5:
            add_student(table, root)
        elif ch == 6:
            view_table(table)
        elif ch == 7:
            break
        else:
            messagebox.showerror("Error", "Invalid input", parent=root)


def user(root, table):
    while True:
        root.update()
        ch = simpledialog.askinteger(
            "User Menu",
            "1. Search Your Details\n2. View Marks\n3. View Table\n4. Exit\nEnter your choice:",
            parent=root
        )
        handle_cancel(ch, root)
        if ch == 1:
            search_student(table, root)
        elif ch == 2:
            view_Marks(table,root)
        elif ch == 3:
            view_table(table)
        elif ch == 4:
            break
        else:
            messagebox.showerror("Error", "Invalid input", parent=root)


# Main Function
def main():
    root, table = setup_tkinter()
    while True:
        root.update()
        ch = simpledialog.askinteger("Login", "1. Admin\n2. User\n3. Exit\nEnter your choice:", parent=root)
        handle_cancel(ch, root)
        if ch == 1:
            admin(root, table)
        elif ch == 2:
            user(root, table)
        elif ch == 3:
             messagebox.showinfo("Message", "Program terminated", parent=root)
             break
        else:
            messagebox.showerror("Error", "Invalid choice", parent=root)
    root.destroy()


# Starting the application
if __name__ == "__main__":
    main()
