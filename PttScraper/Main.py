import requests
from lxml import html

from Boards import *
from PTTParser import *
from NLP import *

PTTBASEURL = "https://www.ptt.cc/"
GOSSIPOVER18DATA = {'from':'/bbs/Gossiping/index.html', 'yes':'yes'}
SEXOVER18DATA = {'from':'/bbs/Sex/index.html', 'yes':'yes'}

def GetArticles(Board, NArticles=1000, StartDate=None, EndDate=None):
	#Since we want latest articles, scrape index first
	Url = PTTBASEURL + Board + "/index.html"
	ArticleList = []
	Session = requests.session()
	if Board == GOSSIPING:
		Res = Session.post(PTTBASEURL+'ask/over18', data=GOSSIPOVER18DATA)
	elif Board == SEX:
		Session.post(PTTBASEURL+'ask/over18', data=SEXOVER18DATA)
	while len(ArticleList) < NArticles:		
		ArticlePage = Session.get(Url)
		if 200 != ArticlePage.status_code:
			#Retry
			print(ArticlePage.status_code)
			print("Retry")
			print(len(ArticleList))
			continue
		HtmlTree = html.fromstring(ArticlePage.content)
		ArticleList += ParseArticleList(HtmlTree)
		print("Current progress : " + str(len(ArticleList)) + "/" + str(NArticles))
		# Go to previous page
		UrlPreviousPage = GetPreviousPageUrl(HtmlTree)
		if "NOPREVPAGE" == UrlPreviousPage:
			print(ArticleList[-1].Title)
			exit()
		Url = PTTBASEURL + UrlPreviousPage

	ArticleList = ArticleList[:NArticles]
	for Article in ArticleList:
		ArticleUrl = PTTBASEURL + Article.ContentUrl
		ArticleContentPage = Session.get(ArticleUrl)
		HtmlTree = html.fromstring(ArticleContentPage.content)
		Article.SetContent(ParseArticleContent(HtmlTree))
	return ArticleList

def Main():
	Latest1000Gossips = GetArticles(GOSSIPING, NArticles=600000, StartDate=None, EndDate=None)
	WordSet = []
	for Article in Latest1000Gossips:
		WordSet += CutSentenceIntoWords(Article.Title)
		WordSet += CutSentenceIntoWords(Article.Content)
	WordSet = set(WordSet)

	with open("./Vocabulary.txt", "w") as VocabularyFile:
		VocabularyFile.write(" ".join(WordSet))
	
	TrainChineseWords()

Main()
