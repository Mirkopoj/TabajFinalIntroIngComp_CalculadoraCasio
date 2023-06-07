if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

import str_to_calculations as stc

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def fracion(a,b):
    return a**b

comp = ""
aux = 'a'
while aux != ' ':
    comp += input(comp)
    #comp = "3|"
    aux = stc.tokenize(comp)
    try:
        aux = stc.parser(aux, frac=fracion)
    except:
        print("SintaxError")
        comp = ""
        continue
    if len(aux)%2 == 1:
        aux = stc.calc(aux, add, sub, mul, div)
