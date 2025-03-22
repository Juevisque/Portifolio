import sys
from Memoization import memoize
from functools import lru_cache #Least Recently Used Cache


# v1

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         xd = (fibonacci(n - 1) + fibonacci(n - 2)) 
#         return xd







# v2

# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)







# v3 fibonacci + memoization made by myself

# @memoize
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         xd = (fibonacci(n - 1) + fibonacci(n - 2)) 
#         return xd
    





# v4 fibonacci + memoization built-in function

# @lru_cache(maxsize=1000)
# def fibonacci(n):
#      if n < 2:
#          return n
#      return fibonacci(n - 1) + fibonacci(n - 2)





# v5 fibonacci + memoization hard code

cache = {}

def fibonacci(n):

    if n in cache:
        return cache[n]

    if n <= 1:
        return n
    
    f = fibonacci(n - 1) + fibonacci( n - 2)

    cache[n] = f

    return f 



if __name__ == '__main__':
#    sys.setrecursionlimit(1000) #Defines the limit of the recursion(How many times we can repeat the code)

    print(fibonacci(100))