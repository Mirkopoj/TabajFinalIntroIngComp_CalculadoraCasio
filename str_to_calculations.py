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
    for i, op in enumerate(operaciones):
        if prev_frac:
            prev_frac = False
            continue
        match op:
            case '=':
                ret.append('=')
                ret.append(' ')
            case '+' | '-' | '*' | '/':
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
                try:
                    ret.append(int(op))
                except:
                    raise (Exception("SintaxError"))
    return ret

def calc(parsed_ops: list, suma, resta, mult, div):
    for i, op in enumerate(reversed(parsed_ops)):
        i = len(parsed_ops)-i-1
        match op:
            case '=':
                print(calc(parsed_ops[:i], suma, resta, mult, div))
                return ' '
            case '/':
                return div(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
            case '*':
                return mult(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
            case '+':
                return suma(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
            case '-':
                return resta(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
            case _ :
                if len(parsed_ops) == 1:
                    return op

