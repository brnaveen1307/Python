import math

def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


exam_scores = [78, 82, 85, 80, 79, 81, 83]
std_dev = calculate_standard_deviation(exam_scores)

print(f"Standard Deviation of exam scores: {std_dev:.2f}")
