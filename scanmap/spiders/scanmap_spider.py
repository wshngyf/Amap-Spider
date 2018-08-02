import scrapy
import json
from scanmap.items import ScanmapItem
class ScanMapSpider(scrapy.Spider):
	name = 'ScanMapSpider'
	def start_requests(self):
		urls = ['http://restapi.amap.com/v3/place/text?key=6dfbd82a982fb0dab8fde453623e10ac&keywords=%E9%A4%90%E9%A5%AE&types=&city=%E6%B2%81%E9%98%B3&children=1&offset=20&page=1&extensions=all',]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
		
	def parse(self,response):
		content = response.body
		items = []
		if not content:
			return
		strjson = json.loads(content)
		jsonarr = strjson['pois']
		for i in jsonarr:
			item = ScanmapItem()
			item['poi_name']=i['name']
			items.append(item)
		return items
	