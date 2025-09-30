import os

from easydict import EasyDict

from utils.enums import PreprocessingType

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

data_config = EasyDict()

data_config.path_to_data = os.path.join(ROOT_DIR, 'data', 'diamonds')
data_config.type = {
    'train': 'diamonds_train.csv',
    'valid': 'diamonds_validation.csv',
    'test': 'diamonds_test.csv'
}

data_config.preprocess_type = PreprocessingType.standartization
data_config.categories = {
    'color': ['J', 'I', 'H', 'G', 'F', 'E', 'D'], 
    'clarity': ['I1', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF'],
    'cut': ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
}