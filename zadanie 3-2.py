import random

n = int(input('введите числа: '))
A = []
B = []
for x in range(n):
    a = random.randint(0, 99)
    A.append(a)
    if not a % 2:
        B.append(a)
print('Список А', A, 'Список В(четные):', B)
