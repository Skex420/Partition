import random as ran

def quickSort(a,inicio,fin):
    if inicio<fin:
        randomN=ran.randint(inicio,fin)
        temp=a[fin]
        a[fin]=a[randomN]
        a[randomN]=temp
        pp=particionRandom(a,inicio,fin)
        quickSort(a,inicio,pp-1)
        quickSort(a,pp+1,fin)
def particionRandom(a, inicio, fin):
    randomN=ran.randint(inicio,fin)
    temp=a[fin]
    a[fin]=a[randomN]
    a[randomN]=temp
    i=inicio-1
    for j in range(inicio,fin):
        if a[j]<a[fin]:
            i=i+1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    temp=a[i+1]
    a[i+1]=a[fin]
    a[fin]=temp
    return i+1
