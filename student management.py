
students = {}


courses = set()


def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    
    course_list = input("Enter courses (comma separated): ").split(",")
    course_set = {c.strip() for c in course_list}

    
    courses.update(course_set)

    
    students[sid] = {
        "name": name,
        "age": age,
        "courses": course_set
    }

    print("Student added successfully!\n")


def remove_student():
    sid = input("Enter Student ID to remove: ")
    if sid in students:
        del students[sid]
        print("Student removed successfully!\n")
    else:
        print("Student not found!\n")


def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        print("Student found:")
        print(students[sid])
    else:
        print("Student not found!\n")


def list_students():
    if not students:
        print("No students in the system.\n")
        return

    print("\n--- All Students ---")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Courses: {info['courses']}")
    print()


def list_courses():
    if not courses:
        print("No courses added yet.\n")
        return

    print("\n--- All Unique Courses ---")
    for course in courses:
        print(course)
    print()


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. List All Students")
        print("5. List All Courses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")



main()
