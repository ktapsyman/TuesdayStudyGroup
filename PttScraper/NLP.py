import jieba
from gensim.models import word2vec
from sklearn.cluster import KMeans #Test lul

from Util import *

StopWordSet = LoadStopWords()
jieba.set_dictionary("./JiebaDict/dict.txt.big.txt")
jieba.load_userdict("./JiebaDict/PTTDict.txt")

def CutSentenceIntoWords(Sentence):
	if not Sentence or 0 == len(Sentence):
		print("Input sentence is None or Empty!")
		return []
	Sentence = Sentence.rstrip()
	Sentence = FilterPunctuation(Sentence)

	CorrectWords = []
	Words = jieba.cut(Sentence)
	for Word in Words:
		if Word in StopWordSet:
			continue
		CorrectWords.append(Word)
	return CorrectWords

def TrainChineseWords(Dim=100, OutputFileName="CHTWord2VecModel.model", PretrainedModel="./word2vec.model"):
	Words = word2vec.LineSentence("./Vocabulary.txt")

	Model = word2vec.Word2Vec.load(PretrainedModel)#word2vec.Word2Vec(Words, size=Dim, min_count=1)
	Model.train(Words)
	Model.save(OutputFileName)
	
	return None

def SentenceToVector(Sentence):
	#TODO
	return None

