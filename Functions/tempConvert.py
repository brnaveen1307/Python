def convert_temperature(value, unit):
    """
    Converts temperature from Celsius to Fahrenheit or Kelvin.

    value: temperature in Celsius
    unit: 'F' for Fahrenheit, 'K' for Kelvin
    """
    if unit == 'F':
        return (value * 9/5) + 32
    elif unit == 'K':
        return value + 273.15
    else:
        return "Invalid unit"

api_temperature = 30  # Celsius

fahrenheit = convert_temperature(api_temperature, 'F')
print(f"Current temperature: {fahrenheit}°F")

kelvin = convert_temperature(api_temperature, 'K')
print(f"Current temperature: {kelvin} K")
