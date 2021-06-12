from lxml import html
import requests
import time

main_link = "https://lenta.ru/"
response = requests.get(main_link)
root = html.fromstring(response.text)
news = root.xpath("//div[@class='