import numpy as np
import pandas as pd


class PreprocessorBase():
	def __init__(self):
		self.name = ""
		pass
	
	def preprocess(self, dataframe:pd.DataFrame):
		raise NotImplementedError("This function is not implemented yet!")
