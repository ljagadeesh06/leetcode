def selectionSort(alist):
    for i in range(0, len(alist), 1):
        min = i
        for j in range(i + 1, len(alist), 1):
            if alist[j][0] <= 0 or alist[j][1] <= 0:
                min =j
            elif alist[j][1]/alist[j][0] < alist[min][1]/alist[min][0]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]

    return alist


def max_duffel_bag_value(cake_tuples, capacity):
    cake_tuples = selectionSort(list(cake_tuples))
    print(cake_tuples)
    collected_cap = 0
    max_val = 0
    idx = len(cake_tuples)-1;
    while collected_cap < capacity and idx >= 0:
        cake = cake_tuples[idx]
        idx -= 1
        if cake[0] == 0 or cake[1] == 0:
            continue
        while collected_cap + cake[0] <= capacity:
            collected_cap += cake[0]
            max_val += cake[1]
    return max_val


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

print(max_duffel_bag_value(cake_tuples, capacity))

