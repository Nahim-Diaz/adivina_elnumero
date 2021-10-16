import random

def main():
    mensaje = """Bienvenido, el juego consiste en tratar de adivinar un numero del 1 al 100
Al princiìp tienes 10 vidas, si te quedas sin vidas perderás :c
Suerte!"""
    print(mensaje)
    ramdon = random.randint(1, 100)
    vidas = 10
    numero = int(input("Escribe un numero del 1 al 100: "))
    while numero != ramdon:
        if numero < ramdon:
            print("Elige un numero más grande")
            vidas-=1
            print(f"Tienes {vidas} vidas")
        elif numero > ramdon:
            print("Elige un numero más pequeño")
            vidas -=1
            print(f"Tienes {vidas} vidas")
        if vidas == 0:
            print("Perdiste :c suerte para la proxima")
            break
        numero = int(input("Escribe otro numero: "))
    if vidas !=0: 
        print("Felicidades Ganaste")
    

if __name__ == "__main__":
    main()