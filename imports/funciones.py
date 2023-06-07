if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

def suma_clasica(a: int,b: int) -> int:
    return a+b

def resta_clasica(a: int,b: int) -> int:
    return a-b

def multiplicacion_clasica(a: int,b: int) -> int:
    return a*b

def division_clasica(a: int,b: int) -> float:
    return a/b

def hacer_fraccion(num: int,den: int) -> tuple[int,int]:
    return(num,den)

def suma_fraccionaria(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    ret_num = a[0]*b[1] + a[1]*b[0]
    ret_den = a[1]*b[1]
    return (ret_den, ret_num)

def resta_fraccionaria(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    ret_num = a[0]*b[1] - a[1]*b[0]
    ret_den = a[1]*b[1]
    return (ret_den, ret_num)

def multiplicacion_fraccionaria(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    ret_num = a[0]*b[0]
    ret_den = a[1]*b[1]
    return (ret_den, ret_num)

def division_fraccionaria(a: tuple[int,int],b: tuple[int,int]) -> tuple[int,int]:
    ret_num = a[0]*b[1]
    ret_den = a[1]*b[0]
    return (ret_den, ret_num)
