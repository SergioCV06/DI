from operaciones import suma, resta, multiplicacion, division

continuar = "s"

while continuar == "s":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(suma(a, b))
    elif opcion == "2":
        print(resta(a, b))
    elif opcion == "3":
        print(multiplicacion(a, b))
    elif opcion == "4":
        print(division(a, b))
    else:
        print("Opción no válida")

    continuar = input("¿Quieres hacer otra operación? (s/n): ")

print("Fin del programa")
