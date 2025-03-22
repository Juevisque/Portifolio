lista = [6,0,5,2,8,3,1,4,9,8]


def quickSort(array):
    leng = len(array)
    if leng <=1:
        return array
    else:
        pivot = array.pop()

    ig = []
    il = []

    for i in array:
        if i > pivot:
            ig.append(i)
        else:
            il.append(i)
    return quickSort(il) + [pivot] + quickSort(ig)

print(quickSort([1,5,4,7,6,7,8,9,0,8,7,6,5,4,3,2]))