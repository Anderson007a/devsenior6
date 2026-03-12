"""
for x in range(1, 11):
    print(x)
"""
"""
for x in range(5):
    print(x)
"""
"""
for x in range(1, 11, 2):
    print(x)
"""
"""
texto = "Python"
for letra in texto:
    print(letra)
"""
"""
nombre = (input("Ingresa tu nombre: "))
tabla = int(input(f"Ingrese el numero de la tabla que desea: "))

print(nombre, f"Elegiste la tabla de multiplicar del {tabla}")
for x in range (1, 11):
    print(f"{tabla} x {x:2} = {tabla * x:2}")
"""

# for anidado

for i in range(1, 11):
    print("Tabla de", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
     
