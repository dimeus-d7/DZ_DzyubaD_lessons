prices = [44, 5, 2, 2.5, 10, 33.33, 12, 14.4, 97, 88, 15.9, 77.6]  # делаем список произвольных цен
prices_2 = []
for numbers in prices:  # делаем уравнение по преобразованию в рубли и копейки
    result = round(numbers * 100)
    roubls = round(result // 100)
    cents = round(result % 100)
    prices_2.append(f"{roubls:02d} руб. {cents:02d} коп.")
print(",".join(prices_2))
prices_sort2 = sorted(prices_2)
print(",".join(prices_sort2))  # по возрастанию
prices_sort3 = sorted(prices_sort2, reverse=True)
print(",".join(prices_sort3))  # по убыванию
print(",".join(sorted(prices_sort3[:5])))  # первые пять дорогих
