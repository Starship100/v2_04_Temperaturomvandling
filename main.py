temp = float(input("Ange en temperatur i grader celsius: "))
farenheit = temp * 9 / 5 + 32
print("Det blir ", farenheit , "grader i farenheit.")

# Version 1
temp = float(input("Ange en temperatur i grader Celsius: "))
farenheit = temp * 9 / 5 + 32
print("Det blir ", farenheit, "grader i Farenheit.")

# Version 2
val = input("Ange temperatur i Fahranheit(f) eller Celsius(c): ")
if val == "c":
    celsius = float(input("Skriv in temperatur i grader Celsius: "))
    # fahrenheit = 1.8 * celsius + 32
    fahrenheit = celsius * 9 / 5 + 32
    print("Det blir ", farenheit, "grader Fahrenheit.")

"""
val = input("Vill du ange temperaturen i Celsius eller Fahrenheit? (C/F): ")

if val == "C":
    celsius = float(input("Skriv in temperaturen i grader Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print(f"Det blir {fahrenheit} grader Fahrenheit.")

"""

# ada