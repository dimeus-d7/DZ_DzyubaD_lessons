percent = ['Процент', 'Процента', 'Проценов']
for i in range(1, 101):
    if i % 10 == 1 and i % 100 and i != 11:
        print(i, percent[0])
    elif 2 <= i % 10 <= 4 and (i % 100 < 10 or i % 100 >= 20):
        print(i, percent[1])
    else:
        print(i, percent[2])
