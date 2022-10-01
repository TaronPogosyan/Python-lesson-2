# 5 Реализуйте алгоритм перемешивания списка.

import random

x = 7
lft = -5
rght = 8

def mass_alg(x, lft, rght):
    return [random.randint(lft, rght) for i in range(x)]
def shuffle_alg(lst):
    return random.shuffle(lst)

mass = mass_alg(x, lft, rght)
print(mass)
shuffle_alg(mass)
print(mass)