def quickSort(a):
   quickSorting(a,0,len(a)-1)

def quickSorting(a,inicio,final):
   if inicio<final:

       pp = particion(a,inicio,final) #pp(punto de particion)

       quickSorting (a, inicio,pp-1)
       quickSorting (a, pp+1, final)

def particion(a , inicio, final):
   pivote = a[inicio]

   j = inicio+1
   k = final

   endwhile = False
   while not endwhile:

       while j <= k and a[j] <= pivote:
           j = j + 1

       while a[k] >= pivote and k >= j:
           k = k -1

       if k < j:
           endwhile = True #si K llega a sobre pasar J, siendo J el inicio.
       else:
           temp = a[j]
           a[j] = a[k]
           a[k] = temp

   temp = a[inicio] #Variable temporal
   a[inicio] = a[k] #al inicio se le asigna la posición K
   a[k] = temp #Al final se le asigna la temporal, siendo el inicio.
   return k
