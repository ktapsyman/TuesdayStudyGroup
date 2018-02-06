import re
import os

def FilterPunctuation(InputStr):
	return re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~\[\]［］@#￥%……&*（）]+", "", InputStr)

def LoadStopWords(Path="./JiebaDict/StopWords.txt"):
	if not os.path.isfile(Path):
		print("No stop words file provided!")
		return []

	StopWords = []
	with open(Path, "r") as StopWordsFile:
		StopWords = StopWordsFile.read().splitlines()
		print(StopWords)
	return StopWords
