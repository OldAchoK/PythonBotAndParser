from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import json


file = open('aneks.json', 'r', encoding="utf-8")
resp = json.loads(file.read())
print(resp['1']['text'])

# url = "https://stalker.fandom.com/ru/wiki/%D0%90%D0%BD%D0%B5%D0%BA%D0%B4%D0%BE%D1%82%D1%8B"
# ua = UserAgent
#
# def collect_aniki():
#     req = requests.get(url, headers = {"user-agent":f'{ua.random}'})
#     with open('full.html', 'w', encoding="utf-8") as file:
#         file.write(req.text)
#     file = open('full.html', 'r', encoding="utf-8")  # or full way
#     site = file.read()
#     file.close()
#     anek = BeautifulSoup(site, "lxml")
#     back = anek.find_all(class_="poem")
#     src = {}
#     src[0] = {
#         'id': 0,
#         'text': "aboba"
#     }
#     for id, item in enumerate(back):
#         src[id]={
#             'id': id,
#             'text': item.text
#         }
#     with open('aneks.json', 'w') as aneks:
#         json.dump(src, aneks, indent=3)
#
# def main():
#
#     collect_aniki()
#
# if __name__ == '__main__':
#     main()