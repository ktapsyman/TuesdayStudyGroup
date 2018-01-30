import requests
from lxml import html

from Boards import *
from PTTParser import *

PTTBASEURL = "https://www.ptt.cc/"
GOSSIPOVER18DATA = {'from':'/bbs/Gossiping/index.html', 'yes':'yes'}
SEXOVER18DATA = {'from':'/bbs/Sex/index.html', 'yes':'yes'}

def GetNLatestArticles(Board, NArticles=1000):
	#Since we want latest articles, scrape index first
	Url = PTTBASEURL + Board + "/index.html"
	ArticleList = []
	Session = requests.session()
	while len(ArticleList) < NArticles:
		print(Url)
		if Board == GOSSIPING:
			Res = Session.post(PTTBASEURL+'ask/over18', data=GOSSIPOVER18DATA)
		elif Board == SEX:
			Session.post(PTTBASEURL+'/ask/over18', data=SEXOVER18DATA)
			
		ArticlePage = Session.get(Url)
		HtmlTree = html.fromstring(ArticlePage.content)
		ArticleList += ParseArticleList(HtmlTree)
		# Go to previous page
		UrlPreviousPage = GetPreviousPageUrl(HtmlTree)
		Url = PTTBASEURL + UrlPreviousPage
	return ArticleList[:NArticles]

def ConvertTitlesToVectors(TitleList):
	#TODO
	return None

def Main():
	Latest1000Gossips = GetNLatestArticles(GOSSIPING, NArticles=1000)
	for Article in Latest1000Gossips:
		print(Article.Title)
		print(Article.Meta.Author)
		print(Article.Meta.PostDate)
Main()