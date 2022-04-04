def num_translate(words):
    Eng_Rus_Numbers = {"One": "один",
                       "two": "два",
                       "tree": 'три',
                       "four": 'четыре',
                       "five": 'пять',
                       "six": 'шесть',
                       "seven": 'семь',
                       "eight": 'восемь',
                       "nine": 'девять',
                       "ten": 'десять'}
    return Eng_Rus_Numbers.get(words).title()


print(num_translate("five"))
