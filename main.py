import csv 
#verfica si esxiste

def menu():
    print("Bienvenido a AeroFer esta es la redservacion de vuelos\n")
    print("1- Vuelos disponibles ")
    print("2- Reservar un vuelo ")

    choose = int(input())
    if choose == 1:
        Existencias()
    elif choose == 2:

        Nombre = input("Ingresa tu nombre: ")
        Origen = input("Ingresa tu origen: ")
        Destino = input("Ingresa tu destino: ")
        reservar_vuelo(Origen, Destino, Nombre)
    else:
        print("Ni siquiera es una opcion")
def Existencias():
    with open('vuelos.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        print("Leyendo el csv: " + str(reader))
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
            menu()
def reservar_vuelo(origen, destino, nombre):
    vuelos_usuario = []
    with open('vuelos.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if origen == row[2] and destino == row[3]:
                des = input("Quieres reserva? y/n").lower()  
                if des == 'y':
                    vuelos_usuario.append(row[0])
                    vuelos_usuario.append(row[1])
                    vuelos_usuario.append(row[2])
                    vuelos_usuario.append(row[3])
                    vuelos_usuario.append(row[4])
                    vuelos_usuario.append(row[5])
                    vuelos_usuario.append(row[6])
                    vuelos_usuario.append(row[7])
                    print("Reservado a nombre de: ", nombre)
                    print("Número de vuelo:", vuelos_usuario[0])
                    print("Aerolínea:", vuelos_usuario[1])
                    print("Origen:", vuelos_usuario[2])
                    print("Destino:", vuelos_usuario[3])
                    print("Hora de salida:", vuelos_usuario[4])
                    print("Hora de llegada:", vuelos_usuario[5])
                    print("Duración:", vuelos_usuario[6])
                    print("Precio:", vuelos_usuario[7])
                    
                    
                elif des == 'n':
                    print("Sale del programa")
                    menu()



