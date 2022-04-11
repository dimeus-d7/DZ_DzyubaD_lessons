# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]
d = {}
for j in src:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1
result = [el for el in src if d[el] ==1]
print(result)