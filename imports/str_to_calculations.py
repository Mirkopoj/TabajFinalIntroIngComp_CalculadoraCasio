if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

def tokenize(operaciones: str) -> list[str]:
    ultimo_index = 0
    ret = []
    for i, car in enumerate(operaciones):
        match car:
            case '+' | '-' | '*' | '/' | '|' | '=':
                ret.append(operaciones[ultimo_index:i])
                ret.append(operaciones[i])
                ultimo_index = i+1
    ret.append(operaciones[ultimo_index:])
    return ret

def parser(operaciones: list[str], frac=None) -> list:
    ret = []
    prev_frac = False
    type_check = int
    if frac != None:
        type_check = tuple
    for i, op in enumerate(operaciones):
        if prev_frac:
            prev_frac = False
            continue
        match op:
            case '=':
                if type(ret[-1]) != type_check:
                    raise (Exception("SintaxError"))
                ret.append('=')
                ret.append(' ')
                return ret
            case '+' | '-' | '*' | '/':
                if type(ret[-1]) != type_check:
                    raise (Exception("SintaxError"))
                ret.append(op)
            case '|':
                if frac == None:
                    raise (Exception("SintaxError"))
                if i+1>=len(operaciones):
                    ret.append(op)
                    continue
                next = operaciones[i+1]
                if next == '':
                    ret.append(op)
                    continue
                ret.append(frac(ret.pop(), int(next)))
                prev_frac = True
            case '':
                continue
            case _ :
                ret.append(int(op))
    return ret

def operand_prety_printer(op, simply):
    if simply != None:
        op = simply(op)
        prt = str(op[0])
        prt += '|'
        prt += str(op[1])
        prt.replace(' ','')
        print(prt, end='')
    else:
        print(op, end='')

def parsed_ops_prety_printer(p_ops, simply):
    for o in p_ops:
        if type(o) == str:
            print(o, end='')
        else:
            operand_prety_printer(o, simply)

def calc(parsed_ops: list, suma, resta, mult, div, simply=None):
    if len(parsed_ops) == 1:
        return parsed_ops[0]
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '=':
                res = calc(parsed_ops[:i], suma, resta, mult, div)
                parsed_ops_prety_printer(parsed_ops, simply)
                operand_prety_printer(res, simply);
                print('\n')
                return ' '
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '+':
                return suma(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '-':
                return resta(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '/':
                return div(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '*':
                return mult(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
