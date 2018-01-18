# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector 

class RunjsSpider(scrapy.Spider):
    name = 'runjs'
    allowed_domains = ['movie.douban.com']
    start_urls = 'https://movie.douban.com/chart'
    webkit_se = None
    headers = {
        "Accept":r"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        ,"Host":"movie.douban.com"
    	,"Referer":"https://movie.douban.com/explore"
        ,"Cookie":r'bid=xBFrO_pyU64; viewed="26274202"; gr_user_id=53c14f3c-3630-425e-87a0-b5b164548a91; _vwo_uuid_v2=2F33C2A2B9203058CBF8736CA8B24F69|b692153a210b98f48c5b58645b623c0d; ll="118281"; __yadk_uid=OWBPoqnxD3Hk7qpPbvnMS4qNoPiymzvV; ps=y; dbcl2="172631816:Dkd9TxAolpg"; push_noty_num=0; push_doumail_num=0; ap=1; ck=D7NU; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1516245987%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; __utma=30149280.1318808727.1513299286.1516179647.1516245987.14; __utmc=30149280; __utmz=30149280.1516245987.14.10.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.2141600912.1515997536.1516092203.1516245987.8; __utmc=223695111; __utmz=223695111.1516245987.8.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=e2c7faaed863bf2b.1515997536.8.1516247663.1516092222.'
    	,"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
    }
    def start_requests(self):
    	yield scrapy.Request(self.start_urls,headers=self.headers,callback=self.parse)

    def parse(self, response):
    	result,resouce = self.webkit_se.evaluate("""
    			document.getElementById("content").getElementsByTagName("table")[0].innerHTML
    		""")
    	del resouce
    	#result = HtmlResponse(result)
    	print "________________________________________________"
    	print Selector(text=result).xpath("//td[@valign='top']/a/@title").extract()
    	print "________________________________________________"
    	yield result     
