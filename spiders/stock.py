# -*- coding: utf-8 -*-
import scrapy
import csv
import codecs
import datetime
from tutorial.items import Funds
# import pandas as pd

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['http://stockpage.10jqka.com.cn']
    start_urls = ['http://stockpage.10jqka.com.cn/000001/funds/']
    # A_stocks = pd.read_excel('Astock/spiders/data_source/Astock10.xlsx',dtype={'code':str,'market':str})


    def parse(self, response):
        context = response.xpath('//*[@id="funds_lszjsj"]/text()')  
        
        title = context.extract()[0]
        print(title)

        stock_code = '000001'
        stock_market = '1201'
        stock_name = '平安银行'

        # print(content)

        # with open('/mnt/d/Crawler/'+ title[2:len(title)-2] + ".csv",'w',encoding='utf-8-sig') as f:
        #     # f.write(codecs.BOM_UTF8)
        #     csv.writer(f).writerow(['日期','收盘价','涨跌幅','资金净流入','5日主力净额','净额','净占比','净额','净占比','净额','净占比'])

        trs = response.xpath("//*[@id='history_table_free']/table[@class='m_table_3']//tr[position()>2]")
        data = []
        for tr in trs:
            date = tr.xpath(".//td[1]/text()").extract()[0]
            closePrice = tr.xpath('.//td[2]/text()').extract()[0]
            quoteChange = tr.xpath('.//td[3]/text()').extract()[0]
            inflow = tr.xpath('.//td[4]/text()').extract()[0]
            mainForce = tr.xpath('.//td[5]/text()').extract()[0]
            bigSingle = tr.xpath('.//td[6]/text()').extract()[0]
            bigSingle1 = tr.xpath('.//td[7]/text()').extract()[0]
            mediumSingle = tr.xpath('.//td[8]/text()').extract()[0]
            mediumSingle1 = tr.xpath('.//td[9]/text()').extract()[0]
            smallSingle = tr.xpath('.//td[10]/text()').extract()[0]
            smallSingle1 = tr.xpath('.//td[11]/text()').extract()[0]

            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(date,closePrice,quoteChange,inflow,mainForce,bigSingle,bigSingle1,mediumSingle,mediumSingle1,smallSingle,smallSingle1)

            dataMap = {
                'date':date,
                'closePrice' : closePrice,
                'quoteChange' : quoteChange,
                'inflow' : inflow,
                'mainForce' : mainForce,
                'bigmap':{
                    'bigSingle':bigSingle,
                    'bigSingle1':bigSingle1,
                },
                'mediumMap':{
                    'mediumSingle':mediumSingle,
                    'mediumSingle1':mediumSingle1,
                },
                'smallMap':{
                    'smallSingle':smallSingle,
                    'smallSingle1':smallSingle1,
                }
            }
            data.append(dataMap)

        
            # item = Funds(stock_code=stock_code,
            #     stock_market=stock_market,
            #     stock_name=stock_name,
            #     data = data
            #     )
            # yield item

            

            # for i in self.A_stocks.index:
            #     stock_code = self.A_stocks['code'][i]
            #     stock_market = self.A_stocks['market'][i]
            #     stock_name = self.A_stocks['name'][i]
            #     url = 'http://stockpage.10jqka.com.cn/%s/funds/' % stock_code
            #     yield scrapy.Request(url=url, callback=self.parse_next, dont_filter=True,
            #                         meta={"info": (stock_code, stock_market, stock_name)})

                # with open('/mnt/d/Crawler/'+ title[2:len(title)-2] + ".csv",'a',encoding='utf-8') as f:
                #     csv.writer(f).writerow([date,closePrice,quoteChange,inflow,mainForce,bigSingle,bigSingle1,mediumSingle,mediumSingle1,smallSingle,smallSingle1])
        for i in range(len(data)):
            print(data[i])

    # def parse_next(self,response):    
    #     stock_code, stock_market, stock_name = response.meta.get('info')

    #     trs = response.xpath("//table[@class='m_table_3']//tr[position()>2]")
    #     data = []

    #     for tr in trs:
    #         date = tr.xpath(".//td[1]/text()").extract()[0]
    #         closePrice = tr.xpath('td[2]/text()').extract()[0]
    #         quoteChange = tr.xpath('td[3]/text()').extract()[0]
    #         inflow = tr.xpath('td[4]/text()').extract()[0]
    #         mainForce = tr.xpath('td[5]/text()').extract()[0]
    #         bigSingle = tr.xpath('td[6]/text()').extract()[0]
    #         bigSingle1 = tr.xpath('td[7]/text()').extract()[0]
    #         mediumSingle = tr.xpath('td[8]/text()').extract()[0]
    #         mediumSingle1 = tr.xpath('td[9]/text()').extract()[0]
    #         smallSingle = tr.xpath('td[10]/text()').extract()[0]
    #         smallSingle1 = tr.xpath('td[11]/text()').extract()[0]

    #         crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #         dataMap = {
    #             'date':date,
    #             'closePrice' : closePrice,
    #             'quoteChange' : quoteChange,
    #             'inflow' : inflow,
    #             'mainForce' : mainForce,
    #             'bigmap':{
    #                 'bigSingle':bigSingle,
    #                 'bigSingle1':bigSingle1,
    #             },
    #             'mediumMap':{
    #                 'mediumSingle':mediumSingle,
    #                 'mediumSingle1':mediumSingle1,
    #             },
    #             'smallMap':{
    #                 'smallSingle':smallSingle,
    #                 'smallSingle1':smallSingle1,
    #             }
    #         }
    #         data.append(dataMap)

    #         item = Funds(stock_code=stock_code,
    #                 stock_market=stock_market,
    #                 stock_name=stock_name,
    #                 data = data)
    #         yield item

        pass


-25144.46
39385.23
-193.02
-9664.10
-8774.44
26807.72
46804.81
32814.00
-20948.81
38542.70
-2988.60
-12828.07
-8635.98
7640.85
-30520.41
51356.16
-9810.46
-68143.78
40903.43
-2993.77
10243.47
19490.68
10614.70
-52185.07
60436.45
18344.51
69984.94
18807.50
11599.34
-36053.88
-25806.86
38654.88
823.01
-9664.10
-18629.74
24531.85
50630.97
31705.35
-21248.56
38149.33
-2988.60