import requests
import json

print("Введите слово!")
text = input("Enter: ")
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
lang = 'en-ru', 'ru-en'
r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
# Выводим результат
print(json.loads(r.text)['text'][0])