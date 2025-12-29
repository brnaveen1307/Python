def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = 70      # in kg
height = 1.75    # in meters

bmi = calculate_bmi(weight, height)
print("BMI:", round(bmi, 2))
