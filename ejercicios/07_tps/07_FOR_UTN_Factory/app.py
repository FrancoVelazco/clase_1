'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).

e. Porcentaje de postulantes de cada genero. # hombres * 100 (%) / total

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        
        contador_no_binario = 0
        flag_menor_jr = True
        menor_edad_jr = 0
        acumulador_nb = 0
        contador_nb = 0
        acumulador_m = 0
        contador_m = 0
        acumulador_f = 0
        contador_f = 0
        contador_js = 0
        contador_python = 0
        contador_asp = 0
        tecnologia_mas_postulantes = None



        for i in range(10):
            nombre = prompt("Toma de datos", "Ingrese un nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("Validación", "Ingrese un nombre con letras")
            
            edad = prompt("Toma de datos", "Ingrese una edad")
            while edad == None or not edad.isdigit() or int(edad) < 18 or int(edad) > 90:
                edad = prompt("Validación", "Ingrese una edad valida")
            
            edad = int(edad)

            genero = prompt("Toma de datos", "Ingres el genero [F-M-NB]")
            while genero == None or genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("Validación", "Ingrese un genero valido [F-M-NB]")
            
            tecnologia = prompt("Toma de datos", "Ingrese la tecnologia usada [PYTHON - JS - ASP.NET]")
            while tecnologia == None or tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("validación", "Ingrese una tecnologia usada valida [PYTHON - JS - ASP.NET]")
            
            puesto = prompt("Toma de datos", "Ingrese puesto [Jr - Ssr - Sr]")
            while puesto == None or puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("validación", "Ingrese un puesto valido [Jr - Ssr - Sr]")

            if genero == "NB":
                if tecnologia == "ASP.NET" or tecnologia == "JS" and edad > 25 and edad < 40 and puesto == "Ssr":
                    contador_no_binario += 1

                acumulador_nb += edad
                contador_nb +=1
            elif genero == "M":
                acumulador_m += edad
                contador_m += 1
            else:
                acumulador_f += edad
                contador_f += 1

            
            if puesto == "Jr":
                if flag_menor_jr or edad < menor_edad_jr:
                    menor_edad_jr = edad
                    nombre_menor_jr = nombre
                    flag_menor_jr = False

            if tecnologia == "JS":
                contador_js += 1
            elif tecnologia == "PYTHON":
                contador_python += 1
            else:
                contador_asp += 1





        promedio_nb = acumulador_nb / contador_nb
        promedio_m = acumulador_m / contador_m
        promedio_f = acumulador_f / contador_f

        if contador_asp > contador_js and contador_asp > contador_python:
            tecnologia_mas_postulantes = "ASP.NET"
        elif contador_js > contador_python and contador_js > contador_asp:
            tecnologia_mas_postulantes = "JS"
        else:
            tecnologia_mas_postulantes = "PYTHON"

        porcentaje_nb = contador_nb * 100 / 10
        porcentaje_m = contador_m * 100 / 10
        porcentaje_f = contador_f * 100 / 10
        
        print(f"Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr son: {contador_no_binario}")
        print(f"Nombre del postulante Jr con menor edad: {nombre_menor_jr}")
        print(f"Promedio de edades por género:\nEl promedio de NoBinario es: {promedio_nb}\nEl Promedio de Masculo es: {promedio_m}\nEl promedio de Femenino es: {promedio_f}")
        print(f"Tecnologia con mas postulantes es: {tecnologia_mas_postulantes}")
        print(f"El porcentaje de postulantes Nobinarios es de: {porcentaje_nb}%\nEl porcentaje de postulantes Masculinos es de: {porcentaje_m}%\nEl porcentaje de postulantes femeninos es de: {porcentaje_f}%")
#         Informar por pantalla:
# a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
# cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
# b. Nombre del postulante Jr con menor edad.
# c. Promedio de edades por género.
# d. Tecnologia con mas postulantes (solo hay una).

# e. Porcentaje de postulantes de cada genero. # hombres * 100 (%) / total


            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
