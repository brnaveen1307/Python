def calculate_power(base, exponent):
    return base ** exponent

initial_power = 100      # watts
growth_factor = 2        # doubles every year
years = 5

future_power = initial_power * calculate_power(growth_factor, years)

print("Power consumption after 5 years:", future_power, "watts")
