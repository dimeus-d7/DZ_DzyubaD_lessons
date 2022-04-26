list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for element in list_1:
    if element.isdigit():
        num = int(element)
        list_2.extend(['"', f'{num:02d}', '"'])
    else:
        list_2.append(element)

print(list_2)
print(' '.join(list_2))
