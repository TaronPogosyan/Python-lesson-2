# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]


N = int(input('Введите число: '))

f = 1
mass = []
for i in range(1, N+1):
    f = i * f
    mass.append(f)
    
print(f"пусть N = {N}, тогда {mass}")