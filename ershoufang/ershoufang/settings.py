# -*- coding: utf-8 -*-

BOT_NAME = 'ershoufang'

SPIDER_MODULES = ['ershoufang.spiders']
NEWSPIDER_MODULE = 'ershoufang.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'ershoufang.pipelines.ErshoufangPipeline': 300,
}
