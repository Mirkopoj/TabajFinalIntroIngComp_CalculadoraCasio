def simplify(frac: tuple[int,int]) -> tuple[int,int]:
    retnum = frac[0]
    retden = frac[1]
    for i in range(frac[1],2,-1):
        if retden%i==0 and retnum%i==0:
            retnum /= i
            retden /= i
    return (int(retnum), int(retden))
