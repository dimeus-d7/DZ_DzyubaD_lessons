# ДЗ студента Дзюбы Дмитрия
# создаем переменную duration где предлогаем пользователю ввести число
# далее, создаем условие вычисления целое числительное деление в зависимости от минуты, часа и дня
# проблемы были в вычислении и подбору чисел и понимания деления или нахождения целого числа
duration = int(input("введите промежуток времени "))
if duration <= 60:
    print(duration, "сек")
elif duration <= 3600:
    print(duration // 60, "мин", duration % 60, "сек")
elif duration <= 86400:
    print(duration // 3600, "час", duration % 3600 // 60, "мин", duration % 60, "сек")
elif duration <= 2678400:
    print(duration // 86400, "дн", duration % 86400 // 3600, "час", duration % 3600 // 60, "мин", duration % 60, "сек")