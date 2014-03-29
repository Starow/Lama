from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from crawler.items import LamaItem

# Launch spiderman : scrapy crawl LamaSpider -o items.json -t json
class LamaSpider(CrawlSpider):
   name = "spiderlama"
   allowed_domains = ['linkedin.com']
   #allowed_domains = ["dmoz.org"]
   start_urls = ["http://fr.linkedin.com/pub/pierre-heyd/82/b46/759"]
   #//li[@class="with-photo"]/a/@href   #### LINKS ####

   #http://fr.linkedin.com/pub/valentin-lacave/82/94/bb2

   #http://directory.google.com/Category/Subcategory/Another_Subcategory
   #allow='directory.google.com/[A-Z][a-zA-Z_/0-9]+$',

   rules = (
        Rule(
        	SgmlLinkExtractor(
        		allow='fr.linkedin.com/pub/[a-zA-Z0-9/_-]+$',
        		#restrict_xpaths='//li[@class="with-photo"]/a/@href'
        		),
        	 callback = 'parse_lama', 
        	 follow = True, 
        	 ),
    )

   def parse_lama(self, response):
       self.log('Response.url %s' % response.url)
       self.log('Rules %s' % LamaSpider.name)

       sel = Selector(response)
       sites = sel.xpath('//html')
       items = []
       for site in sites:
           item = LamaItem()
           item['surname'] = site.xpath('//title/text()').re('(\w+)')[0]
           item['name'] = site.xpath('//title/text()').re('(\w+)')[1]
           item['location'] = site.xpath('//span[@class="locality"]/text()').re('(\w+)')[2]
           items.append(item)
       return items

   def parse_link(self, response):
   	   self.log('This is the parse_link function')

   	   links = sel.xpath('//li[@class="with-photo"]')

   	   for link in links:
   	   	   item = linkItem()
   	   	   item['url'] = link.xpath('a/@href').extract()
   	   	   yield item