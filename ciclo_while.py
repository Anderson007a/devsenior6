menu = """
    Restaurante el buen sabor
    1. Hamburguesa
    2. Pizza
    3. Ensalada
    4. Salchipapa
    5. Perro Caliente
    6. Salir   
    """
    
print(menu)
opcion = 0
while opcion != 6:
    opcion = int(input("Ingrese una opcion del menu "))
    if opcion == 1:
        print("Haz elegido hamburguesa")    
    elif opcion == 2:
        print("Haz elegido Pizza")    
    elif opcion == 3:
        print("Haz elegido Ensalada")    
    elif opcion == 4:
        print("Haz elegido Salchipapa")    
    elif opcion == 5:
        print("Haz elegido Perro Caliente")    
    elif opcion == 6: 
        print("Gracias por visitar el restaurante el buen sabor hasta luego")
        break    
    else: 
        print("Opcion no valida en el menu")
            
print(menu)