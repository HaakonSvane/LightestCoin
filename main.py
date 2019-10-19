'''
Coin weighing:  Given n coins where one has a different weight from the rest, the algorithm finds the index (position)
                of the light coin in the least amount of weighings possible.
Name of author: Haakon Svane
Date:           19.10.2019
'''


import random as r
import math as m

n = 9                                               # Total amount of coins to be given
count = 0                                           # Counter for the recursive loop (number of weighings)

seed = r.randint(0, n-1)
arr = [1 if i != seed else 0 for i in range(n)]     # List of normal coins (1) with a light coin (0) placed randomly

# Determines the lightest of two stacks
def lowest_weight(arr1, arr2):
    global count
    count += 1
    w_1 = sum(arr1)
    w_2 = sum(arr2)

    return 0 if w_1 < w_2 else (1 if w_1 > w_2 else 2)

# Recursive function used to divide the coins into subdivisions for further weighing.
def func(array):
    k = 0
    div = m.ceil(len(array)/3)
    if div == 1:
        return lowest_weight(array[:1], array[1:2])
    else:
        j = lowest_weight(array[:div], array[div:2*div])
        k += func(array[j*div:(j+1)*div])+div*j
    return k


index = func(arr)
print("Original random array: %s \nThe lightest coin is located at index i=%s and was found after c=%s counts."
      %(arr, index, count))