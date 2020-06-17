class Model():
	def __init__(self, algorithm, hyper_parameters, preprocessors, data_loader):
		self.__algorithm = algorithm
		self.__hyper_parameters = {}
		self.__preprocessos = preprocessors
		self.__training_data = None
		self.__test_data = None
		self.__weight = None
		self.__training_result = {}
		self.__evaluation_result = {}

	def preprocess(self):
		return "", ""

	def train(self):
		return ""

	def evaluate(self):
		return ""

	def export(self, path):
		pass

	def __str__(self):
		# TODO: prints out hyper_params, 
		pass