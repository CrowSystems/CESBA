def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

cantidad = float(input("Ingresa la temperatura: "))
escala = input("Ingrese la escala de la temperatura (C para Celsius, F para Fahrenheit): ")

if escala == 'C':
    resultado = celsius_a_fahrenheit(cantidad)
    print(f"{cantidad}°C es igual a {resultado}°F")
elif escala == 'F':
    resultado = fahrenheit_a_celsius(cantidad)
    print(f"{cantidad}°F es igual a {resultado}°C")
else:
    print("Escala no válida. Por Favor ingrese 'C' o 'F'.") 