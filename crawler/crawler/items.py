# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LamaItem(Item):
	name = Field()
	surname = Field()
	location = Field()
	birthdate = Field()
	postalcode = Field()

class ForumPurseblogComItem(Item):
	post = Field()

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class LinkItem():
	url = Field()