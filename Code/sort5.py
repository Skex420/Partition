def sort5(A):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
