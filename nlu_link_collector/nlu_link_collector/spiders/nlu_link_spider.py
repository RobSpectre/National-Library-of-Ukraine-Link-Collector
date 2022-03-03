#!/usr/local/bin/python
# coding: utf-8

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
        data = csv.reader(csv_file.decode('utf-8').splitlines(), delimiter=',')
        next(data, None)
        for row in data:
            urls.append(row[0])

        for url in urls:
            yield Request(url, self.parse_items)

    def parse_items(self, response):
        hxs = Selector(response)

        xpath = "//b[text()=' НАДХОДЖЕННЯ:']/following::table[3]/tr"

        for row in hxs.xpath(xpath):
            year = row.xpath(".//b[1]/text()").extract()

            for link in row.xpath('.//a'):
                href = link.xpath("./@href").extract()

                if len(href) > 0 and "cgi-bin" in href[0]:
                    item = NluLinkCollectorItem()

                    item['source_uri'] = response.url
                    item['year'] = year
                    item['volume'] = link.xpath("./text()").extract()
                    item['title'] = hxs.xpath("//title/text()").extract()
                    item['uri'] = "http://www.irbis-nbuv.gov.ua{0}".format(href[0])

                    if item['uri']:
                        yield item
