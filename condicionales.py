"""
Vamos a hacer un programa que nos diga el sueldo a recibir de un empleado, si gana menos de 2.000.000 de pesos
le vamos a dar un subsidio de 200.000
"""
"""
nombre = input("Ingresa tu nombre: ")
sueldo = int(input("Ingrese el sueldo del empleado: "))
if sueldo > 2000000:
    sueldo += 200000
    print(f"Felicitaciones {nombre} disfruta adicional tu subsidio de $200.000, valor a pagar: $", sueldo)
else: print("sueldo a pagar es: ", sueldo)

"""

"""
Escribir un programa en python y determine si es mayor de edad o no
si la edad es mayor o igual a 18, el programa debe imprimir "Eres mayor de edad"
en caso contrario debe imprimir "eres menor de edad"
"""
"""
nombre = input("Ingresa tu nombre: ")

try:
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print(f"Hola {nombre} eres mayor de edad")
    else: 
        print(f"{nombre} eres menor de edad")

except ValueError:
    print("Error ingresa tu edad usando numeros.")
    
"""

"""
De 0 a 5 primera infancia
de 6 a 12 infancia
de 13 a 17 adolesencia
mayor o igual a 18 adultez
"""

"""
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <=5:
    print("Primera infancia")
elif edad >= 6 and edad <= 12:
    print("Infancia")
elif edad >= 13 and edad <= 17:
    print("Adolecencia")
else: 
    print("Adultez")

"""

"""
Escribir un programa en python que solicite al usuario un numero entre 1 y 7
si es 1 imprimir "Lunes"
si es 2 imprimir "Martes"
si es 3 imprimir "Miercoles"
si es 4 imprimir "Jueves"
si es 5 imprimir "Viernes"
si es 6 imprimir "Sabado"
si es 7 imprimir "Domingo"
y si el numero no esta entre 1 y 7 imprimir "Numero no valido"
"""
"""
dia_sem = int(input("Ingrese un numero entre 1 a 7 "))

try:   
    
    if dia_sem <= 0:
        print("Numero no valido")
    elif dia_sem == 1:
        print("Lunes")        
    elif dia_sem == 2:
        print("Martes")
    elif dia_sem == 3:
        print("Miercoles")
    elif dia_sem == 4:
        print("Jueves")
    elif dia_sem == 5:
        print("Viernes")
    elif dia_sem == 6:
        print("Sabado")
    elif dia_sem == 7:
        print("Domingo")
    else:
        print("Numero no valido")

except ValueError:
    print("Error ingresa solo numeros")

"""
"""
day = input("Ingresa un numero (1-7): ")

match day:
    case "1":
        print("Lunes")
    case "2":
        print("Martes")
    case "3":
        print("Miercoles")
    case "4":
        print("Jueves")
    case "5":
        print("Viernes")
    case "6":
        print("Sabado")
    case "7":
        print("Domingo")
    case _:
        print("Numero no valido")
"""

"""
preguntar al usuario un animal (perro, gato, pez)
si el animal es perro imprimir "Guau"
si el animal es gato imprimir "Miau"    
si el animal es pez imprimir "Blub"
y si el animal no es ninguno de esos imprimir "Animal no reconocido"
"""
perro = 1
gato = 2
pez = 3

animal = input("Escoge un numero (1-3) ")

match animal:
    case "1":
        print("guawww\n")    
    case "2":
        print("Miauuuu\n")    
    case "3":
        print("blub\n")    
    case _:
        print("Numero no valido")    



