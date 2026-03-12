"""
Escribir un programa que pida al usuario dos numeros y muestre un menu de opciones
suma, resta, multiplicacion y division
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo (residuo de la division)
8. Salir



"""

operacion = """
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo (residuo de la division)
8. Salir
"""
print(operacion)

try:
    
    opcion = 0
    while opcion != 7:
        opcion = int(input("\nIngrese una opcion del menu: "))
        if opcion == 1:
            print(f"Haz eligido una suma")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            su_m = n1 + n2
            print(f"El resultado de la suma es {su_m}")
        elif opcion == 2:
            print(f"Haz eligido una resta")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            res = n1 - n2
            print(f"El resultado de la resta es {res}")        
        elif opcion == 3:
            print(f"Haz eligido una multipliacion")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            mult = n1 * n2
            print(f"El resultado de la multiplicación es {mult}")        
        elif opcion == 4:
            print(f"Haz eligido una division")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            div = n1 / n2
            print(f"El resultado de la division es {div}")        
        elif opcion == 5:
            print(f"Haz eligido una division entera")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            divEnt = n1 // n2
            print(f"El resultado de la division entra es {divEnt}")        
        elif opcion == 6:
            print(f"Haz eligido una potencia")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            pot = n1 ** n2
            print(f"El resultado de la potencia es {pot}")        
        elif opcion == 7:
            print(f"Haz eligido el modulo")
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            mod = n1 % n2
            print(f"El resultado del modulo es {mod}")               
        elif opcion == 8:
            print(f"Gracias por usar la calculadora")    
            break
        else:
            print("Opcion no valida")
            
        print(operacion)
except ValueError:
    print("Ingresa solo valores numericos")