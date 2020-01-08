from scrapy.http import HtmlResponse

from items import MySqlDocument
from mysql_parser.title_parser import MySqlTitleParser


def parse(response: HtmlResponse):
    doc = MySqlDocument()
    doc["src"] = response.url

    selector = response.selector
    doc["title"] = MySqlTitleParser().execute(selector)
    return doc
