def simpify(frac: tuple[int,int]) -> tuple[int,int]:
    retnum = frac[0]
    retden = frac[1]
    for i in range(2, frac[1]):
        if retnum%i==0 and retden%i==0:
            retnum /= i
            retden /= i
    return (int(retnum), int(retden))
