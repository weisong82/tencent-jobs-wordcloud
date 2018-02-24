# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from tencentjob.items import TencentjobItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/']

    def parse(self, response):

        # get <a> 列表页
        lists = response.xpath("//table//a")
        for link in lists:
            url = link.xpath("@href").extract()[0]
            if 'position_detail' in url: # 根据url去解析内容页面
                detail_page= urljoin("https://hr.tencent.com/", url)
                yield scrapy.Request(detail_page, callback=self.parse_content)

        # 如果有下一页继续抓取数据
        next_pages = response.xpath('//a[@id="next"]/@href')

        if next_pages:
            next_page = urljoin("https://hr.tencent.com/", next_pages.extract()[0])
            self.log("next_page: % s" % next_page)
            # 自己调用自己  类似php 函数的当中的递归
            yield scrapy.Request(next_page, callback=self.parse)

    # 内容页抓取
    def parse_content(self, response):
        item = TencentjobItem()

        item['title'] = response.xpath("//td[@id='sharetitle']/text()").extract()
        item['location'] = response.xpath("//tr[@class='c bottomline']/td[1]/text()").extract()
        item['classify'] = response.xpath("//tr[@class='c bottomline']/td[2]/text()").extract()
        item['count'] = response.xpath("//tr[@class='c bottomline']/td[3]/text()").extract()
        item['duty'] = response.xpath("//table//tr[@class='c'][1]/td/ul")[0].xpath('string(.)').extract()[0].replace("\n", "")
        item['requirement'] = response.xpath("//table//tr[@class='c'][2]/td/ul")[0].xpath('string(.)').extract()[0].replace("\n", "")
        item['link'] = response.url
        yield item