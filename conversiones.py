#--------------------- CONVERSIONES --------------------------------------------------
def conversiones(expresion: int) -> str:
    num = expresion
    opcion = 0
    resultado = []
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
            print("Ingrese un número válido")
    return lista_a_str(resultado)

#--------------------- BINARIO ---------------------------------------------------------
def binario(num) -> list: 
    actual = num
    aux = 2
    lista=[]

    while aux >= 1:
        aux = actual / 2
        lista.append(int(actual % 2))
        actual = aux
    lista = lista_reversa(lista) 
    return lista
#--------------------- HEXADECIMAL --------------------------------------------------
def hexadecimal(num) -> list:
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
def octal(num) -> list:
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
def lista_reversa(lista:list) -> list:
    a = len(lista)
    lista_R = []
    for _ in range(len(lista)):
        a -= 1
        b = lista[a]
        lista_R.append(b)
    return lista_R

#--------------------- PRETY_PRINT -----------------------------------------------
def lista_a_str(lista: list) -> str:
    ret = ""
    for n in lista:
        match n:
            case 0:
                ret += '0'
            case 1:
                ret += '1'
            case 2:
                ret += '2'
            case 3:
                ret += '3'
            case 4:
                ret += '4'
            case 5:
                ret += '5'
            case 6:
                ret += '6'
            case 7:
                ret += '7'
            case 8:
                ret += '8'
            case 9:
                ret += '9'
            case _:
                ret += n
    return ret
