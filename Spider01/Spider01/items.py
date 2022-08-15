# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider01Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    comment = scrapy.Field()
    link = scrapy.Field()
    scores = scrapy.Field()


if __name__ == "__main__":
    test = Spider01Item()
    test['name'] = 'Mark'
    test['saying'] = 'Practice Makes Perfect!'
    # print(test)
