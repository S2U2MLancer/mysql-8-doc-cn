from abc import ABC, abstractmethod

from scrapy import Selector


class BaseParser(ABC):

    def __init__(self, xpath: str):
        self.xpath = xpath

    def execute(self, selector: Selector) -> str:
        target = selector.xpath(self.xpath)
        if not target:
            return None
        return self.parse(target)

    @abstractmethod
    def parse(self, target: Selector) -> str:
        pass
