if __name__ == "__main__":
    print("Este archivo es para incluir, no para ejecutar")
    exit(-1)

def simplify(frac: tuple[int,int]) -> tuple[int,int]:
    retnum = frac[0]
    retden = frac[1]
    for i in range(frac[1],1,-1):
        if retden%i==0 and retnum%i==0:
            retnum /= i
            retden /= i
            i = i+1
    return (int(retnum), int(retden))
