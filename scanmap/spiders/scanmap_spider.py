import scrapy

class ScanMapSpider(scrapy.Spider):
	def start_requests(self):
		urls = ['http://quotes.toscrape.com/page/1/',]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
		
	def parse(self,response):
	