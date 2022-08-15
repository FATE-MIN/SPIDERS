import scrapy
from Spider01.items import Spider01Item
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 起始url地址
    start_urls = ['http://movie.douban.com/top250']


    def parse(self, response):
        movies_list = response.xpath('//body/div[@id="wrapper"]//li')
        # print(movies_list)
        for movie in movies_list:
            # 将SpiderItem对象转化为dict类型(仅限于scrapy库中使用)
            item = dict(Spider01Item())
            item['name'] = movie.xpath('.//a//span[1]/text()').extract_first()
            item['comment'] = movie.xpath('.//div[2]//p[2]/span/text()').extract_first()
            item['link'] = movie.xpath('.//div/a/@href').extract_first()
            # yield item
            # print(item)

            # meta参数:提取不在本页面链接的内容时使用，字典格式传入，需要定义新的parse方法为callback
            yield scrapy.Request(
                url=item['link'],
                meta={'item':item},
                callback=self.parse_detail
            )

        # 翻页操作
        # temp = int(response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()[7:9])
        # 正则表达式提取链接中变化的部分，返回一个列表
        temp = re.findall(r'\d{2,3}', response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first())
        print(temp[0])

        # print(next_url)
        if response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[@class="next"]/text()').extract_first() != '后页>':
            next_url = 'https://movie.douban.com/top250?start=' + temp[0] + '&filter=' + \
                       response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )
        #     print(next_url)
    def parse_detail(self, response):
        item = response.meta['item']
        item['scores'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        # 返回给引擎
        yield item