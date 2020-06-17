import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataLoader():
	def __init__(self, training_data_path, test_data_path):
		self.training_data_path = training_data_path
		self.test_data_path = test_data_path
		self.training_data = None
		self.test_data = None

	def load(self):
		self.training_data = pd.read_csv(self.training_data_path)
		self.test_data = pd.read_csv(self.test_data_path)
	
	def get_training_data(self):
		pass

	def get_test_data(self):
		pass


