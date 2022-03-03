import csv
import pkgutil

from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from nlu_link_collector.items import NluLinkCollectorItem


class NluLinkCollector(CrawlSpider):
    name = "nlu_link_collector"

    def start_requests(self):
        urls = []

        csv_file = pkgutil.get_data("nlu_link_collector",
                                    "resources/nlu_links.csv")
        data = csv.reader(csv_file)
        next(data, None)
        for row in data:
            urls.append(row[0])

        self.logger.warn(urls[0])

        for url in urls:
            yield Request(url, self.parse_items)

    def parse_items(self, response):
        hxs = Selector(response)

        xpath = "//b[text()=' НАДХОДЖЕННЯ:']/following::table[3]/tr"

        for row in hxs.xpath(xpath):
            year = row.xpath(".//b[1]/text()").extract()

            for link in row.xpath('.//a'):
                item = NluLinkCollectorItem()

                item['year'] = year
                item['volume'] = link.xpath("./text()").extract()
                item['uri'] = link.xpath("./@href").extract()
                item['source_uri'] = response.url

                if item['uri']:
                    yield item
