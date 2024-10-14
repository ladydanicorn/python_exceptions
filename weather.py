#Task 1

fahrenheit_temperature = input("Please enter current temperature in Fahrenheit: ")

#Task 2
def celsius_convert(fahrenheit_temperature):
    try:
        celsius_temperature = (float(fahrenheit_temperature) - 32) * (5/9)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    #Task 3
    else:
        print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature:.2f} degrees Celsius")
        return celsius_temperature
    #Task 4
    finally:
        print("Thank you for using the weather forecast app!")

celsius_convert(fahrenheit_temperature)

