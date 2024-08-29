# codetech task-2

def main():
    # Dictionary to store student grades
    students = {}

    # Number of students
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        name = input("Enter the student's name: ")

        # Get grades for each subject
        physics = float(input(f"Enter {name}'s grade in Physics: "))
        chemistry = float(input(f"Enter {name}'s grade in Chemistry: "))
        math = float(input(f"Enter {name}'s grade in Math: "))

        # Store grades in a dictionary under the student's name
        students[name] = {
            "Physics": physics,
            "Chemistry": chemistry,
            "Math": math
        }

    # Display the grades for all students
    print("\nStudent Grades:")
    for name, grades in students.items():
        print(f"\n{name}:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")

if __name__ == "__main__":
    main()
