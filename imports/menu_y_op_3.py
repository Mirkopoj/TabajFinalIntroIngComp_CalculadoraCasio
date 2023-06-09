if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

import conversiones as con
import str_to_calculations as stc
import funciones as fn
import simplifica2 as sm

#--------------------- MENU -----------------------------------------------------------
#                                    8b    d8  888888  88b 88  88   88 
#                                    88b  d88  88__    88Yb88  88   88 
#                                    88YbdP88  88""    88 Y88  Y8   8P   
#                                    88 YY 88  888888  88  Y8  `YbodP' 

def run():
    calc_On = True
    expresion = 0
    boton = 1

    print("Calculadora Casio")
    print("Ingrese 0 para encender")
    print()


    while boton != '0':
        print(" 0 -> ON ")
        boton = str(input("\n_"))

    while calc_On == True:
        print("Menu: ")
        print("1- Calculadora clásica")
        print("2- Calculadora fraccionaria")
        print("3- Calculadora de conversiones") 
        print("4- Apagar calculadora")

        select = input("\n_")

        if select == '1' or select == '2':    
            suma = fn.suma_clasica
            resta = fn.resta_clasica
            multiplicacion = fn.multiplicacion_clasica
            division = fn.division_clasica
            fraccion = None
            simplificar = None
            if select == '2':
                print("Usted se ha movido  a la fraccionaria, ingrese una expresión")
                print("del tipo [frac] [op] [frac] [op] ... [op] [frac] =") 
                print("donde las fracciones de denotan a|b, siendo a y b numeros enteros")
                print("y los operadores validos son +, -, * y /")
                suma = fn.suma_fraccionaria
                resta = fn.resta_fraccionaria
                multiplicacion = fn.multiplicacion_fraccionaria
                division = fn.division_fraccionaria
                fraccion = fn.hacer_fraccion
                simplificar = sm.simplify
            else:
                print("Usted ha ingresado a la calculadora clásica, ingrese una expresión") 
                print("del tipo [num] [op] [num] [op] ... [op] [num] =") 
                print("donde los numeros deben ser enteros")
                print("y los operadores validos son +, -, * y /")
            comp = ""
            aux = 'a'
            while aux != ' ':
                comp += input(comp)
                aux = stc.tokenize(comp)
                try:
                    aux = stc.parser(aux, frac=fraccion)
                except:
                    print("SintaxError")
                    comp = ""
                    continue
                if len(aux)>2 and aux[-2] == '=':
                    try:
                        aux = stc.calc(aux, suma, resta, multiplicacion, division, simplificar)
                    except:
                        print("MathError")
                        comp = ""
                        continue

        elif select == '3': 
            print("Usted ha ingresado a la calculadora de conversiones") 
            print("ingrese el numero que desea convertir") 
            print("debe ser un mnumero entero en base decimal, de hasta 4 digitos") 
            expresion = int(input("\n_"))
            #valida que sea una opcion valida
            while expresion < 0 or expresion > 9999:
                print("\nIngrese un numero valido ")
                expresion = int(input("\n_"))

            lista_convertido = con.conversiones(expresion)
            print(f"Conversión: {lista_convertido} ")

        elif select == '4':
            calc_On = False
            print("\n\nApagando...")
        else:
            print("Error ingrese una opción válida")
        
