'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos     # MAXIMO
b. nombre y edad del candidato con menos votos    # MINIMO
c. el promedio de edades de los candidatos   # PROMEDIO
d. total de votos emitidos.     # TOTAL
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = True
        continuar = True
        contador = 0
        while True:
            nombre = prompt("Nombre", "Ingrese el Nombre del candidato")
            while (nombre == None or nombre == "") or not nombre.isalpha():
                nombre = prompt("Titulo", "Reingrese nombre")

            edad = prompt("edad", "ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 25:
                edad = prompt("edad", "ingrese una edad valida")
            edad = int(edad)




            continuar = question("Titulo", "¿Desea seguir ingresando candidatos?")
            if continuar == True:
                continue
            else:
                break


            







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
