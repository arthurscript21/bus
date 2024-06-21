asiento=10000
descuento=0
import csv
cliente = []
import os, time, csv
bus = [["O" for x in range(1, 6)] for y in range(7)]

def mostrar_bus():
    for fila in bus:
        print(fila)

def comprar_asiento():

    fila_asiento = int(input("ingrese la fila: "))
    columna_asiento = int(input("ingrese la columna: "))
    if bus[fila_asiento-1][columna_asiento-1]=="x":
        return fila_asiento, columna_asiento
    else:
        bus[fila_asiento-1][columna_asiento-1]="x"
        print("fue resevado con exito")
        

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    telefono =int(input("Ingrese su numero: "))
    if edad < 18:
        descuento = asiento * 0.2
        total_pagar = asiento - descuento
    elif edad > 65:
        descuento = asiento * 0.15
        total_pagar = asiento - descuento
    else:
        total_pagar = asiento
    
    persona = {
        "fila":fila_asiento,
        "columna":columna_asiento,
        "nombre":nombre,
        "edad":edad,
        "telefono":telefono,
        "pagar":total_pagar
        
    }
    cliente.append(persona)

def Mostrar_vent():
    for lulo in cliente:
        print(f"fila: {lulo['fila']} columna: {lulo['columna']} nombre: {lulo['nombre']} edad: {lulo['edad']} telefono: {lulo['telefono']} pagar: {lulo['total_pagar']}")

def arch_csv():
    with open("digy.csv", "w", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerow(cliente)


def terminar():
    print("adios")
    exit()