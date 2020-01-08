import scrapy
from scrapy.http import HtmlResponse

import mysql_parser


class MySQL57DocSpider(scrapy.Spider):
    name = 'mysql57'
    doc_root_url = 'https://dev.mysql.com/doc/refman/5.7/en/'

    def start_requests(self):
        yield scrapy.Request(url=self.doc_root_url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        doc = mysql_parser.parse(response)
        yield doc
        # doc = MySqlDocument()
        # doc["src"] = response.url
        # doc["title"] = response.xpath("//*[@class='title']").extract_first()
        # doc["breadcrumbs"] = response.xpath("//div[@id='docs-breadcrumbs']").extract_first()
        # doc["content"] = response.xpath("//div[@id='docs-body']").extract_first()
        # yield doc
        #
        # toc_elements = response.xpath("//div[@class='toc']//span[@class='section']/a")
        # for toc_element in toc_elements:
        #     # title = toc_element.xpath('text()').extract_first()
        #     link = toc_element.xpath('@href').extract_first()
        #     target_url = response.urljoin(link)
        #     yield Request(
        #         target_url,
        #         callback=self.parse
        #     )
