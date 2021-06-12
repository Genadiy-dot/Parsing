'''
Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости.
 Для парсинга использовать XPath. Структура данных должна содержать:
название источника;
наименование новости;
ссылку на новость;
дата публикации.
'''

from pprint import pprint
from lxml import html
import requests
import time

headers = {

    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177 (Edition 360-1)",
    'Accept-Language': "Accept-Language: ru-RU, ru;q=0.9, en-US;q=0.8, en;q=0.7, fr;q=0.6"

}

site_head = "https://mail.ru/"
url = "https://news.mail.ru/"

response = requests.get(url, headers=headers)

root = html.fromstring(response.text)
news = root.xpath("//div[@class='newsitem.newsitem_height_fixed.newsitem_height_fixed_primary.js-ago-wrapper']")

print(news[0])
print(type(news[0]))
# for news_item in news:
#     source_name = news_item.xpath(".//span class='hdr__text'")
#     href = news_item.xpath(".//div class='article__intro.meta-speakable-intro p'")
#     name = news_item.xpath(".//h1 class='hdr__inner'")
#     publication_date = news_item.xpath(".//span class='note__text.breadcrumbs__text.js-ago datetime'")
    #print(source_name, href, name, publication_date)


