# Student Report Generator


# Global variable
school_name = "CodeBridge Academy"


# Function with normal arguments
def calculate_average(name, *marks):
    # Local variable
    total = sum(marks)
    average = total / len(marks)

    return name, average


# Function with **kwargs
def student_info(**kwargs):
    print("\n--- Student Information ---")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Function using both *args and **kwargs
def create_report(*subjects, **student):
    print("\n===== STUDENT REPORT =====")

    print(f"School: {school_name}")

    print(f"Student Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")

    print("\nSubjects:")

    for subject in subjects:
        print(f"- {subject}")


# Normal function
def show_result(name, *marks):
    name, average = calculate_average(name, *marks)

    print("\n===== RESULT =====")
    print(f"Name: {name}")
    print(f"Average: {average:.2f}")

    if average >= 60:
        print("Result: Pass")
    else:
        print("Result: Fail")


# Program starts here

create_report(
    "Python",
    "Database",
    "Django",
    name="Shawkat",
    student_id="CB101"
)

student_info(
    name="Shawkat",
    age=25,
    course="Backend Development",
    level="Beginner"
)

show_result(
    "Shawkat",
    80,
    75,
    90,
    85
)