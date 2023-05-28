def tokenize(operaiones: str) -> list[str]:
    return operaiones.split(' ')

def parser(operaiones: str, frac=None) -> list:
    ret = []
    for op in operaiones:
        match op:
            case '=':
                ret.append('=')
                ret.append(' ')
            case '+' | '-' | '*' | '/':
                ret.append(op)
            case '|':
                if frac != None:
                    ret.append(frac)
                else:
                    raise (Exception("SintaxError"))
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
                print(calc(parsed_ops[:i], suma, resta, mult, div), calc(parsed_ops[(i+1):], suma, resta, mult, div))
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

