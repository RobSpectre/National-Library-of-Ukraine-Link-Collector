# National Library of Ukraine Link Collector

A Scrapy spider to collect links to volumes of academic journals held by the
National Library of Ukraine.

Created for [Saving Ukrainian Cultural Heritage
Online](https://www.sucho.org/).


## Usage

1) Install requirements.

Install scrapy (preferably in a virtualenv).

`pip install scrapy`

2) Enter package directory.

`cd nlu_link_collector`

3) Launch spider.

`scrapy crawl nlu_link_collector`


## Important files

* `nlu_link_collector/nlu_link_collector/spiders/nlu_link_spider.py` - Main
  logic for collection.
* `nlu_link_collector/resources/nlu_links.csv` - Starting links for journals
* `nlu_link_collector/nlu_link_collector_links.csv` - Default output of spider.


## Meta

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Crafted in solidarity by [Rob Spectre](https://brooklynhacker.com).
