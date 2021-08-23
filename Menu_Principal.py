from io import open
from tkinter import filedialog


class menu:

    def op(self):
        bandera = True
        while bandera:
            print("----Menu principal----")
            print("Elija una opcion: ")
            print("1. Cargar Archivo \n"
                  "2. Procesar Archivo \n"
                  "3. Escribir archivo salida \n"
                  "4. Mostras Datos del estudiante \n"
                  "5. Generar Grafica \n"
                  "6. salida")

            opcion = int(input())

            if opcion == 1:
                print("Carga del archivo")
                with open(filedialog.askopenfilename(), encoding="utf-8") as fname:
                    carga = fname.readlines()
                    c=len(carga)


            elif opcion == 2:
                print("")

            elif opcion == 3:
                print("")
            elif opcion == 4:
                print("-------DATOS DEL ESTUDIANTE--------")
                print("> Diana Magaly Fuentes Garcia \n" +
                    "> 201801208 \n"+
                    "> Introduccion a la programacion y computacion 2 seccion C \n" +
                    "> ingenieria en ciencias y sistemas"+
                    "> 4to Semestre")

            elif opcion == 5:
                print("")

            elif opcion == 6:
                print("Salida")
                bandera = False

menu().op()