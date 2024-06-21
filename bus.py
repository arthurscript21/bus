
from funciones_bus import *
while True:
    print("Programa para haciento de bus")
    print("1. Ver los asientos")
    print("2. Comprar asientos")
    print("3. Mostrar ventas")
    print("4. generar archivo csv con las ventas")
    print("5. Terminar")
    opc = int(input("Ingrese una opcion: "))
    if opc==1:
        mostrar_bus()
    elif opc==2:
        comprar_asiento()
    elif opc==3:
        Mostrar_vent()
    elif opc==4:
        arch_csv()
    elif opc==5:
        terminar()
    