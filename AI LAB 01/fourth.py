
def convertToFahrenheit(Celsius):
    return Celsius *  (9/5)  + 32 

def convertToCelsius(Fahrenheit):
    return (Fahrenheit - 32) * (9 / 5)

cel = float(input("Enter the temperature in Celsius: "))

print ("The Fahrenheit of your input is : " , convertToFahrenheit(cel))


farh = float(input("Enter the temperature in Fahrenheit : "))

print ("The Celsius of your input is : " , convertToCelsius(farh))