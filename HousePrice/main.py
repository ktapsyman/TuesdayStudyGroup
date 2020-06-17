from data_loader.data_loader import DataLoader
from preprocessor.AreaPreprocessor import AreaPreprocessor
from preprocessor.CeilingPreprocessor import CeilingPreprocessor

from model.Model import Model

training_data_path = ''
test_data_path = ''

# Model A
modelA_data_loader = DataLoader(training_data_path, test_data_path)
modelA_preprocessors = {
	AreaPreprocessor.__name__:AreaPreprocessor(),
	CeilingPreprocessor.__name__:CeilingPreprocessor()
}

modelA = Model(
	hyper_parameters={}, 
	preprocessors=modelA_preprocessors, 
	data_loader=modelA_data_loader
)

preprocessed_training_data, preprocessed_test_data = modelA.preprocess()
training_result = modelA.train()
test_result = modelA.evaluate()

modelA.export("submission.csv")