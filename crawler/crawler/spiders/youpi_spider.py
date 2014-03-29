from scrapy.spider import Spider
from scrapy.selector import Selector, HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from crawler.items import ForumPurseblogComItem

class ForumSpider(CrawlSpider):
    name = 'forum_purseblog_spider'
    allowed_domains = ['forum.purseblog.com']
    start_urls = ['http://forum.purseblog.com/handbags-and-purses/']

    total_posts = 0

    rules = (
        # Extract all pages one by one
        Rule(SgmlLinkExtractor(allow=('index\d{1,3}\.html', ),
                               deny=('announcement\.php',
                                     'member\.php',
                                     '#post'))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(
            allow=('[\w]+\.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
        print "(Total posts: %d)Page: %s" % (self.total_posts, response.url)

        hxs = HtmlXPathSelector(response)
        posts = self.strip(hxs.select('//div[@class="msgfield"]/text()').extract())

        for post in posts:
            item = ForumPurseblogComItem()
            item['post'] = post
            self.total_posts += 1
            yield  item


    def strip(self, lst):
        return [self.normalize_space(item) for item in lst if item.strip()]


    def normalize_space(self, text):
        return RE_SPACE.sub(' ', text).strip()
