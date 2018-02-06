import jieba
from gensim.models import word2vec
from sklearn.cluster import KMeans #Test lul

from Util import *

StopWordSet = LoadStopWords()

def CutSentenceIntoWords(Sentence):
	if not Sentence or 0 == len(Sentence):
		print("Input sentence is None or Empty!")
		return []
	Sentence = Sentence.rstrip()
	Sentence = FilterPunctuation(Sentence)

	Words = jieba.cut(Sentence)
	for Word in Words:
		if Word in StopWordSet:
			Words.remove(Word)

	return Words

def TrainChineseWords(Words, Dim=100, OutputFileName="CHTWord2VecModel.model"):
	if not Words or 0 == len(Words):
		print("No Words input")
		exit()

	Model = word2vec.Word2Vec(Words, size=Dim)
	Model.save(OutputFileName)
	
	return None

def SentenceToVector(Sentence):
	#TODO
	return None

