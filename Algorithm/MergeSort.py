
megaxd = [8,2,5,3,4,7,6,1]

def mergeSort(array):

    def merge(Larray, Rarray, array):
        leftsize = len(array) //2
        rightsize = len(array) - leftsize

        x = 0
        l = 0
        r = 0

        while l < leftsize and r < rightsize:
            if leftarray[l] < rightarray[r]:
                array[x] = leftarray[l]
                x+=1
                l+=1
            else:
                array[i] = rightarray[r]
                i+=1
                r+=1
        while l < leftsize:
            array[x] = leftarray[l]
            x +=1
            l+=1
        while r < rightsize:
            array[x] = rightarray[r]
            x +=1
            r+=1



    lenght = len(array)
    if len(array) <= 1:
        return
    
    middle = lenght // 2
    leftarray = middle
    rightarray = lenght - middle

    i = 0
    j = 0

    for i in array:
        i +=1
        if i < middle:
            leftarray[i] = array[i]
        else:
            leftarray[j] = array[i]
            j+=1

    mergeSort(leftarray)
    mergeSort(rightarray)
    merge(leftarray, rightarray, array)

mergeSort(megaxd)