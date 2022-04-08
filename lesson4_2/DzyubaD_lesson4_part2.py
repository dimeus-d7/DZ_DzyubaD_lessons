import requests


def currency_rates (val):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = site.content.decode(encoding=site.encoding)
    result = None
    if val not in content:
        return result
    else:
        for element in content.split(f'{val}')[1:]:
            for element_2 in element.split('</Value>')[:1]:
                result = round(float(element_2.split('<Value>')[1].replace(',', '.')), 2)
                return f'Курс валютты: {result} руб.'


if __name__ == '__main__':

    code_val = input('Введите код валюты: ')
    print(currency_money(code_val))
