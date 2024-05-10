import tkinter as tk
import csv
from tkinter import messagebox

def mostrar_vuelos():
    for widget in frame_vuelos.winfo_children():
        widget.destroy()

    listbox_vuelos = tk.Listbox(frame_vuelos, width=100, height=10)
    listbox_vuelos.pack()

    with open('vuelos.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            info_vuelo = f"{row[0]} - {row[1]} - {row[2]} a {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]}"
            listbox_vuelos.insert(tk.END, info_vuelo)

def reservar_vuelo():
    global entry_nombre, entry_origen, entry_destino
    nombre = entry_nombre.get()
    origen = entry_origen.get()
    destino = entry_destino.get()

    for widget in frame_reserva.winfo_children():
        widget.destroy()

    listbox_reserva = tk.Listbox(frame_reserva, width=100, height=10)
    listbox_reserva.pack()
    vuelos_usuario = []
    with open('vuelos.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        vuelo_encontrado = False
        for row in reader:
            if origen == row[2] and destino == row[3]:
                vuelo_encontrado = True
                confirmacion = messagebox.askquestion("Confirmar reserva", f"¿Quieres reservar el vuelo {row[0]}?")  
                if confirmacion == 'yes':
                    vuelos_usuario = row
                    vuelo_info = f"{row[0]} - {row[1]} - {row[2]} a {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]}"
                    listbox_reserva.insert(tk.END, vuelo_info)
                    break
                else:
                    messagebox.showinfo("Info", "Reserva cancelada")
                    break
        if not vuelo_encontrado:
            messagebox.showinfo("Info", "No se encontraron vuelos disponibles para esa ruta.")

def mostrar_menu():
    root.destroy()

def main():
    global root, entry_nombre, entry_origen, entry_destino, frame_vuelos, frame_reserva
    root = tk.Tk()
    root.geometry("800x600")
    root.title("AeroFer - Reserva de vuelos")

    label_nombre = tk.Label(root, text="Nombre:")
    label_nombre.grid(row=0, column=0)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1)

    label_origen = tk.Label(root, text="Origen:")
    label_origen.grid(row=1, column=0)
    entry_origen = tk.Entry(root)
    entry_origen.grid(row=1, column=1)

    label_destino = tk.Label(root, text="Destino:")
    label_destino.grid(row=2, column=0)
    entry_destino = tk.Entry(root)
    entry_destino.grid(row=2, column=1)

    # Botones para mostrar vuelos
    btn_mostrar_vuelos = tk.Button(root, text="Mostrar vuelos disponibles", command=mostrar_vuelos)
    btn_mostrar_vuelos.grid(row=3, column=0, pady=20)

    btn_reservar_vuelo = tk.Button(root, text="Reservar vuelo", command=reservar_vuelo)
    btn_reservar_vuelo.grid(row=3, column=1, pady=20)

    btn_mostrar_menu = tk.Button(root, text="Salir", command=mostrar_menu)
    btn_mostrar_menu.grid(row=3, column=2, pady=20)

    # Frame para mostrar los vuelos
    frame_vuelos = tk.Frame(root)
    frame_vuelos.grid(row=4, column=0, columnspan=3)

    # Frame para mostrar la reserva
    frame_reserva = tk.Frame(root)
    frame_reserva.grid(row=5, column=0, columnspan=3)

    root.mainloop()

if __name__ == '__main__':
    main()
