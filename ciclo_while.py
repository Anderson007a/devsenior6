menu = """
    Restaurante el buen sabor
    1. Hamburguesa - $20.000
    2. Pizza - $7.500
    3. Ensalada - $4.500
    4. Salchipapa - $8000
    5. Perro Caliente - $12.000
    6. Salir   
    """

    
menu = """
1. Hamburguesa ($20.000)
2. Pizza ($7.500)
3. Ensalada ($4.500)
4. Salchipapa ($8.000)
5. Perro Caliente ($12.000)
6. Salir y Ver Factura
"""

print(menu)
total_cuenta = 0
cantidadHamburguesas = 0 
cantidadPizza = 0
cantidadEnsalada = 0 
cantidadSalchipapa = 0
cantidadPerro_Caliente = 0

opcion = 0
while opcion != 6:
    opcion = int(input("\nIngrese una opcion del menu: "))
    if opcion == 1:
        print("Has elegido hamburguesa")
        total_cuenta += 20000
        cantidadHamburguesas += 1     
    elif opcion == 2:
        print("Has elegido Pizza")
        total_cuenta += 7500    
        cantidadPizza += 1
    elif opcion == 3:
        print("Has elegido Ensalada")
        total_cuenta += 4500
        cantidadEnsalada += 1    
    elif opcion == 4:
        print("Has elegido Salchipapa")
        total_cuenta += 8000 
        cantidadSalchipapa += 1   
    elif opcion == 5:
        print("Has elegido Perro Caliente")
        total_cuenta += 12000
        cantidadPerro_Caliente += 1    
    elif opcion == 6: 
        # Calculamos los totales antes de imprimir
        totalHamburguesas = cantidadHamburguesas * 20000
        totalPizza = cantidadPizza * 7500
        totalEnsalada = cantidadEnsalada * 4500
        totalSalchipapa = cantidadSalchipapa * 8000
        totalPerro = cantidadPerro_Caliente * 12000
        
        print("\n--- FACTURA FINAL ---")
        print(f"Hamburguesas: {cantidadHamburguesas} | Subtotal: ${totalHamburguesas}")
        print(f"Pizzas:       {cantidadPizza} | Subtotal: ${totalPizza}")
        print(f"Ensaladas:    {cantidadEnsalada} | Subtotal: ${totalEnsalada}")
        print(f"Salchipapas:  {cantidadSalchipapa} | Subtotal: ${totalSalchipapa}")
        print(f"Perros Cal.:  {cantidadPerro_Caliente} | Subtotal: ${totalPerro}")
        print("---------------------")
        print(f"TOTAL A PAGAR: ${total_cuenta}")
        break    
    else: 
        print("Opcion no valida en el menu")
            
print(menu)