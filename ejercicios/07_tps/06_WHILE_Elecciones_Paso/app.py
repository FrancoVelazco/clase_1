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
        flag_mas_votos = True
        flag_menos_votos = True
        continuar = True
        mas_votos = 0
        menos_votos = 0
        edad_menos_votos = 0
        acumulador_edades = 0
        total_votos = 0
        contador_edades = 0
        nombre_mas_votos = None
        nombre_menos_votos = None
        while True:
            nombre = prompt("Nombre", "Ingrese el Nombre del candidato")
            while (nombre == None or nombre == "") or not nombre.isalpha():
                nombre = prompt("Titulo", "Reingrese nombre")

            edad = prompt("edad", "ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 25 or int(edad) > 90:
                edad = prompt("edad", "Ingrese una edad valida")
            edad = int(edad)

            votos = prompt("Votos", "Ingrese la cantidad de votos que recibio el candidato")
            while votos == None or not votos.isdigit() or int(votos) <= 0:
                votos = prompt("Votos", "Ingrese una cantidad valida de votos que recibio el candidato")
            votos = int(votos)

            if flag_mas_votos or votos > mas_votos:
                flag_mas_votos = False
                mas_votos = votos
                nombre_mas_votos = nombre
            elif flag_menos_votos or votos < menos_votos:
                flag_menos_votos = False
                menos_votos = votos
                nombre_menos_votos = nombre
                edad_menos_votos = edad

            acumulador_edades += edad
            contador_edades += 1
            total_votos += votos
            
            continuar = question("Titulo", "¿Desea seguir ingresando candidatos?")
            if continuar == True:
                continue
            else:
                break
        
        promedio_edades = acumulador_edades / contador_edades

        print(f"El candidato con mas votos es: {nombre_mas_votos}\nEl nombre y la edad del menos votado es: {nombre_menos_votos}, {edad_menos_votos} años\nEl promedio de edades es: {promedio_edades}\nEl total de votos es de: {total_votos}")

# a. nombre del candidato con más votos     # MAXIMO
# b. nombre y edad del candidato con menos votos    # MINIMO
# c. el promedio de edades de los candidatos   # PROMEDIO
# d. total de votos emitidos.     # TOTAL

            







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
