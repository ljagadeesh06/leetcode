def selectionSort(alist):
    for i in range(0, len(alist), 1):
        min = i
        for j in range(i + 1, len(alist), 1):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]

    return alist


alist = (4, 7, 2)
retItems = selectionSort(list(alist))
print(retItems)





