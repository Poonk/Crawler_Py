# -*- coding: utf-8 -*-
import scrapy
import datetime
from tutorial.items import Holder


class HolderSpider(scrapy.Spider):
    name = 'holder'
    allowed_domains = ['http://stockpage.10jqka.com.cn']
    start_urls = ['http://stockpage.10jqka.com.cn/HK8238/holder/']
    A_stocks = pd.read_excel('Astock/spiders/data_source/Astock10.xlsx',dtype={'code':str,'market':str})

    def parse(self, response):
        stock_code = '000001'
        stock_market = '1201'
        stock_name = '平安银行'


        data = []

        trs = response.xpath("//*[@id='change']/div[2]/table/tbody/tr")



        for tr in trs :
            date = tr.xpath("./th/text()").extract()[0]
            shareholder = tr.xpath("./td[1]/text()").extract()[0]
            # change = tr.xpath("./td[2]/span/text()").extract()[0]

            try:
                change = tr.xpath("./td[2]/span/text()").extract()[0]
            except :
                change = tr.xpath("./td[2]/text()").extract()[0]
                change = change.strip()

            holding = tr.xpath("./td[3]/text()").extract()[0]
            proportion = tr.xpath("./td[4]/text()").extract()[0]
            quality = tr.xpath("./td[5]/text()").extract()[0]

            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(date,shareholder,change,holding,proportion,quality)

            dataMap = {
                'date':date,
                'shareholder':shareholder,
                'change':change,
                'holding':holding,
                'proportion':proportion,
                'quality':quality,
            }
            data.append(dataMap)

            item = Holder(
                stock_code=stock_code,
                stock_market=stock_market,
                stock_name=stock_name,
                data = data,
                crawl_time = crawl_time,
                )
            yield item

            for i in self.A_stocks.index:
                stock_code = self.A_stocks['code'][i]
                stock_market = self.A_stocks['market'][i]
                stock_name = self.A_stocks['name'][i]
                # url = 'http://stockpage.10jqka.com.cn/%s/funds/' % stock_code
                yield scrapy.Request(url=url, callback=self.parse_next, dont_filter=True,
                                    meta={"info": (stock_code, stock_market, stock_name)})

            # print("\n")
        # for i in range(len(data)):
        #     print(data[i])
    def parse_next(self,response):    
        stock_code, stock_market, stock_name = response.meta.get('info')

        data = []

        trs = response.xpath("//*[@id='change']/div[2]/table/tbody/tr")



        for tr in trs :
            date = tr.xpath("./th/text()").extract()[0]
            shareholder = tr.xpath("./td[1]/text()").extract()[0]
            # change = tr.xpath("./td[2]/span/text()").extract()[0]

            try:
                change = tr.xpath("./td[2]/span/text()").extract()[0]
            except :
                change = tr.xpath("./td[2]/text()").extract()[0]
                change = change.strip()

            holding = tr.xpath("./td[3]/text()").extract()[0]
            proportion = tr.xpath("./td[4]/text()").extract()[0]
            quality = tr.xpath("./td[5]/text()").extract()[0]

            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(date,shareholder,change,holding,proportion,quality)

            dataMap = {
                'date':date,
                'shareholder':shareholder,
                'change':change,
                'holding':holding,
                'proportion':proportion,
                'quality':quality,
            }
            data.append(dataMap)

            item = Holder(
                stock_code=stock_code,
                stock_market=stock_market,
                stock_name=stock_name,
                data = data,
                crawl_time = crawl_time,
                )
            yield item
        pass
