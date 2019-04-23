from tj import parserT2J

text = '''
Доброго дня, { name }!
Сегодня { day } день как вы не заходили к нам на сайт.
{ site }
'''
json_P = {
    "name": "Никита Львович",
    "day": "3",
    "site": "http://www.domen.ru"
}

print(parserT2J(text, json_P))

# Доброго дня, Никита Львович!
# Сегодня 3 день как вы не заходили к нам на сайт.
# http://www.domen.ru

