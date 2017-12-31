def insertionSort(alist):
    for i in range(1, len(alist), 1):
        v = alist[i]
        j = i
        while alist[j - 1] > v and j >= 1:
            alist[j] = alist[j - 1]
            j -= 1
        alist[j] = v

    return alist


alist = (4, 7, 2)
retItems = insertionSort(list(alist))
print(retItems)

