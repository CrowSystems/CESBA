import random

def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    puntuacion_jugador = 0
    puntuacion_computadora = 0
    print("Bienvenido al juego de piedra, Papel o Tijera!")
    print("Juega 'piedra', 'papel' o 'tijera'. Escribe 'salir' para terminar el juego.")
    
    while True:
        jugador = input("Elige tu opción: ").lower()
        if jugador == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        if jugador not in opciones:
            print("Opción no valida. Por Favor, elige 'piedra', 'papel' o 'tijera'.")
            continue
        computadora = random.choice(opciones)
        print(f"La computadora eligio: {computadora}")
        
        if jugador == computadora:
            print("¡Es un empate!")
        elif(jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
            print("Ganaste esta ronda!")
            puntuacion_jugador += 1
        else:
            print("La computadora gano esta ronda.")
            puntuacion_computadora += 1
            
            print(f"Puntuación - Jugador: {puntuacion_jugador} | Computadora: {puntuacion_computadora}")

juego_piedra_papel_tijera()