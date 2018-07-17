# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItemTryPipeline(object):
    def process_item(self, item, spider):
        
  #   	title  = item.get('title')
		# last_reply_date = item.get('last_reply_date')
		# num_of_reply = item.get('num_of_reply')
		# num_of_view = item.get('num_of_view')
		# abs_url = item.get('abs_url')


        return item
