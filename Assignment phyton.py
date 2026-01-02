students = {}

# Add Student
def add_student():
    student = {}
    try:
        student_id = input("Enter student ID: ").strip()
        if student_id in students:
            raise ValueError("This student ID already exists.")
        
        student['ID'] = student_id
        student['name'] = input("Enter student name: ").strip()
        if not student['name']:
            raise ValueError("Name cannot be empty.")
        
        age = input("Enter student age: ").strip()
        if not age.isdigit() or not (16 <= int(age) <= 100):
            raise ValueError("Age must be between 16 and 100.")
        student['age'] = int(age)
        
        student['course'] = input("Enter student course: ").strip()
        
        gpa = input("Enter student GPA: ").strip()
        try:
            gpa = float(gpa)
            if not (0.0 <= gpa <= 4.0):
                raise ValueError
        except ValueError:
            raise ValueError("GPA must be between 0.0 and 4.0.")
        student['GPA'] = gpa
        
        students[student_id] = student
        print("Student added successfully.")
        
    except ValueError as e:
        print(f"Error: {e}")

# Update Student
def update_student():
    student_id = input("Enter the student ID needed to be updated: ").strip()
    if student_id not in students:
        print("No student found.")
        return
    
    student = students[student_id]
    print(f"Current details: {student}")
    
    update_choice = input("Which would you like to update? (name, age, course, GPA): ").strip().lower()
    if update_choice == 'name':
        student['name'] = input("Enter new name: ").strip()
    elif update_choice == 'age':
        age = input("Enter new age: ").strip()
        if age.isdigit() and 16 <= int(age) <= 100:
            student['age'] = int(age)
        else:
            print("Invalid age.")
            return
    elif update_choice == 'course':
        student['course'] = input("Enter new course: ").strip()
    elif update_choice == 'gpa':
        gpa = input("Enter new GPA: ").strip()
        try:
            gpa = float(gpa)
            if 0.0 <= gpa <= 4.0:
                student['GPA'] = gpa
            else:
                raise ValueError
        except ValueError:
            print("Invalid GPA.")
            return
    else:
        print("Invalid field choice.")
        return
    
    print("Student record updated successfully.")

# Delete Student
def delete_student():
    student_id = input("Enter the student ID to delete: ").strip()
    if student_id not in students:
        print("No student found with this ID.")
        return
    
    confirm = input(f"Are you sure you want to delete student {student_id}? (yes/no): ").strip().lower()
    if confirm == 'yes':
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Deletion canceled.")

# View Students
def view_students():
    if not students:
        print("No student records available.")
        return
    
    print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Course':<15} {'GPA':<5}")
    print("-" * 60)
    
    for student in students.values():
        print(f"{student['ID']:<10} {student['name']:<20} {student['age']:<5} {student['course']:<15} {student['GPA']:<5}")

# Save Records
def save_records(filename="students.csv"):
    """Save all student records to a CSV file."""
    with open(filename, "w") as file:
        file.write("ID,Name,Age,Course,GPA\n")
        for student in students.values():
            line = f"{student['ID']},{student['name']},{student['age']},{student['course']},{student['GPA']}\n"
            file.write(line)
    print("Data saved successfully.")

# Load Records
def load_records(filename="students.csv"):
    """Load student records from a CSV file into the students dictionary."""
    global students
    students = {} 
    try:
        with open(filename, "r") as file:
            next(file) 
            for line in file:
                student_data = line.strip().split(",")
                if len(student_data) == 5: 
                    student_id, name, age, course, gpa = student_data
                    students[student_id] = {
                        "ID": student_id,
                        "name": name,
                        "age": int(age),
                        "course": course,
                        "GPA": float(gpa)
                    }
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No data file found; starting with an empty student database.")

# Menu
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            save_records()  
        elif choice == '6':
            load_records() 
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run Program
if __name__ == "__main__":
    main()
