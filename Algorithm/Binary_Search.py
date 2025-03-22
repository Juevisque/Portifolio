lista = [42,56,67,45,43,23,34,44,86,97]
# Test = ['Lucas', 'Bernardo','adamastor','Escoliose multipla'] N'ao Funciona
alvo = 86

def binarySearch(array, target):

    low = 0
    high = len(array) - 1
    

    while low <= high:
        middle = low + (high - low)//2
        value = array[middle]

        print(middle)

        if value < target:
            low = middle +1
        elif value > target:
            high = middle - 1
        else:
            return middle
        
binarySearch(lista, alvo)
