'''
Coin weighing:  Given n coins where one has a different weight from the rest, the algorithm finds the index (position)
                of the light coin in the least amount of weighings possible.
Name of author: Haakon Svane
Date:           19.10.2019
'''

import random as r
import math as m

# Determines the lightest of two stacks
def lowest_weight(arr1, arr2):
    w_1 = sum(arr1)
    w_2 = sum(arr2)
    return 0 if w_1 < w_2 else (1 if w_1 > w_2 else 2)

def solve_puzzle(num_coins=9):
    seed = r.randint(0, num_coins - 1)
    # List of normal coins (1) with a light coin (0) placed randomly
    arr = [1 if i != seed else 0 for i in range(num_coins)]

    # Recursive function used to divide the coins into subdivisions for further weighing.
    def func(array):
        ind = 0
        count = 0
        div = m.ceil(len(array) / 3)

        j = lowest_weight(array[:div], array[div:2 * div])
        count += 1

        if div == 1:
            ind += j
        else:
            k, c = func(array[j * div:(j + 1) * div])
            count += c
            ind += k + div * j
        return ind, count

    return arr, func(arr)


arr, (index, count) = solve_puzzle(num_coins=11)
print("Original random array: %s \nThe lightest coin is located at index i=%s and was found after c=%s weighings."
      % (arr, index, count))


# Code for plotting results
# from matplotlib import pyplot as plt
# solution = []
# for i in range(2, 101):
#     _, (_, count) = solve_puzzle(i)
#     solution.append(count)
#
# plt.scatter([i for i in range(2, 101)], solution, label="Simulation")
# plt.plot([i for i in range(2, 101)],
#          [m.ceil(m.log(i, 3)) for i in range(2, 101)],
#          'r', label="$\left \lceil{log_3(x)}\\right \\rceil $")
# plt.ylabel('Number of weighings')
# plt.xlabel('Number of coins')
# plt.legend()
# plt.show()


