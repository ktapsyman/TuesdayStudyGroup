from Article import *
from Meta import *

def GetPreviousPageUrl(Root):
	Path = '//div[@id="action-bar-container"]/div/div[2]/a[2]'
	PreviousPageBtn = Root.xpath(Path)
	if IsNullNode(PreviousPageBtn):
		print("Error : previous page button not found!")
		exit()

	return PreviousPageBtn[0].attrib['href']

def IsNullNode(Node):
	return Node is None or 0 == len(Node) 

def ParseArticleList(Root):
	Path = '//div[@class="r-ent"]'
	ArticleNodes = Root.xpath(Path)
	print(len(ArticleNodes))
	ArticleList = []
	for ArticleNode in ArticleNodes:
		Title = ArticleNode.xpath('div[@class="title"]/a')
		if IsNullNode(Title):
			continue
		Title = Title[0].text
		if "本文已被刪除" in Title:
			continue

		ArticleUrl = ArticleNode.xpath('div[@class="title"]/a')
		if IsNullNode(ArticleUrl):
			continue
		ArticleUrl = ArticleUrl[0].attrib['href']

		Push = ArticleNode.xpath('div[@class="nrec"]/span')
		if IsNullNode(Push):
			Push = 0
		else:
			Push = Push[0].text

		Mark = ArticleNode.xpath('div[@class="mark"]')
		if IsNullNode(Mark):
			Mark = ""
		else:
			Mark = Mark[0].text

		Author = ArticleNode.xpath('div[@class="meta"]/div[1]')
		if IsNullNode(Author):
			continue
		Author = Author[0].text

		PostDate = ArticleNode.xpath('div[@class="meta"]/div[2]')
		if IsNullNode(PostDate):
			continue
		PostDate = PostDate[0].text

		ArticleList.append(Article(Title=Title, Meta=Meta(Author, PostDate), Push=Push, Mark=Mark, ContentUrl=ArticleUrl))
	return ArticleList

def ParseArticleContent(Root):
	#TODO
	return None
