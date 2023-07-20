import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("titulo", "ingrese apellido")

        while (apellido == None or apellido == "") or not apellido.isalpha():
            apellido = prompt("Titulo", "Reingrese apellido")

        edad = prompt(title="edad",prompt= "ingrese su edad")
        while edad == None or not edad.isdigit() or int(edad) < 18 or int(edad) > 90:
            edad = prompt(title="edad",prompt= "ingrese una edad valida")
        edad = int(edad)

        estado_civil = prompt("Titulo", "Ingrese su estado civil").capitalize()
        while (estado_civil == None or not estado_civil.isalpha()) or estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Divorciado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda" :
            estado_civil = prompt("Titulo", "ReIngrese su estado civil [ Soltero/a, Divorciado/a, Casado/a, Viudo/a]")
        
        if estado_civil == "Soltero" or estado_civil == "Soltera":
            estado_civil = "Soltero/a"
        elif estado_civil == "Casado" or estado_civil == "Casada":
            estado_civil = "Casado/a"
        elif estado_civil == "Divorciado" or estado_civil == "Divorciada":
            estado_civil = "Divorciado/a"
        else:
            estado_civil = "Viudo/a"

        legajo = prompt(title="legajo",prompt= "ingrese su legajo")
        while legajo == None or not legajo.isdigit() or int(legajo) < 1000 or int(legajo) > 9999:
            legajo = prompt(title="legajo",prompt= "ingrese una legajo valida")
        legajo = int(legajo)

        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, edad)
        self.combobox_tipo.set(estado_civil)
        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, legajo)






        """  apellido = prompt("titulo", "ingrese apellido")

        while (apellido == None or apellido == "") or not apellido.isalpha():
            apellido = prompt("Titulo", "Reingrese apellido") """
        """ while True:
            while edad == None or not edad.isdigit():
                edad = prompt("Titulo", "Reingrese su edad")
                if edad != None and edad.isdigit():
                    edad = int(edad)
                    break
                else:
                    continue """


            





















        """ apellido = prompt("Toma de datos", "Ingrese su apellido").capitalize()
        while apellido == None or apellido.isdigit():
            apellido = prompt("Toma de datos", "ReIngresa tu apellido").capitalize()
            if apellido != None and apellido.isalpha():
                break
            else:
                continue
                  
        edad = prompt("Toma de datos", "Ingrese su edad")
        bandera_edad = edad
        while True:
            while bandera_edad == None or not bandera_edad.isdigit():
                edad = prompt('validar', 'Reingrese su edad')
                if edad != None and edad.isdigit() :
                    edad = int(edad)
                    break
                else:
                    continue
            edad = int(edad)
            while edad < 18 or edad > 90:
                edad = prompt('validar', 'bandera_legajoSu edad no esta al alcance del rango solicitado')
                bandera_edad = edad
                while bandera_edad == None or not bandera_edad.isdigit():
                    edad = prompt('validar', 'ingrese su edad en numeros')
                    if edad != None and edad.isdigit():
                        edad = int(edad)
                        break
                    else:
                        continue 
                edad = int(edad)
            break


        estado_civil = prompt("Toma de datos", "Ingrese su estado civil ['Soltero/a', 'Casado/a', 'Divorciado/a', 'Viudo/a']").capitalize()
        bandera_civil = estado_civil
        while True:
            while bandera_civil == None and not bandera_civil.isalpha():
                estado_civil = prompt('validar',"ReIngrese su estado civil ['Soltero/a', 'Casado/a', 'Divorciado/a', 'Viudo/a']").capitalize()
                if estado_civil != None and estado_civil.isalpha():
                    break
                else:
                    continue
            while estado_civil != "Soltero/a" and estado_civil != "Divorciado/a" and estado_civil != "Casado/a" and estado_civil != "Viudo/a":
                estado_civil = prompt('validar', "ReIngrese su estado civil ['Soltero/a', 'Casado/a', 'Divorciado/a', 'Viudo/a']").capitalize()
                bandera_civil = estado_civil
                while bandera_civil == None or not bandera_civil.isalpha():
                    estado_civil = prompt('validar', "ReIngrese su estado civil ['Soltero/a', 'Casado/a', 'Divorciado/a', 'Viudo/a']").capitalize()
                    if estado_civil != None and estado_civil.isalpha():
                        break
                    else:
                        continue 
            break

        
        legajo = prompt("Toma de datos", "Ingrese su legajo")
        bandera_legajo = legajo
        while True:
            while bandera_legajo == None or not bandera_legajo.isdigit():
                    legajo = prompt('validar', 'ingrese su legajo en numeros')
                    if legajo != None and legajo.isdigit():
                        legajo = int(legajo)
                        break
                    else:
                        continue 
            legajo = int(legajo)
            while legajo < 1000 or legajo > 9999:
                legajo = prompt('validar', 'Su legajo no esta al alcance del rango solicitado')
                bandera_legajo = legajo
                while bandera_legajo == None or not bandera_legajo.isdigit():
                    legajo = prompt('validar', 'ingrese su legajo en numeros')
                    if legajo != None and legajo.isdigit():
                        legajo = int(legajo)
                        break
                    else:
                        continue 
                legajo = int(legajo)
            break

        
        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, edad)
        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, legajo)
        self.combobox_tipo.set(estado_civil)
        

"""
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
