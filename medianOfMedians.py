def medianOfMedians(a, n):
    listasDivididas = [a[j:j+5] for j in range(0, len(a), 5)]
    listaMedianas = [sorted(listaDividida)[len(listaDividida)//2] for listaDividida in listasDivididas]
    if len(listaMedianas) <= 5:
        pp = sorted(listaMedianas)[len(listaMedianas)//2]
    else:
        pp = medianOfMedians(listaMedianas, len(listaMedianas)//2)
    menoresQuePP = [j for j in a if j < pp]
    mayoresQuePP = [j for j in a if j > pp]
    k = len(menoresQuePP)
    if n < k:
        return medianOfMedians(menoresQuePP,n)
    elif n > k:
        return medianOfMedians(mayoresQuePP,n-k-1)
    else:
        return pp