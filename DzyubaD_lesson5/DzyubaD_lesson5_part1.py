def odd_numbers(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_5 = odd_numbers(5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))

# задача 2
# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
n = int(input("Введите n: "))
num = (i for i in range(1, n + 1, 2))

for element in num:
    print(element)
