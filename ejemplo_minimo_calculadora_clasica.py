import str_to_calculations as stc

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

comp = ""
while True:
    comp += input(comp)
    aux = stc.tokenize(comp)
    try:
        aux = stc.parser(aux)
    except:
        print("SintaxError")
        comp = ""
        continue
    aux = stc.calc(aux, add, sub, mul, div)
    if aux == ' ':
        comp = ""
