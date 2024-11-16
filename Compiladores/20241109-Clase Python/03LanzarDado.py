import random

def lanzar_dado():
    return random.randint(1, 6)
print("Bienvenido al lanzador de dados virtual.")

while True:
    respuesta = input("¿Quiere lanzar el dado? (si/no): ").strip().lower()

    if respuesta == "si":
        resultado = lanzar_dado()
        print(f"Has lanzado el dado y ha sido: {resultado}")
    elif respuesta == "no":
        print("Gracias por jugar. !Hasta la próxima!")
        break
    else:
        print("Por favor, responder 'si' o 'no'")