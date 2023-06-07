if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

numerador = 2145
divisor = 635
bandera = True
multiplos2 = ["2","0","4","6","8"]
multiplos9 = [9,18,27,36,45,54,63,72,81,90]
multiplos3 = [3,6,9,12,15,18,21,24,27,30]
multiplos5 = ["0","5"]
numerador_lista = list(str(numerador))
divisor_lista = list(str(divisor))

while bandera:

    suma9 = int(numerador_lista[0])
    if len(numerador_lista)>1:
        for i in range(len(numerador_lista)-1):
            suma9 = suma9 + int(numerador_lista[i + 1])

    suma9_2 = int(divisor_lista[0])
    if len(divisor_lista)>1:
        for j in range(len(divisor_lista)-1):
            suma9_2 = suma9_2 + int(divisor_lista[j + 1])

    if numerador >= 9 and divisor >= 9 and suma9 in multiplos9 and suma9_2 in multiplos9: 
        div1 = int(numerador / 9)
        div2 = int(divisor / 9)
        numerador = div1
        divisor = div2
        
    elif numerador >= 6 and divisor >= 6 and  numerador_lista[len(numerador_lista)-1] in multiplos2 and divisor_lista[len(divisor_lista)-1] in multiplos2 and suma9 in multiplos3 and suma9_2 in multiplos3:
        div1 = int(numerador / 6)
        div2 = int(divisor / 6)
        numerador = div1
        divisor = div2

    elif numerador >= 5 and divisor >= 5 and numerador_lista[len(numerador_lista)-1] in multiplos5 and divisor_lista[len(divisor_lista)-1] in multiplos5:
        div1 = int(numerador / 5)
        div2 = int(divisor / 5)
        numerador = div1
        divisor = div2
    
    numerador_lista.clear
    divisor_lista.clear
    numerador_lista = list(str(numerador))
    divisor_lista = list(str(divisor))

    suma9 = int(numerador_lista[0])    
    if len(numerador_lista)>1:
        for k in range(len(numerador_lista)-1):
            suma9 = suma9 + int(numerador_lista[k + 1])

    suma9_2 = int(divisor_lista[0])
    if len(divisor_lista)>1:
        for j in range(len(divisor_lista)-1):
            suma9_2 = suma9_2 + int(divisor_lista[j + 1])

    if numerador >= 3 and divisor >= 3 and suma9 in multiplos3 and suma9_2 in multiplos3: 
        div1 = int(numerador / 3)
        div2 = int(divisor / 3)
        numerador = div1
        divisor = div2
        
    elif numerador >= 2 and divisor >= 2 and numerador_lista[len(numerador_lista)-1] in multiplos2 and divisor_lista[len(divisor_lista)-1] in multiplos2:
        div1 = int(numerador / 2)
        div2 = int(divisor / 2)
        numerador = div1
        divisor = div2

    else:
        bandera = False

print(numerador)
print(divisor)

