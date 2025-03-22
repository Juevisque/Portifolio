
#O(n)
def aumenta(x):
    for i in range(x):   
        print(i)
        i+=1

#O(n^2)
def square(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#O(n^3)
def cube(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

#O(log n) *2 examples
def recursive_log(n, y=0):
    if n <= 1:
        return y
    else:
        return recursive_log(n // 2, y + 1)



def iterative_log(n):
    y = 0
    while n > 1:
        n//=2
        y+=1

    return y

print(iterative_log(8))