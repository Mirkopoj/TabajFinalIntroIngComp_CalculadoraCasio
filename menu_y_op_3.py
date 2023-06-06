# considerar usar el clear para la calculadora
calc_On = True
expresion = 0
boton = 1

#--------------------- CONVERSIONES --------------------------------------------------
def conversiones(expresion):
    num = expresion
    opcion = 0
    resultado = 0
    band = True

    while band == True:
        print("\n1- Binario")
        print("2- Hexadecimal")
        print("3- Octal")

        opcion = int(input("\n_"))

        if opcion == 1:
            resultado = binario(num)
            band = False
        elif opcion == 2:
            resultado = hexadecimal(num)
            band = False
        elif opcion == 3:
            resultado = octal(num)
            band = False
        else:
            print("Ingrese un numero valido")
    return resultado

#--------------------- BINARIO ---------------------------------------------------------
def binario(num): 
    actual = num
    aux = 2
    lista=[]

    while aux > 1:
        aux = actual / 2
        lista.append(int(actual % 2))
        actual = aux
    lista = lista_reversa(lista) 
    return lista
#--------------------- HEXADECIMAL --------------------------------------------------
def hexadecimal(num):
    band_H = True
    lista_H=[]
    siguiente_num = 0
    redondeo = 0
    resto = 0 
    inte = 0
    multi = 0 

    while band_H == True:
        siguiente_num = num / 16
        redondeo = int(siguiente_num)
        multi= redondeo * 16 
        resto = num - multi
        inte = int(resto)
        num = siguiente_num  
        lista_H.append(inte)

        if redondeo == 0:
            band_H = False

    i=0 
    j=0
    letras=['A','B','C','D','E','F']
    for i in range(len(lista_H)):
        for j in range(6): # 6 porque va de 0 a 5
            if lista_H[i] == (j+10):
                lista_H[i] = letras[j]
        j=0 # resetea el for 
    lista_H = lista_reversa(lista_H)
    return lista_H
#--------------------- OCTAL -------------------------------------------------------
def octal(num):
    band_o = True
    resultado = [] #lista vacia
    siguiente_num = 0
    entero = 0
    mult = 0
    resto = 0
    entero2 = 0

    while band_o == True:

        siguiente_num = num / 8
        entero = int(siguiente_num)
        mult = entero * 8
        resto = num - mult
        entero2 = int(resto)
        num = siguiente_num
        resultado.append(entero2)

        if entero == 0:
            band_o = False

    resultado = lista_reversa(resultado)
    return resultado

#--------------------- LISTA_REVERSA -----------------------------------------------
def lista_reversa(lista):
    a = len(lista)
    lista_R = []
    for i in range(len(lista)):
        a -= 1
        b = lista[a]
        lista_R.append(b)
    return lista_R

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

        lista_convertido = conversiones(expresion)
        print(f"Conversión: {lista_convertido} ")

    elif select == 4:
        calc_On = False
        print("\n\nApagando...")
    else:
        print("Error ingrese una opción válida")
    