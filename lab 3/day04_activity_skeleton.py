"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# TODO: Implement the tasks above using nested dict access.

# Task 1: Get Alice's AI301 grade
alice_ai301_grade = students["S001"]["courses"]["AI301"]["grade"]
print(f"Alice's AI301 grade: {alice_ai301_grade}")

# Task 2: Calculate Bob's GPA (weighted by credits)
bob_courses = students["S002"]["courses"]
total_points = sum(course["grade"] * course["credits"] for course in bob_courses.values())
total_credits = sum(course["credits"] for course in bob_courses.values())
bob_gpa = total_points / total_credits if total_credits > 0 else 0
print(f"Bob's GPA: {bob_gpa:.2f}")

# Task 3: Find all students in CS101
students_in_cs101 = [students[sid]["name"] for sid in students if "CS101" in students[sid]["courses"]]
print(f"Students in CS101: {students_in_cs101}")

# Task 4: Get average grade across all courses
all_grades = [course["grade"] for student in students.values() for course in student["courses"].values()]
average_grade = sum(all_grades) / len(all_grades) if all_grades else 0
print(f"Average grade across all courses: {average_grade:.2f}")

# Task 5: Find student with highest GPA
def calculate_gpa(student):
    courses = student["courses"]
    total_points = sum(course["grade"] * course["credits"] for course in courses.values())
    total_credits = sum(course["credits"] for course in courses.values())
    return total_points / total_credits if total_credits > 0 else 0

gpas = {sid: calculate_gpa(students[sid]) for sid in students}
highest_gpa_student = max(gpas, key=gpas.get)
print(f"Student with highest GPA: {students[highest_gpa_student]['name']} (GPA: {gpas[highest_gpa_student]:.2f})")
