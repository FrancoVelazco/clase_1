import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")



    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio = cantidad * 800
        descuento = 0

# FORMA 3 (match)

"""         match cantidad:
            case 5:
                  match marca:
                        case "ArgentinaLuz":
                            descuento = 40
                        case _:
                            descuento = 30
            case 4:
                  match marca:
                        case "ArgentinaLuz" | "FelipeLuz":
                            descuento = 25
                        case _:
                            descuento = 20
            case 3:
                  match marca:
                        case "ArgentinaLuz":
                            descuento = 15
                        case "FelipeLamparas":
                            descuento = 10
                        case _:
                            descuento = 5
            case 2 | 1:
                  descuento = 0
            case _:
                  descuento = 50


        precio = precio - (precio * descuento / 100)

        if precio >= 4000:
            precio = precio - (precio * 5 / 100)

        alert("Información", f"El precio total es: {precio}") """
        







        
        # FORMA 2 (ELIF)
        
        
        
"""
    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)
        precio = cantidad * 800
        descuento = 0

        if cantidad > 5:
             descuento = 50
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                  descuento = 40
            else:
             descuento = 30
        elif cantidad == 4:
            if marca == "ArgentinaLUZ" or marca == "FelipeLamparas":
                descuento = 25
            else:
                descuento = 20
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                descuento = 15
            elif marca == "FelipeLamparas":
                descuento = 10
            else:
                descuento = 5

        precio = precio - (precio * descuento / 100)

        if precio >= 4000:
            precio = precio - (precio * 5 / 100)

        alert("Información", f"El precio total es: {precio}")

"""



#          FORMA 1 (IF)



"""

    def btn_calcular_on_click(self):
        # TOMA DE DATOS
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad)
        precio = cantidad * 800
        descuento = 0

        if cantidad > 5:
            descuento = 50
        else:
            if cantidad == 5:
                if marca == "ArgentinaLuz":
                    descuento = 40
                else:
                    descuento = 30
            else:
                if cantidad == 4:
                    if marca == "ArgentinaLuz" or  marca == "FelipeLamparas":
                        descuento = 25
                    else:
                        descuento = 20
                else:
                    if cantidad == 3:
                        if marca == "ArgentinaLuz":
                            descuento = 15
                        else:
                            if marca == "FelipeLamparas":
                                descuento = 10
                            else:
                                descuento = 5

        precio = precio - (precio * descuento / 100)

        if precio >= 4000:
            precio = precio - (precio * 5 / 100)

        alert("Información", f"El precio total es: {precio}")

"""      
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()