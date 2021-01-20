year = int(input('Введите кол-во лет\n'))
amortization = int(input('введите процент амортизации за год: '))
a = 1
overall = []
while year >= a:
    equipment = int(input(f'Введите стоимость оборудования за {a} год: '))
    percent = equipment - (equipment / 100 * amortization * a)
    overall.append(percent)
    a += 1
print('итоговая стоимость оборудования:', sum(overall))
