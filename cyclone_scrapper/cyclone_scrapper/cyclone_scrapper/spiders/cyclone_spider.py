from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cyclone_scrapper.items import CycloneScrapperItem
from scrapy import Selector


class CycloneSpider(BaseSpider):

	name = "cyclone_scrapper"
	allowed_domains = ["rammb.cira.colostate.edu"]
	start_urls = ["http://rammb.cira.colostate.edu/products/tc_realtime/index.asp"]

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@id="wrapper"]')

		items = []

		for site in sites:
			item = CycloneScrapperItem()
			item['title'] = site.select('div[@id="content"]/div[@class="basin_storms"]/h3/text()').extract()
			item['location'] = site.select('div[@id="content"]/div[@class="basin_storms"]/h3/text()').extract()
			item['history'] = site.select('//div[@id="sidebar"]/ul[@class="list_level_1"]/li/span[@class="list_heading_span"]/ul/li/text()').extract()
			item['link'] = site.select('//div[@id="sidebar"]/ul[@class="list_level_1"]/li/a/text()').extract()
			item['forecast'] = site.select('//div[@id="content"]/div[@class="basin_storms"]/ul/li/a/text()').extract()
			items.append(item)
		return items




