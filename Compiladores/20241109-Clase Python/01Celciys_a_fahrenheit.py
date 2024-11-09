#Conversión de Celsius a Fahtrenheit
def celcius_a_fahrenheit(celcius):
    return (celcius * 9/5)+32

#Solicitar al usuario la temperatura en Celcius
celcius = float(input("Ingrese la temperatura en Celcius: "))

#Convertur y mostrar el resultado
fahrenheit = celcius_a_fahrenheit(celcius)
print(f"{celcius} °C es igual a {fahrenheit} °F")
