import sys
from collections import Counter

import requests
from lxml import html

from Boards import *
from PTTParser import *
from NLP import *


PTTBASEURL = "https://www.ptt.cc/"
GOSSIPOVER18DATA = {'from':'/bbs/Gossiping/index.html', 'yes':'yes'}
SEXOVER18DATA = {'from':'/bbs/Sex/index.html', 'yes':'yes'}

def GetArticlesByDate(Board, StartDate=None):
	#Since we want latest articles, scrape index first
	Url = PTTBASEURL + Board + "/index.html"
	ArticleDictByDate = {}
	Session = requests.session()
	if Board == GOSSIPING:
		Res = Session.post(PTTBASEURL+'ask/over18', data=GOSSIPOVER18DATA)
	elif Board == SEX:
		Session.post(PTTBASEURL+'ask/over18', data=SEXOVER18DATA)

	while (StartDate is not None):
		ArticlePage = Session.get(Url)
		if 200 != ArticlePage.status_code:
			#Retry
			print(ArticlePage.status_code)
			print("Retry")
			continue
		HtmlTree = html.fromstring(ArticlePage.content)
		for Article in ParseArticleList(HtmlTree):
			print(Article.Title)
			if "ANSI" in Article.Title:
				continue
			ArticleUrl = PTTBASEURL + Article.ContentUrl
			ArticleContentPage = Session.get(ArticleUrl)
			ContentHtmlTree = html.fromstring(ArticleContentPage.content)
			Article.SetContent(ParseArticleContent(ContentHtmlTree))
			PostYearMonth = ParseDetailedPostDate(ContentHtmlTree)
			if PostYearMonth is None:
				continue
			#print(PostYearMonth)
			if PostYearMonth < StartDate:
				break
			if time.strftime("%Y%m%d", PostYearMonth) not in ArticleDictByDate:
				ArticleDictByDate[PostYearMonth] = []	
			ArticleDictByDate[PostYearMonth].append(Article)

		# Go to previous page
		UrlPreviousPage = GetPreviousPageUrl(HtmlTree)
		if "NOPREVPAGE" == UrlPreviousPage:
			exit()
		Url = PTTBASEURL + UrlPreviousPage

	return ArticleDictByDate

def GetArticlesByNumber(Board, NArticles=1000, StartDate=None):
	#Since we want latest articles, scrape index first
	Url = PTTBASEURL + Board + "/index.html"
	ArticleDictByDate = {}
	ArticleList = []
	Session = requests.session()
	if Board == GOSSIPING:
		Res = Session.post(PTTBASEURL+'ask/over18', data=GOSSIPOVER18DATA)
	elif Board == SEX:
		Session.post(PTTBASEURL+'ask/over18', data=SEXOVER18DATA)
	if 0 != NArticles:
		while len(ArticleList) < NArticles:
			ArticlePage = Session.get(Url)
			if 200 != ArticlePage.status_code:
				#Retry
				print(ArticlePage.status_code)
				print("Retry")
				print(len(ArticleList))
				continue
			HtmlTree = html.fromstring(ArticlePage.content)
			ArticleList += [Article for Article in ParseArticleList(HtmlTree) if "ANSI" not in Article.Title]

			# Go to previous page
			UrlPreviousPage = GetPreviousPageUrl(HtmlTree)
			if "NOPREVPAGE" == UrlPreviousPage:
				print(ArticleList[-1].Title)
			Url = PTTBASEURL + UrlPreviousPage
		return ArticleList[:NArticles]
	else:
		return []

def Main():
	LatestArticles = GetArticlesByNumber(C_CHAT, NArticles=int(sys.argv[1]) )

	for Article in LatestArticles:
		print(Article.Title)

	WordSet = []
	for Article in LatestArticles:
		WordSet += CutSentenceIntoWords(Article.Title)

	TF = Counter(WordSet).most_common(10)
	OutputFilename = sys.argv[2] + ".txt"
	with open(OutputFilename, "w") as VocabularyFile:
		for Word in TF:
			VocabularyFile.write(Word[0] + "," + str(Word[1]) + "\n")
	
	#TrainChineseWords()

Main()
