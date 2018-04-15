from Article import *
from Meta import *
from Util import *

import time

MONTHDICT = {
	'Jan':1,
	'Feb':2,
	'Mar':3,
	'Apr':4,
	'May':5,
	'Jun':6,
	'Jul':7,
	'Aug':8,
	'Sep':9,
	'Oct':10,
	'Nov':11,
	'Dec':12,
}

def GetPreviousPageUrl(Root):
	Path = '//div[@id="action-bar-container"]/div/div[2]/a[2]'
	PreviousPageBtn = Root.xpath(Path)
	if IsNullNode(PreviousPageBtn):
		print("Error : previous page button not found!")
		return "NOPREVPAGE"

	return PreviousPageBtn[0].attrib['href']

def IsNullNode(Node):
	return Node is None or 0 == len(Node) 

def ParseArticleList(Root):
	Path = '//div[@class="r-ent"]'
	ArticleNodes = Root.xpath(Path)
	ArticleList = []
	for ArticleNode in ArticleNodes:
		Title = ArticleNode.xpath('div[@class="title"]/a/text()')
		if IsNullNode(Title):
			continue
		Title = Title[0]
		if "本文已被刪除" in Title:
			continue

		ArticleUrl = ArticleNode.xpath('div[@class="title"]/a')
		if IsNullNode(ArticleUrl):
			continue
		ArticleUrl = ArticleUrl[0].attrib['href']

		Push = ArticleNode.xpath('div[@class="nrec"]/span/text()')
		if IsNullNode(Push):
			Push = 0
		else:
			Push = Push[0]

		Mark = ArticleNode.xpath('div[@class="mark"]/text()')
		if IsNullNode(Mark):
			Mark = ""
		else:
			Mark = Mark[0]

		Author = ArticleNode.xpath('div[@class="meta"]/div[1]/text()')
		if IsNullNode(Author):
			continue
		Author = Author[0]

		PostDate = ArticleNode.xpath('div[@class="meta"]/div[2]/text()')
		if IsNullNode(PostDate):
			continue
		PostDate = PostDate[0]

		ArticleList.append(Article(Title=Title, Meta=Meta(Author, PostDate), Push=Push, Mark=Mark, ContentUrl=ArticleUrl))
	return ArticleList

def ParseArticleContent(Root):
	#TODO
	Path = '//div[@id="main-content"]/text()'

	ArticleContentNode = Root.xpath(Path)
	if IsNullNode(ArticleContentNode):
		print("此文章無內文！")
		return ""

	ArticleContentText = ArticleContentNode[0]

	return ArticleContentText

def ParseDetailedPostDate(Root):
	Path = '//div[@id="main-content"]/div[@class="article-metaline"][3]/span[@class="article-meta-value"]/text()'
	DetailedPostDateNode = Root.xpath(Path)
	if IsNullNode(DetailedPostDateNode):
		return None

	DetailedPostDate = time.strptime(DetailedPostDateNode[0], '%a %b %d %H:%M:%S %Y')
	
	return DetailedPostDate

