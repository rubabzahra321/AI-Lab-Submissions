def convert_temperature(value, to_unit="Fahrenheit"):
    if to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif to_unit == "Kelvin":
        return value + 273.15

    
result1 = convert_temperature(25)
result2 = convert_temperature(25, "Kelvin")
result3 = convert_temperature(value=100, to_unit="Kelvin")
print("25C in Fahrenheit (default):" , result1)
print("25C in Kelvin:" , result2)
print("100C in Kelvin:" , result3)