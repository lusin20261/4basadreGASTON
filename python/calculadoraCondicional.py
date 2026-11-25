print("......................................................")
print("         Bienvenido a mi CALCULADORA                  ")
print("......................................................")

while True: 
    print("")
    print("¿Qué operacion quieres realizar?")
    print("1) Sumar")
    print("2) Restar")
    print("3) Dividir")
    print("4) Multiplicar")
    print("5) Salir")
    print("................................")

    Opcion = input("Elige una opcion: ")

    if opcion == "1": 
        num1 = input("ingresa el primer numero")
        num1 = int(num1)
        num2 =("ingresa en segundo numero")
        num2 = int(num2)
        print("El resultado de la suma es:",num1 + num2)

    elif opcion  == "2": 
        