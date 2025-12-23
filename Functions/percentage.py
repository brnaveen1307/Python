def calculate_percentage(part, total):
    return (part / total) * 100

marks_scored = 78
total_marks = 100

percentage = calculate_percentage(marks_scored, total_marks)

print(f"Student scored {percentage}%")
