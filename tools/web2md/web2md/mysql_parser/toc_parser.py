from scrapy import Selector

from mysql_parser.base_parser import BaseParser


class MySqlTocParser(BaseParser):

    def __init__(self):
        super().__init__("//*[@class='title']")

    def parse(self, target: Selector) -> str:
        pass
