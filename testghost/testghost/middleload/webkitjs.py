# -*- coding: utf-8 -*-

from scrapy.http import Request,HtmlResponse
from testghost.settings import WEBKIT_DOWNLOADER
from ghost import Ghost,Session

class  webkitDownloader(object):
	"""docstring for  webkitDownloader"""
	def process_request(self,request,spider):
		if spider.name in WEBKIT_DOWNLOADER:
			gh = Ghost()
			se = Session(gh,download_images = False)
			se.open(request.url)
			result,resource = se.evaluate('document.documentElement.innerHTML')
			spider.webkit_se = se
			renderedBody = str(resource).encode('utf8')
			return HtmlResponse(request.url,body=renderedBody)
