def thesaurus(*names):
    name_dict = dict()
    for i in sorted(names):
        key = i[0]
        if name_dict.get(key) is None:
            name_dict[key] = [i]
        else:
            name_dict[key].append(i)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Дима"))
