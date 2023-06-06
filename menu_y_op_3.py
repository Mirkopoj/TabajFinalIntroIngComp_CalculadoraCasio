import conversiones as con

# considerar usar el clear para la calculadora
calc_On = True
expresion = 0
boton = 1

#--------------------- MENU -----------------------------------------------------------
#                                    8b    d8  888888  88b 88  88   88 
#                                    88b  d88  88__    88Yb88  88   88 
#                                    88YbdP88  88""    88 Y88  Y8   8P 
#                                    88 YY 88  888888  88  Y8  `YbodP' 

while boton != 0:
    print(" 0 -> ON ")
    boton = int(input("\n_"))

while calc_On == True:
    print("Menu: ")
    print("1- Calculadora clásica")
    print("2- Calculadora fraccionaria")
    print("3- Calculadora de conversiones") 
    print("4- Apagar calculadora")

    select = int(input("\n_"))

    if select == 1:
        print(" pasan cosas")
    elif select == 2: 
        print("pasan cosas 2")
    elif select == 3: 

        print("Ingrese expresión: ") 
        expresion = int(input("\n_"))
        #valida que sea una opcion valida
        while expresion < 0 or expresion > 9999:
            print("\nIngrese un numero valido ")
            expresion = int(input("\n_"))

        lista_convertido = con.conversiones(expresion)
        print(f"Conversión: {lista_convertido} ")

    elif select == 4:
        calc_On = False
        print("\n\nApagando...")
    else:
        print("Error ingrese una opción válida")
    
