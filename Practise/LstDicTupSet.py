# -----------------------------
# Student Course Management System
# -----------------------------

# List to store multiple student records
students = []

# Adding some students (Tuple: fixed info like name, roll, department)
student1_info = ("Naveen", "S001", "Computer Science")
student2_info = ("Priya", "S002", "Electronics")

# Courses as a Set (no duplicate subjects)
student1_courses = {"Python", "Data Structures", "AI"}
student2_courses = {"Python", "Digital Circuits", "AI"}  # Note: Python, AI repeated intentionally

# Dictionary to combine all details
student1 = {
    "info": student1_info,
    "courses": student1_courses,
    "grades": {"Python": "A+", "Data Structures": "A", "AI": "B+"}
}

student2 = {
    "info": student2_info,
    "courses": student2_courses,
    "grades": {"Python": "A", "Digital Circuits": "B", "AI": "A-"}
}

# Add students (dictionary objects) to the list
students.extend([student1, student2])

# -----------------------------
# Operations
# -----------------------------

# Print all student data
for student in students:
    name, roll, dept = student["info"]
    print(f"\n👨‍🎓 {name} ({roll}) - {dept}")
    print("📚 Courses:", ", ".join(student["courses"]))
    
    # Show grades
    print("📊 Grades:")
    for course, grade in student["grades"].items():
        print(f"   {course}: {grade}")

# -----------------------------
# Real use case: Find all unique courses offered
# -----------------------------
all_courses = set()
for student in students:
    all_courses.update(student["courses"])

print("\n🏫 All Unique Courses Offered:", ", ".join(all_courses))
