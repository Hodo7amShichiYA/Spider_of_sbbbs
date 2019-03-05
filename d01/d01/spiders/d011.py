import scrapy


class d01(scrapy.Spider):
    name = "sbbbs"  # 定义蜘蛛名
    start_urls = ['http://www.mcbbs.net/forum-serverpack-1.html']

    def parse(self, response):
        #此处可改成其他需要的元素
        titles = response.xpath('//a[@class="s xst"]/text()').extract()[6:]
        links = response.xpath('//a[@class="s xst"]/@href').extract()[6:]

        for title, link in zip(titles, links):
            print(title, 'http://www.mcbbs.net/'+link)

        for i in range(20):
            #修改此处可以爬取任意版块
            all_pages = 'http://www.mcbbs.net/forum-serverpack-%s.html' % i
            yield scrapy.Request(
                url=all_pages,
                callback=self.parse
            )
