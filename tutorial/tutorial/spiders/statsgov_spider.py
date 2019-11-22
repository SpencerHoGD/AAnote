
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'province'

    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html',
    ]
    # start_urls = ['./stats/stats_province.html']

    # def parse(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()

    #     yield {
    #         'province': extract_with_css('.provincetr a::text'),
    #     }


    # def parse(self, response):
    #     year = response.url.split("/")[-3]
    #     filename = 'stats-%s.html' % year
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)


    # def parse(self, response):
    #     for province in response.css('tr.provincetr'):
    #         yield {
    #             'province': province.css('td a::text').getall(),
    #         }

    def parse(self, response):
        for province in response.css('tr.provincetr td'):
            yield {
                'province': province.css('a::text').get(),
                'link': province.css('a::attr(href)').get(),
            }

        # follow links to city page
        for a in response.css('tr.provincetr td a'):
            yield response.follow(a, callback=self.parse_city)



class AuthorSpider(scrapy.Spider):
    name = 'city2'

    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html',
    ]

    def parse(self, response):
        # follow links to city page
        for a in response.css('tr.provincetr td a'):
            yield response.follow(a, callback=self.parse_city)


    def parse_city(self, response):
        for city in response.css('tr.citytr'):
            yield {
                'code': city.css('td a::text')[0].get(),
                'city': city.css('td a::text')[1].get(),
                'link': city.css('td a::attr(href)')[0].get(),
            }


class AuthorSpider(scrapy.Spider):
    name = 'city1'

    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/13.html',
    ]


    def parse(self, response):
        for city in response.css('tr.citytr'):
            yield {
                'code': city.css('td a::text')[0].get(),
                'city': city.css('td a::text')[1].get(),
                'link': city.css('td a::attr(href)')[0].get(),
            }
