# Student Grade Management System (Console-Based)
students = {}

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students[name] = grade
    print(f"{name} added successfully.\n")

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        grade = float(input("Enter new grade: "))
        students[name] = grade
        print(f"{name}'s grade updated.\n")
    else:
        print("Student not found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"{name} deleted successfully.\n")
    else:
        print("Student not found.\n")

def show_students():
    if students:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No student records found.\n")

def main():
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_grade()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            show_students()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
      
