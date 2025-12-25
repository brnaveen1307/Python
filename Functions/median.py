def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

salaries = [28000, 32000, 35000, 40000, 45000, 120000]
median_salary = calculate_median(salaries)

print("Median Salary:", median_salary)
