# -*- coding: utf-8 -*-
import scrapy
# from scrapy.contrib.loader import ItemLoader
# from item_try.items import ItemTryItem
from scrapy.loader import ItemLoader
from item_try.items import ItemTryItem
from scrapy.http import request



# crawlera_enabled = True
# crawlera_apikey = '7d7b9060a4b94dec961e87549db3d50a'


class TrySpiderSpider(scrapy.Spider):
    name = 'try-spider'
    allowed_domains = ['backpackers.com.tw']
    start_urls = ['https://www.backpackers.com.tw/forum/forumdisplay.php?f=25']


    def parse(self, response):
    	# loaderr = ItemLoader(item = ItemTryItem(), response = response)
    	# loaderr.add_xpath('title','//a[@id="thread_title_5984"]/text()')
    	# loaderr_data  = loaderr.load_item()
    	# print(loaderr_data)
        # pass
        trs = response.xpath('//tbody[@id = "threadbits_forum_25"]/tr')
        for tr in trs:
        	#only includes non-ad posts
        	if tr.xpath('./td[@colspan]').extract_first() is None:
	        	item = ItemTryItem()
	        	item['title'] = tr.xpath('.//*[starts-with(@id,"td_threadtitle")]//div/a/text()').extract_first()
	        	item['num_of_reply']=tr.xpath('./td[@align="center"]/text()').extract()[0]
	        	item['num_of_view']=tr.xpath('./td[@align="center"]/text()').extract()[1]
	        	item['last_reply_date'] = tr.xpath('.//td[@class ="alt2"]/div[@class="smallfont"]/text()').extract()[0].strip() 
	        	#next page button
	        	url = tr.xpath('.//a[starts-with(@id,"thread_title")]/@href').extract_first()
	        	abs_url = response.urljoin(url)

	        	item['abs_url'] = abs_url

	        	request = scrapy.Request(url =abs_url, callback = self.parse_inner_page)
	        	#store scraped data which is to be retrieved later 
	        	request.meta['item'] = item
	        	yield request

        #testing conrol = whether loop through all posts across pages
        # if response.xpath('//a[@rel="next"]/@href').extract_first() is not None:
        # 	next_btn_url = response.xpath('//a[@rel="next"]/@href').extract_first()
        # 	absolute_next_btn_url = response.urljoin(next_btn_url)
        # 	request2 = scrapy.Request(url =absolute_next_btn_url, callback = self.parse)
        # 	yield request2




    def parse_inner_page(self, response):
    	#if it is in first page
    	# if response.xpath('//a[@rel="prev"]/text()').extract_first():
    	item = response.meta['item']

    	content = response.xpath('.//div[starts-with(@id,"post_message_")]//td[@class="alt2 inner-quote"]/text()').extract()
    	content = ''.join(content)
    	content = content.split()
    	content = ''.join(content)
    	item['content']=content

    	#proceed to next content page
    	next_button_url = response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract_first()   	
    	abs_next_button_url = response.urljoin(next_button_url)
    	request3 = scrapy.Request(url =abs_next_button_url, callback = self.parse_inner_page)
    	request3.meta['item'] = item

    	if response.xpath('//a[@class = "smallfont" and @rel ="next"]//text()').extract_first() is None:
    		yield item




    	# yield item


    	# if response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]:
    	# 	next_button_url = response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]
    	# 	abs_next_button_url = response.urljoin(next_button_url)
    	# 	request = scrapy.Request(url =abs_next_button_url, callback = self.parse_inner_page)
    	# 	request.meta['item'] = item
    	# 	yield request


    	

    	# if response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]:
    	# 	next_button_url = response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]
    	# 	abs_next_button_url = response.urljoin(next_button_url)
    	# 	request = scrapy.Request(url =abs_next_button_url, callback = self.parse_inner_page)
    	# 	request.meta['item'] = item
    	# 	yield request
    	# else:
    	# 	yield item

    	# yield item
  #   	#################################################
  #   	content = response.xpath('.//div[starts-with(@id,"post_message_")]//td[@class="alt2 inner-quote"]/text()').extract()
  #   	#convert all items in a list into a single string
    	
  #   	content = ''.join(content)
  #   	content = content.split()
  #   	content = ''.join(content)
  #   	item['content']=content


  #   	if response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]:
  #   		next_button_url = response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]
  #   		abs_next_button_url = response.urljoin(next_button_url)
  #   		request = scrapy.Request(url =abs_next_button_url, callback = self.parse_inner_page)
  #   		request.meta['item'] = item
  #   		yield request
  #   	else:
  #   		yield item
		# ########################################################
    	#request = scrapy.Request(url =abs_url, callback = self.parse_inner_page)

    	#run if next page button is found
    	# if response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]:
	    # 	next_button_url = response.xpath('//a[@class ="smallfont" and @rel = "next"]/@href').extract()[1]
	    # 	abs_next_button_url = response.urljoin(next_button_url)
    	# request = scrapy.Request(url =None)
    	#request.meta['item'] = item
		# request = scrapy.Request(url =abs_next_button_url, callback = self.parse_inner_page)
		
    	# else:
    	#yield item

    	# return item
    	# pass
    	# print (item)