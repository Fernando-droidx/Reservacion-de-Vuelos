import csv 

def mostrar_vuelos():
    with open('vuelos.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        print("Leyendo el csv: ")
        for row in reader:
            print("Número de vuelo:", row[0])
            print("Aerolínea:", row[1])
            print("Origen:", row[2])
            print("Destino:", row[3])
            print("Hora de salida:", row[4])
            print("Hora de llegada:", row[5])
            print("Duración:", row[6])
            print("Precio:", row[7])
            print("----------------------------------") 
        
def reservar_vuelo(origen, destino, nombre):
    vuelos_usuario = []
    with open('vuelos.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if origen == row[2] and destino == row[3]:
                des = input("¿Quieres reservar? (y/n): ").lower()  
                if des == 'y':
                    vuelos_usuario = row
                    print("Reservado a nombre de: ", nombre)
                    print("Número de vuelo:", vuelos_usuario[0])
                    print("Aerolínea:", vuelos_usuario[1])
                    print("Origen:", vuelos_usuario[2])
                    print("Destino:", vuelos_usuario[3])
                    print("Hora de salida:", vuelos_usuario[4])
                    print("Hora de llegada:", vuelos_usuario[5])
                    print("Duración:", vuelos_usuario[6])
                    print("Precio:", vuelos_usuario[7])
                    break
                elif des == 'n':
                    print("Sale del programa")
                    break
        else:
            print("No se encontraron vuelos disponibles para esa ruta.")

def menu():
    print("Bienvenido a AeroFer esta es la redservacion de vuelos\n")
    print("1- Mostrar vuelos disponibles ")
    print("2- Reservar un vuelo ")
    choose = input("Elige una opción (1/2): ")
    return choose

if __name__ == '__main__':
    while True:
        opcion = menu()
        if opcion == '1':
            mostrar_vuelos()
        elif opcion == '2':
            nombre = input("Ingresa tu nombre: ")
            origen = input("Ingresa tu origen: ")
            destino = input("Ingresa tu destino: ")
            reservar_vuelo(origen, destino, nombre)
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            salir = input("¿Quieres salir del programa? (y/n): ").lower()
            if salir == 'y':
                print("¡Hasta luego!")
                break
